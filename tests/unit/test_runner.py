import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from rapcode_interpreter.runner import RapcodeRunnerError, run_file, run_source


class TestRapcodeRunner(unittest.TestCase):
    def test_run_source_uses_injected_callbacks(self):
        code = textwrap.dedent(
            """
            counter := INPUT(">")
            OUTPUT counter
            """
        )
        outputs = []
        inputs = iter(["4"])
        interpreter = run_source(
            code,
            input_func=lambda prompt: next(inputs),
            output_func=outputs.append,
        )
        self.assertEqual(outputs, [4])
        self.assertEqual(interpreter.memory["counter"], 4)

    def test_run_file_executes_disk_program(self):
        code = 'OUTPUT "runner"\n'
        with tempfile.TemporaryDirectory() as tmpdir:
            script = Path(tmpdir) / "runner.rapcode"
            script.write_text(code, encoding="utf-8")
            outputs = []
            interpreter = run_file(script, output_func=outputs.append)
            self.assertEqual(outputs, ["runner"])
            self.assertEqual(interpreter.memory, {})

    def test_run_file_missing_raises_runner_error(self):
        with self.assertRaises(RapcodeRunnerError):
            run_file(Path("missing_runner_file.rapcode"))

    def test_run_source_handles_loop_and_break(self):
        code = textwrap.dedent(
            """
            LOOP
                OUTPUT "tick"
                BREAK
            ENDLOOP
            """
        )
        outputs = []
        interpreter = run_source(code, output_func=outputs.append)
        self.assertEqual(outputs, ["tick"])
        self.assertEqual(interpreter.memory, {})


if __name__ == "__main__":
    unittest.main()

