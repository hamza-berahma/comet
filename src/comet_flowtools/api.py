"""
Public API helpers that orchestrate the converter and interpreter subsystems.
"""
from __future__ import annotations

from pathlib import Path
from typing import Callable, IO, Optional, Tuple, Union

from raptor_converter.generation.rapcode_generator import RapcodeGenerator
from raptor_converter.parsing.rapcode_parser import RapcodeParser as FlowRapcodeParser
from raptor_converter.parsing.raptor_xml_parser import RaptorXMLParser
from rapcode_interpreter.runner import (
    RapcodeRunnerError,
    run_file as _run_rapcode_file,
    run_source as _run_rapcode_source,
)

TextSource = Union[str, Path, IO[str]]
OutputCallback = Callable[[object], None]
InputCallback = Callable[[str], str]


def parse_raptor_file(path_or_text: TextSource) -> dict:
    """
    Parse a Raptor (.rap XML) flowchart into an AST dictionary.

    If *path_or_text* is a path-like object pointing to an existing file, the file
    is read from disk. Otherwise it's treated as raw XML text.
    """
    parser = RaptorXMLParser()
    content = _read_text(path_or_text, prefer_file=True)
    return parser.parse(content)


def parse_rapcode(source: TextSource) -> dict:
    """
    Parse Rapcode source code into the canonical AST structure.

    Accepts either a filesystem path or an in-memory string/stream.
    """
    parser = FlowRapcodeParser()
    content = _read_text(source, prefer_file=True)
    return parser.parse(content)


def ast_to_rapcode(ast_dict: dict) -> str:
    """
    Generate Rapcode text from an AST created by the parser helpers.
    """
    generator = RapcodeGenerator()
    return generator.generate(ast_dict)


def convert_raptor_to_rapcode(
    input_path: Union[str, Path],
    output_path: Optional[Union[str, Path]] = None,
) -> Tuple[str, Optional[Path]]:
    """
    Convenience helper that loads a .rap file, converts it to Rapcode,
    and optionally writes the result to *output_path*.

    Returns a tuple of (rapcode_text, output_path_written).
    """
    input_path = Path(input_path)
    rapcode_text = ast_to_rapcode(parse_raptor_file(input_path))

    destination: Optional[Path] = None
    if output_path is not None:
        destination = Path(output_path)
        destination.write_text(rapcode_text, encoding="utf-8")

    return rapcode_text, destination


def run_rapcode(
    source: TextSource,
    *,
    source_is_path: Optional[bool] = None,
    input_callback: Optional[InputCallback] = None,
    output_callback: Optional[OutputCallback] = None,
) -> dict:
    """
    Execute Rapcode from a path or raw string and return the interpreter memory.

    Parameters
    ----------
    source:
        A path to a .rapcode file or a string / IO handle containing Rapcode.
    source_is_path:
        Force treating *source* as a file path (True) or as raw code (False).
        When left as None (default) the helper auto-detects based on filesystem
        existence checks.
    input_callback/output_callback:
        Optional callables injected into the interpreter so tests can stub I/O.
    """
    run_kwargs = {
        "input_func": input_callback,
        "output_func": output_callback,
    }

    if source_is_path is True:
        interpreter = _run_rapcode_file(source, **run_kwargs)
    elif source_is_path is False:
        code = _read_text(source, prefer_file=False)
        interpreter = _run_rapcode_source(code, **run_kwargs)
    else:
        if _looks_like_existing_path(source):
            interpreter = _run_rapcode_file(source, **run_kwargs)
        else:
            code = _read_text(source, prefer_file=False)
            interpreter = _run_rapcode_source(code, **run_kwargs)

    return dict(interpreter.memory)


__all__ = [
    "parse_raptor_file",
    "parse_rapcode",
    "ast_to_rapcode",
    "convert_raptor_to_rapcode",
    "run_rapcode",
    "RapcodeRunnerError",
]


def _read_text(source: TextSource, *, prefer_file: bool) -> str:
    """
    Normalize the supported *TextSource* inputs into a unicode string.
    """
    if hasattr(source, "read"):
        return source.read()

    if isinstance(source, Path):
        return source.read_text(encoding="utf-8")

    source_str = str(source)
    if prefer_file and _looks_like_existing_path(source_str):
        return Path(source_str).read_text(encoding="utf-8")

    return source_str


def _looks_like_existing_path(value: TextSource) -> bool:
    if isinstance(value, Path):
        return value.exists()
    if isinstance(value, str):
        try:
            path = Path(value)
        except OSError:
            return False
        return path.exists()
    return False

