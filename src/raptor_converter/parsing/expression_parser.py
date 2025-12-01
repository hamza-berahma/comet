"""
ExpressionParser
A robust, precedence-climbing parser for handling mathematical and logical
expressions. This fixes the critical operator precedence bug.
"""

import re
from ..ast import nodes
from ..utils.exceptions import ParsingError

class ExpressionParser:
    """
    Parses string expressions into an AST, respecting operator precedence.
    Used by both RapcodeParser and RaptorXMLParser.
    """
    
    def __init__(self, raw_tokens):
        self.tokens = raw_tokens
        self.pos = 0

    def parse(self):
        """Public entry point to parse the full expression."""
        if not self.tokens:
            return None
        try:
            ast = self._parse_logical_or()
            if self._peek():
                raise ParsingError(f"Unexpected token: '{self._peek()}'")
            return ast
        except IndexError:
            raise ParsingError("Unexpected end of expression.")

    # --- Token Helpers ---
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

    # --- Grammar Rules (Recursive Descent) ---
    
    # Precedence Level 6: OR
    def _parse_logical_or(self):
        node = self._parse_logical_and()
        while self._match("OR"):
            right = self._parse_logical_and()
            node = nodes.create_binary_expression("OR", node, right)
        return node

    # Precedence Level 5: AND
    def _parse_logical_and(self):
        node = self._parse_comparison()
        while self._match("AND"):
            right = self._parse_comparison()
            node = nodes.create_binary_expression("AND", node, right)
        return node
    
    # Precedence Level 4: ==, !=, <, >, <=, >=
    def _parse_comparison(self):
        node = self._parse_additive()
        op = self._match("==", "!=", "<", ">", "<=", ">=")
        if op:
            right = self._parse_additive()
            node = nodes.create_binary_expression(op, node, right)
        return node

    # Precedence Level 3: +, -
    def _parse_additive(self):
        node = self._parse_multiplicative()
        while True:
            op = self._match("+", "-")
            if not op:
                break
            right = self._parse_multiplicative()
            node = nodes.create_binary_expression(op, node, right)
        return node

    # Precedence Level 2: *, /, MOD
    def _parse_multiplicative(self):
        node = self._parse_unary()
        while True:
            op = self._match("*", "/", "MOD")
            if not op:
                break
            right = self._parse_unary()
            node = nodes.create_binary_expression(op, node, right)
        return node
    
    # Precedence Level 1: NOT, - (unary)
    def _parse_unary(self):
        op = self._match("NOT", "-")
        if op:
            argument = self._parse_unary()
            return nodes.create_unary_expression(op, argument)
        return self._parse_atom()

    # Precedence Level 0: Atoms (Literals, Vars, Parentheses)
    def _parse_atom(self):
        token = self._peek()

        if token is None:
            raise ParsingError("Unexpected end of expression.")

        if token == "(":
            self._consume("(")
            node = self._parse_logical_or() # Start from top precedence
            self._consume(")")
            return node
        
        if token == "INPUT":
            self._consume("INPUT")
            self._consume("(")
            # The prompt can be any valid expression
            prompt_node = self._parse_logical_or()
            self._consume(")")
            return nodes.create_input_expression(prompt_node)

        if token == "TRUE":
            self._consume()
            return nodes.create_literal(True)
        if token == "FALSE":
            self._consume()
            return nodes.create_literal(False)
        
        if token.startswith('"'):
            return nodes.create_literal(self._consume())
        
        if re.fullmatch(r'\d+(\.\d*)?', token):
            try:
                val = int(self._consume())
            except ValueError:
                val = float(token) # Re-get token before consuming
            return nodes.create_literal(val)

        if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', token):
            return nodes.create_identifier(self._consume())
        
        raise ParsingError(f"Unexpected token in expression: '{token}'")
    
    