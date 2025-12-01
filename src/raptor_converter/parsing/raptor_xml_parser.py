"""
RaptorXMLParser
Parses .rap (XML) files into an AST.
"""
import re
import xml.etree.ElementTree as ET
from .base_parser import BaseParser
from .expression_parser import ExpressionParser
from .rapcode_parser import RapcodeParser
from ..ast import nodes
from ..utils.exceptions import ParsingError

class RaptorXMLParser(BaseParser):
    """
    Loads a Raptor XML file (.rap) and returns a JSON AST.
    This version uses the robust ExpressionParser.
    """
    
    NAMESPACES = {
        '': 'http://schemas.datacontract.org/2004/07/RAPTOR_Avalonia_MVVM.ViewModels',
        'i': 'http://www.w3.org/2001/XMLSchema-instance',
        'a': 'http://schemas.datacontract.org/2004/07/raptor',
        'b': 'http://www.w3.org/2001/XMLSchema'
    }

    def __init__(self):
        # We reuse the tokenizer from RapcodeParser
        self.tokenizer = RapcodeParser()._tokenize
        
    def parse(self, content: str) -> dict:
        try:
            root = ET.fromstring(content)
            start_node = root.find('.//a:Start', self.NAMESPACES)
            if start_node is None:
                raise ParsingError("Could not find the <Start> node in the XML file.")
            
            successor_container = self._find_element_robust(start_node, 'a:_Successor')
            first_node = self._find_actual_component(successor_container)
            body = self._parse_raptor_node(first_node)
            return nodes.create_program(body)
        except ET.ParseError as e:
            raise ParsingError(f"XML Parse Error: {e}")

    # --- XML Helper Methods ---

    def _get_node_type(self, xml_node):
        if xml_node is None: return None
        type_attr = xml_node.get(f"{{{self.NAMESPACES['i']}}}type")
        if type_attr: return type_attr.split(':')[-1]
        return xml_node.tag.split('}')[-1]

    def _find_element_robust(self, xml_node, tag):
        if xml_node is None: return None
        element = xml_node.find(tag, self.NAMESPACES)
        if element is None:
            local_tag = tag.split(':')[-1]
            element = xml_node.find(local_tag)
        return element

    def _safe_get_text(self, xml_node, tag, default=''):
        element = self._find_element_robust(xml_node, tag)
        return element.text if element is not None and element.text is not None else default

    def _find_actual_component(self, container_element):
        if container_element is None: return None
        if container_element.get(f"{{{self.NAMESPACES['i']}}}type"):
            return container_element
        for child in container_element:
            if isinstance(child.tag, str): return child
        return None

    # --- Expression Parsing ---

    def _parse_expression(self, expr_str: str) -> dict:
        """
        Parses a Raptor expression string using the robust ExpressionParser.
        """
        if not expr_str:
            raise ParsingError("Empty expression string found in XML.")
            
        # 1. Pre-process: Map Raptor syntax to Rapcode syntax
        # Basic replacements
        expr_str = expr_str.replace(' mod ', ' MOD ')
        expr_str = expr_str.replace(' and ', ' AND ')
        expr_str = expr_str.replace(' or ', ' OR ')
        expr_str = expr_str.replace(' not ', ' NOT ')
        
        # Handle string concatenation (+)
        # Raptor uses '+' for both math and string concat. We assume type
        # correctness from the user.
        
        # Handle comparisons: = (becomes ==) and <> (becomes !=)
        # We must be careful not to replace :=, ==, <=, >=
        # This regex replaces '=' only if it's not part of another operator
        expr_str = re.sub(r'(?<![:!<>=])=(?!=)', '==', expr_str)
        expr_str = expr_str.replace('<>', '!=')

        # 2. Tokenize and Parse
        try:
            tokens = self.tokenizer(expr_str)
            return ExpressionParser(tokens).parse()
        except Exception as e:
            raise ParsingError(f"Failed to parse expression '{expr_str}': {e}")

    # --- Node Parsing (Recursive) ---

    def _parse_raptor_node(self, xml_node):
        if xml_node is None or xml_node.get(f"{{{self.NAMESPACES['i']}}}nil") == 'true':
            return []
            
        node_type = self._get_node_type(xml_node)
        ast_nodes = []
        current_ast_node = None

        try:
            if node_type == 'Rectangle':
                text = self._safe_get_text(xml_node, 'a:_text_str')
                if ':=' in text:
                    left_str, right_str = text.split(':=', 1)
                    left_node = self._parse_expression(left_str.strip())
                    right_node = self._parse_expression(right_str.strip())
                    current_ast_node = nodes.create_assignment_statement(left_node, right_node)
                else:
                    # Could be a procedure call, which we treat as an expression statement
                    # For this project, we'll assume it's an unhandled rectangle.
                    pass 
                    
            elif node_type == 'Parallelogram':
                is_input = self._safe_get_text(xml_node, 'a:_is_input', 'false').lower() == 'true'
                text_str = self._safe_get_text(xml_node, 'a:_text_str').strip()
                
                if is_input:
                    prompt_text = self._safe_get_text(xml_node, 'a:_prompt').strip()
                    if prompt_text.startswith('"') and prompt_text.endswith('"'):
                        prompt_text = prompt_text[1:-1]
                    # Input prompt is a literal string
                    prompt_node = nodes.create_literal(prompt_text)
                    current_ast_node = nodes.create_assignment_statement(
                        nodes.create_identifier(text_str),
                        nodes.create_input_expression(prompt_node)
                    )
                else:
                    arg_node = self._parse_expression(text_str)
                    current_ast_node = nodes.create_output_statement(arg_node)

            elif node_type == 'IF_Control':
                text = self._safe_get_text(xml_node, 'a:_text_str')
                left_child_container = self._find_element_robust(xml_node, 'a:_left_Child')
                right_child_container = self._find_element_robust(xml_node, 'a:_right_Child')
                
                consequent_body = self._parse_raptor_node(self._find_actual_component(left_child_container))
                alternate_body = self._parse_raptor_node(self._find_actual_component(right_child_container))
                
                current_ast_node = nodes.create_if_statement(
                    self._parse_expression(text),
                    consequent_body,
                    alternate_body if alternate_body else None
                )

            elif node_type == 'Loop':
                # This is the "mid-test" loop.
                # We transform it into a `While(True)` loop with an `If(test) { Break }` inside.
                text = self._safe_get_text(xml_node, 'a:_text_str') # This is the EXIT condition
                
                before_child_container = self._find_element_robust(xml_node, 'a:_before_Child')
                after_child_container = self._find_element_robust(xml_node, 'a:_after_Child')
                
                before_body = self._parse_raptor_node(self._find_actual_component(before_child_container))
                after_body = self._parse_raptor_node(self._find_actual_component(after_child_container))
                
                # The "if-break" node
                if_break_node = nodes.create_if_statement(
                    self._parse_expression(text),
                    [nodes.create_break_statement()] # Consequent is a break
                )
                
                loop_body_statements = before_body + [if_break_node] + after_body
                current_ast_node = nodes.create_while_statement(
                    nodes.create_literal(True),
                    loop_body_statements
                )

        except Exception as e:
            raise ParsingError(f"Error parsing XML node of type '{node_type}': {e}")

        if current_ast_node:
            ast_nodes.append(current_ast_node)
            
        # Recursively parse the successor
        successor_container = self._find_element_robust(xml_node, 'a:_Successor')
        successor_node = self._find_actual_component(successor_container)
        if successor_node is not None:
            ast_nodes.extend(self._parse_raptor_node(successor_node))
            
        return ast_nodes