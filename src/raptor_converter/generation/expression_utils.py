"""
Helpers for turning AST expressions back into readable strings.
"""
from ..utils.exceptions import GenerationError


def expression_to_string(node):
    """Convert an expression AST node (dict) to a string representation."""
    if node is None:
        return ""

    node_type = node.get("type")

    if node_type == "Literal":
        value = node.get("value")
        if isinstance(value, str):
            return f'"{value}"'
        if isinstance(value, bool):
            return "TRUE" if value else "FALSE"
        return str(value)

    if node_type == "Identifier":
        return node.get("name", "")

    if node_type == "BinaryExpression":
        left = expression_to_string(node.get("left"))
        right = expression_to_string(node.get("right"))
        operator = node.get("operator", "")
        return f"({left} {operator} {right})"

    if node_type == "UnaryExpression":
        argument = expression_to_string(node.get("argument"))
        operator = node.get("operator", "")
        if operator == "NOT":
            return f"NOT {argument}"
        return f"({operator}{argument})"

    if node_type == "CallExpression":
        callee = node.get("callee", "")
        args = [expression_to_string(arg) for arg in node.get("arguments", [])]
        if callee == "Input":
            prompt = args[0] if args else ""
            return f"INPUT({prompt})"
        return f'{callee}({", ".join(args)})'

    raise GenerationError(f"Unknown expression node type: {node_type}")

