# File: raptor_converter/__main__.py
"""
Main entry point for the raptor_converter package.
This allows the package to be run as a script:
  python -m raptor_converter input.rap --to mermaid
"""
from .cli import main

if __name__ == "__main__":
    main()