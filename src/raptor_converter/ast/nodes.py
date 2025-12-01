"""
AST Node Factory Functions
Provides simple factory functions to ensure all AST nodes (represented as dicts)
have a consistent structure.
"""

def create_program(body):
    return {"type": "Program", "body": body}

def create_block(body):
    return {"type": "BlockStatement", "body": body}

def create_literal(value):
    if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
        value = value[1:-1] 
    return {"type": "Literal", "value": value}

def create_identifier(name):
    return {"type": "Identifier", "name": name}

def create_binary_expression(operator, left, right):
    return {"type": "BinaryExpression", "operator": operator, "left": left, "right": right}

def create_unary_expression(operator, argument):
    return {"type": "UnaryExpression", "operator": operator, "argument": argument}

def create_call_expression(callee, arguments):
    return {"type": "CallExpression", "callee": callee, "arguments": arguments}

def create_input_expression(prompt_node):
    """Creates a standardized 'Input' call node."""
    return {"type": "CallExpression", "callee": "Input", "arguments": [prompt_node]}

def create_output_statement(argument_node):
    """Creates a standardized 'Output' statement."""
    return {
        "type": "ExpressionStatement",
        "expression": create_call_expression("Output", [argument_node])
    }

def create_assignment_statement(left, right):
    return {"type": "AssignmentStatement", "left": left, "right": right}

def create_if_statement(test, consequent_body, alternate_body=None):
    return {
        "type": "IfStatement",
        "test": test,
        "consequent": create_block(consequent_body),
        "alternate": create_block(alternate_body) if alternate_body is not None else None
    }

def create_while_statement(test, body):
    return {"type": "WhileStatement", "test": test, "body": create_block(body)}

def create_break_statement():
    return {"type": "BreakStatement"}