# File: raptor_converter/cli.py
"""
Command-Line Interface (CLI) for the Raptor Converter.
This file orchestrates the parsing and generation process.
"""

import argparse
import os
import sys
from pathlib import Path

from comet_flowtools import ast_to_rapcode, parse_rapcode, parse_raptor_file

from .generation.graphviz_generator import GraphvizGenerator
from .generation.mermaid_generator import MermaidGenerator
from .utils.exceptions import RaptorConverterError

def main():
    """Main function to run the flowchart conversion tool."""
    parser = argparse.ArgumentParser(
        description="A tool to convert between Raptor flowcharts, .rapcode, and visual formats.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # --- Arguments ---
    parser.add_argument("input_file", help="Path to the input file (.rap or .rapcode).")
    parser.add_argument(
        "--to",
        dest="output_format",
        required=True,
        choices=["rapcode", "mermaid", "dot"],
        help="The desired output format."
    )
    parser.add_argument(
        "-o", "--output",
        dest="output_file",
        help="Path to the output file. If not provided, it will be generated based on the input file name."
    )

    args = parser.parse_args()

    # Map output formats to their generator classes
    GENERATOR_MAP = {
        "mermaid": MermaidGenerator,
        "dot": GraphvizGenerator
    }

    try:
        # --- 1. Parse input into AST ---
        input_path = Path(args.input_file)
        if not input_path.exists():
            print(f"Error: Input file not found: {input_path}", file=sys.stderr)
            sys.exit(1)

        _, ext = os.path.splitext(input_path.name)
        if ext == ".rap":
            ast = parse_raptor_file(input_path)
        elif ext == ".rapcode":
            ast = parse_rapcode(input_path)
        else:
            print(f"Error: Unknown input file type for '{args.input_file}'. Please use .rap or .rapcode.", file=sys.stderr)
            sys.exit(1)

        # --- 3. Get Generator ---
        if args.output_format == "rapcode":
            output_content = ast_to_rapcode(ast)
        else:
            generator_class = GENERATOR_MAP.get(args.output_format)
            if not generator_class:
                print(f"Error: Unknown output format '{args.output_format}'.", file=sys.stderr)
                sys.exit(1)
            generator = generator_class()
            output_content = generator.generate(ast)
    
    except RaptorConverterError as e:
        # Catch our application-specific errors (ParsingError, GenerationError)
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected internal error occurred: {e}", file=sys.stderr)
        # You might want to print a full traceback here for debugging
        # import traceback
        # traceback.print_exc()
        sys.exit(1)

    # --- 4. Determine output file path and save ---
    if args.output_file:
        output_path = args.output_file
    else:
        base_name = os.path.splitext(args.input_file)[0]
        ext_map = {"mermaid": "mmd", "dot": "dot", "rapcode": "rapcode"}
        extension = ext_map.get(args.output_format)
        output_path = f"{base_name}_converted.{extension}"

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output_content)
        print(f"✅ Successfully converted '{args.input_file}' to '{output_path}'.")
    except IOError as e:
        print(f"Error writing to output file: {e}", file=sys.stderr)
        sys.exit(1)
        
if __name__ == '__main__':
    main()