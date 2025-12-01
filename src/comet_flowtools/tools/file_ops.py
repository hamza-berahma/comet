"""
File-based helpers that mirror the one-off scripts that previously lived under
`python/`. These functions lean on the canonical converters so they stay in sync
with the rest of the library.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional, Tuple, Union

from comet_flowtools import ast_to_rapcode, parse_rapcode, parse_raptor_file
from raptor_converter.generation.graphviz_generator import GraphvizGenerator
from raptor_converter.generation.mermaid_generator import MermaidGenerator

PathLike = Union[str, Path]
TextAndPath = Tuple[str, Path]


def export_raptor_ast(
    input_path: PathLike,
    output_path: Optional[PathLike] = None,
) -> TextAndPath:
    """
    Convert a `.rap` XML file into a JSON AST on disk.
    """
    ast_dict = parse_raptor_file(input_path)
    serialized = json.dumps(ast_dict, indent=2)
    destination = _resolve_destination(input_path, output_path, ".json")
    destination.write_text(serialized, encoding="utf-8")
    return serialized, destination


def ast_json_to_rapcode(
    input_path: PathLike,
    output_path: Optional[PathLike] = None,
) -> TextAndPath:
    """
    Convert a JSON AST (as produced by `export_raptor_ast`) into `.rapcode`.
    """
    source = Path(input_path)
    ast_dict = json.loads(source.read_text(encoding="utf-8"))
    rapcode_text = ast_to_rapcode(ast_dict)
    destination = _resolve_destination(source, output_path, ".rapcode")
    destination.write_text(rapcode_text, encoding="utf-8")
    return rapcode_text, destination


def rapcode_to_mermaid(
    input_path: PathLike,
    output_path: Optional[PathLike] = None,
) -> TextAndPath:
    """
    Generate a Mermaid flowchart from a `.rapcode` program.
    """
    ast_dict = parse_rapcode(input_path)
    generator = MermaidGenerator()
    mermaid_diagram = generator.generate(ast_dict)
    destination = _resolve_destination(input_path, output_path, ".mmd")
    destination.write_text(mermaid_diagram, encoding="utf-8")
    return mermaid_diagram, destination


def rapcode_to_graphviz(
    input_path: PathLike,
    output_path: Optional[PathLike] = None,
) -> TextAndPath:
    """
    Generate a Graphviz DOT diagram from a `.rapcode` program.
    """
    ast_dict = parse_rapcode(input_path)
    generator = GraphvizGenerator()
    dot_diagram = generator.generate(ast_dict)
    destination = _resolve_destination(input_path, output_path, ".dot")
    destination.write_text(dot_diagram, encoding="utf-8")
    return dot_diagram, destination


def _resolve_destination(
    src: PathLike,
    provided: Optional[PathLike],
    default_ext: str,
) -> Path:
    if provided:
        return Path(provided)
    src_path = Path(src)
    return src_path.with_suffix(default_ext)

