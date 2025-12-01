import json
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from comet_flowtools.tools import file_ops

FIXTURES_DIR = PROJECT_ROOT / "tests" / "fixtures"


class TestFileOps(unittest.TestCase):
    def test_export_raptor_ast_writes_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            destination = Path(tmpdir) / "area.json"
            text, written = file_ops.export_raptor_ast(FIXTURES_DIR / "area.rap", destination)
            self.assertEqual(written, destination)
            parsed = json.loads(destination.read_text(encoding="utf-8"))
            self.assertEqual(parsed["type"], "Program")
            self.assertEqual(text, destination.read_text(encoding="utf-8"))

    def test_ast_json_to_rapcode_generates_code(self):
        ast_payload = {
            "type": "Program",
            "body": [
                {
                    "type": "ExpressionStatement",
                    "expression": {
                        "type": "CallExpression",
                        "callee": "Output",
                        "arguments": [{"type": "Literal", "value": "Hello"}],
                    },
                }
            ],
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            ast_path = Path(tmpdir) / "flow.json"
            rapcode_path = Path(tmpdir) / "flow.rapcode"
            ast_path.write_text(json.dumps(ast_payload), encoding="utf-8")
            text, written = file_ops.ast_json_to_rapcode(ast_path, rapcode_path)
            self.assertEqual(written, rapcode_path)
            self.assertIn('OUTPUT "Hello"', text)
            self.assertIn('OUTPUT "Hello"', rapcode_path.read_text(encoding="utf-8"))

    def test_rapcode_to_mermaid_uses_default_output(self):
        rapcode = 'OUTPUT "Hello"\n'
        with tempfile.TemporaryDirectory() as tmpdir:
            rap_path = Path(tmpdir) / "hello.rapcode"
            rap_path.write_text(rapcode, encoding="utf-8")
            diagram, written = file_ops.rapcode_to_mermaid(rap_path)
            self.assertTrue(written.name.endswith(".mmd"))
            self.assertIn("graph TD", diagram)
            self.assertIn("OUTPUT", diagram)

    def test_rapcode_to_graphviz_generates_dot(self):
        rapcode = 'OUTPUT "Dot"\n'
        with tempfile.TemporaryDirectory() as tmpdir:
            rap_path = Path(tmpdir) / "dot.rapcode"
            rap_path.write_text(rapcode, encoding="utf-8")
            dot_text, written = file_ops.rapcode_to_graphviz(rap_path)
            self.assertTrue(written.name.endswith(".dot"))
            self.assertIn("digraph", dot_text)
            self.assertIn("OUTPUT", dot_text)


if __name__ == "__main__":
    unittest.main()

