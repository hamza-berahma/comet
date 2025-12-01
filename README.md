# Comet Flowtools

Utilities for working with Raptor flowcharts and Rapcode programs.

## Installation

Install from PyPI:

```bash
pip install comet-flowtools
```

Or install from source for development:

```bash
git clone <repository-url>
cd comet
pip install -e .
```

## Repository Layout

- `src/comet_flowtools`: High-level API plus modernized utility helpers (formerly the loose scripts inside `python/`).
- `src/raptor_converter`: Library + CLI for converting `.rap` / `.rapcode` files into Rapcode, Mermaid, or Graphviz outputs.
- `src/rapcode_interpreter`: ANTLR-based interpreter for `.rapcode` programs plus the generated lexer/parser artifacts.
- `tests/fixtures`: Minimal `.rap` inputs that keep the test suite self-contained.
- `tests/unit`: Python unit tests that cover the parser/generator stack and the public API.

The duplicate copy of `raptor_converter` that previously lived inside the interpreter directory has been removed. Both apps now share the same canonical package under `src/`.

## Usage

After installation (from PyPI or source), the following command-line tools are available:

- `raptor-convert path/to/flowchart.rap --to mermaid`
- `rapcode-run path/to/program.rapcode`
- `flowtools export-raptor-ast path/to/flowchart.rap -o flowchart.json`

You can also run individual modules directly:

```bash
python -m raptor_converter input.rap --to mermaid
python -m rapcode_interpreter program.rapcode
```

Or use the unified `flowtools` command with subcommands.

## Python API

Installing the project also exposes a `comet_flowtools` package that unifies
the converter and interpreter capabilities behind a single import surface:

```python
from comet_flowtools import (
    parse_raptor_file,
    parse_rapcode,
    ast_to_rapcode,
    convert_raptor_to_rapcode,
    run_rapcode,
)

# Parse a .rap XML file into the canonical AST structure.
# Note: Use absolute paths or paths relative to your working directory
program_ast = parse_raptor_file("path/to/flowchart.rap")

# Convert that AST into Rapcode text (and optionally write it to disk).
rapcode_text, _ = convert_raptor_to_rapcode(
    "path/to/flowchart.rap",
    "output.rapcode",
)

# You can also round-trip an existing .rapcode file or text snippet.
rapcode_ast = parse_rapcode(rapcode_text)

# Execute Rapcode from a string or path and capture its output.
captured = []
run_rapcode('OUTPUT "Hello!"', output_callback=captured.append, source_is_path=False)
assert captured == ["Hello!"]
```

Every helper returns plain dictionaries or strings so you can integrate the
library into other tooling or educational workflows.

## Running Tests

```bash
python -m unittest discover -s tests -t .
```

