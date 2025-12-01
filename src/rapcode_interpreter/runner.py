"""
Utilities for executing Rapcode programs from files or in-memory strings.
"""
from __future__ import annotations

from pathlib import Path
from typing import Callable, Optional, Union

from antlr4 import CommonTokenStream, FileStream, InputStream

from .generated.RapcodeLexer import RapcodeLexer
from .generated.RapcodeParser import RapcodeParser
from .interpreter import RapcodeInterpreter

PathLike = Union[str, Path]
InputFunc = Callable[[str], str]
OutputFunc = Callable[[object], None]


class RapcodeRunnerError(Exception):
    """Wrapper exception for I/O or pipeline setup issues."""


def run_source(
    source_code: str,
    *,
    input_func: Optional[InputFunc] = None,
    output_func: Optional[OutputFunc] = None,
) -> RapcodeInterpreter:
    """
    Execute Rapcode supplied as a string and return the interpreter instance.
    """
    stream = InputStream(source_code)
    return _execute(stream, input_func, output_func)


def run_file(
    path: PathLike,
    *,
    input_func: Optional[InputFunc] = None,
    output_func: Optional[OutputFunc] = None,
) -> RapcodeInterpreter:
    """
    Execute Rapcode stored on disk and return the interpreter instance.
    """
    try:
        stream = FileStream(str(path), encoding="utf-8")
    except FileNotFoundError as exc:
        raise RapcodeRunnerError(f"The file '{path}' was not found.") from exc
    except OSError as exc:
        raise RapcodeRunnerError(f"Could not open '{path}': {exc}") from exc

    return _execute(stream, input_func, output_func)


def _execute(
    stream,
    input_func: Optional[InputFunc],
    output_func: Optional[OutputFunc],
) -> RapcodeInterpreter:
    lexer = RapcodeLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = RapcodeParser(tokens)
    tree = parser.program()

    interpreter = RapcodeInterpreter(
        input_func=input_func or input,
        output_func=output_func or print,
    )
    interpreter.visit(tree)
    return interpreter


__all__ = ["RapcodeRunnerError", "run_file", "run_source"]

