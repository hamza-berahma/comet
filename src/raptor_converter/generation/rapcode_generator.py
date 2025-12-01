# File: raptor_converter/generation/rapcode_generator.py
"""
RapcodeGenerator
Generates .rapcode text from an AST.
"""
from .base_generator import BaseGenerator
from .expression_utils import expression_to_string
from ..utils.exceptions import GenerationError

class RapcodeGenerator(BaseGenerator):
    """
    Generates formatted .rapcode text from an AST.
    """
    
    def generate(self, ast: dict) -> str:
        try:
            return self._generate_nodes(ast.get("body", []), 0)
        except Exception as e:
            raise GenerationError(f"Rapcode generation failed: {e}")

    def _generate_nodes(self, ast_nodes, indent_level):
        """Recursively traverses the AST and generates formatted .rapcode lines."""
        code_lines = []
        indent = "  " * indent_level

        for node in ast_nodes:
            node_type = node.get("type")

            if node_type == "AssignmentStatement":
                left = expression_to_string(node.get("left"))
                right = expression_to_string(node.get("right"))
                code_lines.append(f'{indent}{left} := {right}')

            elif node_type == "ExpressionStatement":
                expression = node.get("expression", {})
                if expression.get("callee") == "Output":
                    arg_node = expression.get("arguments", [])[0]
                    arg_string = expression_to_string(arg_node)
                    code_lines.append(f'{indent}OUTPUT {arg_string}')

            elif node_type == "IfStatement":
                consequent = node.get("consequent", {}).get("body", [])
                alternate = node.get("alternate", {}).get("body", []) if node.get("alternate") else []
                test = expression_to_string(node.get("test"))

                code_lines.append(f"{indent}IF {test} THEN")
                code_lines.extend(self._generate_nodes(consequent, indent_level + 1).splitlines())
                
                if alternate:
                    code_lines.append(f"{indent}ELSE")
                    code_lines.extend(self._generate_nodes(alternate, indent_level + 1).splitlines())
                
                code_lines.append(f"{indent}ENDIF")

            elif node_type == "WhileStatement":
                test = node.get("test")
                
                # FIX: Correctly generate LOOP or WHILE...DO
                if test.get("type") == "Literal" and test.get("value") is True:
                    code_lines.append(f"{indent}LOOP")
                else:
                    test_expr = expression_to_string(test)
                    code_lines.append(f"{indent}WHILE {test_expr} DO")
                
                body = node.get("body", {}).get("body", [])
                code_lines.extend(self._generate_nodes(body, indent_level + 1).splitlines())
                code_lines.append(f"{indent}ENDLOOP")
                
            elif node_type == "BreakStatement":
                code_lines.append(f"{indent}BREAK")

        return '\n'.join(code_lines)