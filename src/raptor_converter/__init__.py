"""
raptor_converter package initializer.

Exposes the CLI entry point via ``raptor_converter.main`` so callers can run
``python -m raptor_converter`` or import ``main`` directly.
"""

from comet_flowtools._version import __version__


def main():
    from .cli import main as _cli_main

    return _cli_main()


__all__ = ["main", "__version__"]

