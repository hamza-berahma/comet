"""
Command-line entry point for the modernized utility scripts.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from . import (
    ast_json_to_rapcode,
    export_raptor_ast,
    rapcode_to_graphviz,
    rapcode_to_mermaid,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="flowtools",
        description="Utility commands built on top of comet_flowtools.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    export_ast = subparsers.add_parser(
        "export-raptor-ast",
        help="Convert a .rap XML file into a JSON AST.",
    )
    export_ast.add_argument("input", type=Path, help="Path to the .rap file.")
    export_ast.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Destination JSON path (defaults to <input>.json).",
    )

    ast_to_rap = subparsers.add_parser(
        "ast-to-rapcode",
        help="Convert a previously exported JSON AST into Rapcode text.",
    )
    ast_to_rap.add_argument("input", type=Path, help="Path to the JSON AST file.")
    ast_to_rap.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Destination Rapcode path (defaults to <input>.rapcode).",
    )

    mermaid = subparsers.add_parser(
        "rapcode-to-mermaid",
        help="Render a Rapcode program into a Mermaid flowchart.",
    )
    mermaid.add_argument("input", type=Path, help="Path to the .rapcode file.")
    mermaid.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Destination Mermaid file (defaults to <input>.mmd).",
    )

    dot = subparsers.add_parser(
        "rapcode-to-dot",
        help="Render a Rapcode program into a Graphviz DOT diagram.",
    )
    dot.add_argument("input", type=Path, help="Path to the .rapcode file.")
    dot.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Destination DOT file (defaults to <input>.dot).",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "export-raptor-ast":
        _, destination = export_raptor_ast(args.input, args.output)
        print(f"AST saved to {destination}")
        return

    if args.command == "ast-to-rapcode":
        _, destination = ast_json_to_rapcode(args.input, args.output)
        print(f"Rapcode saved to {destination}")
        return

    if args.command == "rapcode-to-mermaid":
        _, destination = rapcode_to_mermaid(args.input, args.output)
        print(f"Mermaid diagram saved to {destination}")
        return

    if args.command == "rapcode-to-dot":
        _, destination = rapcode_to_graphviz(args.input, args.output)
        print(f"DOT diagram saved to {destination}")
        return

    parser.error(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()

