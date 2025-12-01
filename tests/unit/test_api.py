import json
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from comet_flowtools import (
    ast_to_rapcode,
    convert_raptor_to_rapcode,
    parse_rapcode,
    parse_raptor_file,
    run_rapcode,
)
from rapcode_interpreter.runner import RapcodeRunnerError
from raptor_converter.utils.exceptions import ParsingError

FIXTURES_DIR = PROJECT_ROOT / "tests" / "fixtures"
AREA_FIXTURE = FIXTURES_DIR / "area.rap"


class TestCometFlowtoolsAPI(unittest.TestCase):
    def setUp(self):
        self.area_xml = AREA_FIXTURE.read_text(encoding="utf-8")

    # --- parse_raptor_file ---
    def test_parse_raptor_file_from_path(self):
        ast = parse_raptor_file(AREA_FIXTURE)
        self.assertEqual(ast["type"], "Program")
        self.assertGreater(len(ast["body"]), 0)

    def test_parse_raptor_file_accepts_raw_xml_string(self):
        ast = parse_raptor_file(self.area_xml)
        self.assertEqual(ast["type"], "Program")

    def test_parse_raptor_file_raises_for_missing_start(self):
        bad_xml = "<MainWindowViewModel.Raptor_File></MainWindowViewModel.Raptor_File>"
        with self.assertRaises(ParsingError):
            parse_raptor_file(bad_xml)

    # --- parse_rapcode ---
    def test_parse_rapcode_handles_newlines_and_assignments(self):
        rapcode = textwrap.dedent(
            """
            radius := 2
            area := (3.14 * radius * radius)
            OUTPUT ("Area=" + area)
            """
        )
        ast = parse_rapcode(rapcode)
        self.assertEqual(ast["type"], "Program")
        self.assertEqual(len(ast["body"]), 3)

    # --- ast_to_rapcode / convert helper ---
    def test_convert_raptor_to_rapcode_writes_destination(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            destination = Path(tmpdir) / "area.rapcode"
            rapcode_text, written = convert_raptor_to_rapcode(AREA_FIXTURE, destination)
            self.assertEqual(written, destination)
            self.assertTrue(destination.exists())
            self.assertIn("OUTPUT", rapcode_text)
            self.assertGreater(destination.stat().st_size, 0)

    # --- run_rapcode ---
    def test_run_rapcode_from_string_with_callbacks(self):
        rapcode = textwrap.dedent(
            """
            value := INPUT("Number?")
            OUTPUT value
            """
        )
        outputs = []
        inputs = iter(["5"])
        memory = run_rapcode(
            rapcode,
            source_is_path=False,
            input_callback=lambda prompt: next(inputs),
            output_callback=outputs.append,
        )
        self.assertEqual(outputs, [5])  # interpreter auto-converts numeric strings
        self.assertEqual(memory["value"], 5)

    def test_run_rapcode_detects_path_automatically(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            script = Path(tmpdir) / "echo.rapcode"
            script.write_text('OUTPUT "ok"\n', encoding="utf-8")
            outputs = []
            memory = run_rapcode(script, output_callback=outputs.append)
            self.assertEqual(outputs, ["ok"])
            self.assertEqual(memory, {})

    def test_run_rapcode_missing_file_raises_runner_error(self):
        with self.assertRaises(RapcodeRunnerError):
            run_rapcode(Path("does_not_exist.rapcode"), source_is_path=True)

    # --- round-trip integration ---
    def test_round_trip_between_raptor_and_rapcode(self):
        ast = parse_raptor_file(AREA_FIXTURE)
        rapcode_text = ast_to_rapcode(ast)
        rapcode_ast = parse_rapcode(rapcode_text)
        self.assertEqual(rapcode_ast["type"], "Program")
        self.assertGreater(len(rapcode_ast["body"]), 0)

    def test_parse_raptor_then_run_generated_rapcode(self):
        ast = parse_raptor_file(AREA_FIXTURE)
        rapcode_text = ast_to_rapcode(ast)
        outputs = []
        inputs = iter(["2"])
        run_rapcode(
            rapcode_text,
            source_is_path=False,
            input_callback=lambda prompt: next(inputs),
            output_callback=outputs.append,
        )
        self.assertTrue(outputs)  # Should print at least once


if __name__ == "__main__":
    unittest.main()

