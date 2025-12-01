import sys
import textwrap
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from raptor_converter.parsing.rapcode_parser import RapcodeParser
from raptor_converter.utils.exceptions import ParsingError


class TestRapcodeParser(unittest.TestCase):
    def _parse(self, code: str) -> dict:
        parser = RapcodeParser()
        normalized = textwrap.dedent(code).strip() + "\n"
        return parser.parse(normalized)

    def test_assignment_and_output_with_newlines(self):
        program = self._parse(
            """
            radius := 2

            OUTPUT radius
            """
        )
        body = program["body"]
        self.assertEqual(len(body), 2)
        self.assertEqual(body[0]["type"], "AssignmentStatement")
        self.assertEqual(body[1]["type"], "ExpressionStatement")

    def test_if_else_structure(self):
        program = self._parse(
            """
            IF TRUE THEN
                OUTPUT "yes"
            ELSE
                OUTPUT "no"
            ENDIF
            """
        )
        (if_stmt,) = program["body"]
        self.assertEqual(if_stmt["type"], "IfStatement")
        self.assertEqual(len(if_stmt["consequent"]["body"]), 1)
        self.assertEqual(len(if_stmt["alternate"]["body"]), 1)

    def test_loop_and_break(self):
        program = self._parse(
            """
            LOOP
                BREAK
            ENDLOOP
            """
        )
        (loop_stmt,) = program["body"]
        self.assertEqual(loop_stmt["type"], "WhileStatement")
        self.assertTrue(loop_stmt["test"]["value"])
        self.assertEqual(loop_stmt["body"]["body"][0]["type"], "BreakStatement")

    def test_invalid_statement_raises(self):
        with self.assertRaises(ParsingError):
            self._parse("OUTPUT")

    def test_missing_endif_raises(self):
        with self.assertRaises(ParsingError):
            self._parse(
                """
                IF TRUE THEN
                    OUTPUT "dangling"
                """
            )


if __name__ == "__main__":
    unittest.main()

