
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from raptor_converter.generation.expression_utils import expression_to_string
from raptor_converter.parsing.expression_parser import ExpressionParser
from raptor_converter.utils.exceptions import ParsingError


class TestExpressionParser(unittest.TestCase):
    def _parse_and_assert(self, tokens, expected_type, expected_str):
        """Helper to parse tokens and assert the resulting AST node's shape."""
        ast = ExpressionParser(tokens).parse()
        self.assertIsNotNone(ast, f"Parser returned None for tokens: {tokens}")
        self.assertEqual(ast.get("type"), expected_type, f"Unexpected node type for {tokens}")
        self.assertEqual(expression_to_string(ast), expected_str)

    def test_simple_addition(self):
        self._parse_and_assert(["1", "+", "2"], "BinaryExpression", "(1 + 2)")

    def test_precedence(self):
        self._parse_and_assert(["1", "+", "2", "*", "3"], "BinaryExpression", "(1 + (2 * 3))")

    def test_parentheses(self):
        self._parse_and_assert(["(", "1", "+", "2", ")", "*", "3"], "BinaryExpression", "((1 + 2) * 3)")

    def test_unary_negation(self):
        self._parse_and_assert(["-", "5"], "UnaryExpression", "(-5)")

    def test_unary_not(self):
        self._parse_and_assert(["NOT", "TRUE"], "UnaryExpression", "NOT TRUE")

    def test_logical_and(self):
        self._parse_and_assert(["TRUE", "AND", "FALSE"], "BinaryExpression", "(TRUE AND FALSE)")

    def test_logical_or(self):
        self._parse_and_assert(["TRUE", "OR", "FALSE"], "BinaryExpression", "(TRUE OR FALSE)")

    def test_logical_precedence(self):
        self._parse_and_assert(["FALSE", "OR", "TRUE", "AND", "TRUE"], "BinaryExpression", "(FALSE OR (TRUE AND TRUE))")

    def test_comparison(self):
        self._parse_and_assert(["x", ">", "5"], "BinaryExpression", "(x > 5)")
        self._parse_and_assert(["y", "<=", "10"], "BinaryExpression", "(y <= 10)")

    def test_string_literal(self):
        self._parse_and_assert(['"hello"'], "Literal", '"hello"')

    def test_number_literals(self):
        self._parse_and_assert(["123"], "Literal", "123")
        self._parse_and_assert(["3.14"], "Literal", "3.14")

    def test_boolean_literals(self):
        self._parse_and_assert(["TRUE"], "Literal", "TRUE")
        self._parse_and_assert(["FALSE"], "Literal", "FALSE")

    def test_identifier(self):
        self._parse_and_assert(["my_var"], "Identifier", "my_var")

    def test_input_expression(self):
        self._parse_and_assert(["INPUT", "(", '"Enter a value"', ")"], "CallExpression", 'INPUT("Enter a value")')

    def test_complex_expression(self):
        tokens = [
            "(", "a", "+", "b", ")", "*", "(", "c", "-", "5", ")",
            ">=", "10", "AND", "NOT", "(", "d", "OR", "e", ")"
        ]
        expected = "((((a + b) * (c - 5)) >= 10) AND NOT (d OR e))"
        self._parse_and_assert(tokens, "BinaryExpression", expected)

    def test_empty_input(self):
        self.assertIsNone(ExpressionParser([]).parse())

    def test_invalid_token(self):
        with self.assertRaises(ParsingError):
            ExpressionParser(["1", "PLUS", "2"]).parse()

    def test_incomplete_expression(self):
        with self.assertRaises(ParsingError):
            ExpressionParser(["1", "+"]).parse()

    def test_mismatched_parentheses(self):
        with self.assertRaises(ParsingError):
            ExpressionParser(["(", "1", "+", "2"]).parse()


if __name__ == '__main__':
    unittest.main()
