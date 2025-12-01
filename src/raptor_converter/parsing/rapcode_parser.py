"""
RapcodeParser
Parses .rapcode text files into an AST.
"""
import re
from .base_parser import BaseParser
from .expression_parser import ExpressionParser
from ..ast import nodes
from ..utils.exceptions import ParsingError

class RapcodeParser(BaseParser):
    """
    Parses a string of .rapcode and returns a JSON AST.
    This version correctly handles operator precedence.
    """

    NEWLINE = "<NEWLINE>"
    
    # This regex is designed to be simple and "good enough".
    # It correctly handles quoted strings with escaped quotes.
    TOKEN_REGEX = re.compile(
        r'(\s+)'                               # 1. Whitespace
        r'|(--[^\n]*)'                         # 2. Comments
        r'|([A-Za-z_][A-Za-z0-9_]*)'           # 3. Identifiers/Keywords (IF, LOOP, AND, etc.)
        r'|(:=|==|!=|<=|>=|<|>|\+|-|\*|/|\^)'  # 4. Multi-char operators
        r'|(\d+(?:\.\d*)?)'                    # 5. Numbers (int or float)
        r'|("(?:\\.|[^"\\])*")'                # 6. Strings (handles escaped quotes)
        r'|(.)'                                # 7. Single-char tokens ( ( ) etc.)
    )
    
    RESERVED_KEYWORDS = {
        "IF", "THEN", "ELSE", "ENDIF", "WHILE", "DO", "LOOP", "ENDLOOP",
        "BREAK", "INPUT", "OUTPUT", "TRUE", "FALSE", "NOT", "AND", "OR", "MOD"
    }

    def __init__(self):
        self.tokens = []
        self.pos = 0

    def _tokenize(self, code):
        """Splits the code into tokens, respecting string literals."""
        raw_tokens = []
        for match in self.TOKEN_REGEX.finditer(code):
            group_idx, token = next((i, m) for i, m in enumerate(match.groups(), 1) if m is not None)
            
            if group_idx == 1:  # Whitespace (may include newlines)
                newline_count = token.count("\n")
                if newline_count:
                    raw_tokens.extend([self.NEWLINE] * newline_count)
                continue
            if group_idx == 2: # Comment
                continue # Skip
                
            raw_tokens.append(token)
            
        return raw_tokens

    def _peek(self): 
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None
    
    def _consume(self, expected=None):
        token = self._peek()
        if expected and token != expected:
            raise ParsingError(f"Expected '{expected}' but found '{token}' at position {self.pos}")
        self.pos += 1
        return token
    
    def _match(self, *token_types):
        if self._peek() in token_types:
            return self._consume()
        return None

    def _is_expression_start(self, token):
        if token is None: return False
        if token in ("(", "NOT", "-", "INPUT", "TRUE", "FALSE"): return True
        if token.startswith('"'): return True
        if token[0].isdigit(): return True
        if token[0].isalpha() and token not in self.RESERVED_KEYWORDS: return True
        return False

    def parse(self, content):
        self.tokens = self._tokenize(content)
        self.pos = 0
        statements = []
        self._skip_newlines()
        while self._peek() is not None:
            stmt = self._parse_statement()
            if stmt is not None:
                statements.append(stmt)
            self._skip_newlines()
        return nodes.create_program(statements)

    def _parse_statement(self):
        self._skip_newlines()
        token = self._peek()
        if token is None or token in {"ELSE", "ENDIF", "ENDLOOP"}:
            return None
        if token == "IF": 
            return self._parse_if()
        if token == "LOOP" or token == "WHILE": 
            return self._parse_loop()
        if token == "BREAK": 
            self._consume("BREAK")
            return nodes.create_break_statement()
        if token == "OUTPUT": 
            return self._parse_output()
        
        # Must be an assignment or expression statement
        if not self._is_expression_start(token):
             raise ParsingError(f"Unexpected token: '{token}'. Expected start of statement.")
             
        # Use the expression parser
        expr_ast = self._parse_expression()
        
        if self._match(":="):
            right = self._parse_expression()
            if expr_ast["type"] != "Identifier":
                raise ParsingError("Invalid left-hand side in assignment.")
            return nodes.create_assignment_statement(expr_ast, right)
        
        # If it wasn't an assignment, it's an error, as rapcode
        # doesn't support standalone expression statements (like just 'x + 1')
        raise ParsingError(f"Invalid statement. Did you mean 'OUTPUT {token}...' or an assignment?")

    def _parse_expression(self):
        """Splits off the tokens for an expression and parses them."""
        expr_tokens = []
        open_parens = 0
        
        while True:
            token = self._peek()
            if not token:
                break
            
            # Check for end of expression
            if token == self.NEWLINE and open_parens == 0:
                break
            if token == ":=" and open_parens == 0:
                break
            if token in ("THEN", "DO", "ENDLOOP") and open_parens == 0:
                break
            # Check for start of another statement (end of line)
            if token in ("IF", "LOOP", "WHILE", "BREAK", "OUTPUT") and open_parens == 0:
                break
                
            expr_tokens.append(self._consume())
            
            if token == "(":
                open_parens += 1
            elif token == ")":
                open_parens -= 1
                if open_parens < 0:
                    break # Let the parser handle the error

        if not expr_tokens:
            raise ParsingError("Expected expression.")
            
        return ExpressionParser(expr_tokens).parse()

    def _parse_if(self):
        self._consume("IF")
        test = self._parse_expression()
        self._consume("THEN")
        consequent_body = []
        while True:
            self._skip_newlines()
            upcoming = self._peek()
            if upcoming in ("ELSE", "ENDIF") or upcoming is None:
                break
            consequent_body.append(self._parse_statement())
        
        alternate_body = None
        if self._match("ELSE"):
            alternate_body = []
            while True:
                self._skip_newlines()
                if self._peek() == "ENDIF":
                    break
                alternate_body.append(self._parse_statement())
        
        self._consume("ENDIF")
        return nodes.create_if_statement(test, consequent_body, alternate_body)

    def _parse_loop(self):
        if self._match("LOOP"):
            test = nodes.create_literal(True)
        elif self._match("WHILE"):
            test = self._parse_expression()
            self._consume("DO")
        else:
            raise ParsingError("Expected 'LOOP' or 'WHILE'.")

        body = []
        while True:
            self._skip_newlines()
            if self._peek() == "ENDLOOP":
                break
            body.append(self._parse_statement())
        self._consume("ENDLOOP")
        
        return nodes.create_while_statement(test, body)

    def _parse_output(self):
        self._consume("OUTPUT")
        arg_node = self._parse_expression()
        return nodes.create_output_statement(arg_node)

    def _skip_newlines(self):
        while self._peek() == self.NEWLINE:
            self._consume()