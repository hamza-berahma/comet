import argparse
import sys

from .interpreter import RapcodeError
from .runner import RapcodeRunnerError, run_file

def main():
    """
    The main entry point for the Rapcode interpreter.
    Sets up argument parsing and the ANTLR pipeline.
    """
    parser = argparse.ArgumentParser(description="A robust interpreter for the Rapcode language.")
    parser.add_argument("file", help="The .rapcode file to execute.")
    args = parser.parse_args()

    try:
        run_file(args.file)
    except RapcodeRunnerError as e:
        print(f"[File Error] {e}", file=sys.stderr)
        sys.exit(1)
    except RapcodeError as e:
        # Catch our custom, clean runtime errors and print them.
        print(str(e), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors during interpretation.
        print(f"[Interpreter Crash] An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()

