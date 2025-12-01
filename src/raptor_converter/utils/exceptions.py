"""
Custom exceptions for the application.
"""

class RaptorConverterError(Exception):
    """Base exception for all application-specific errors."""
    pass

class ParsingError(RaptorConverterError):
    """Exception raised for errors during parsing (lexing, syntax)."""
    pass

class GenerationError(RaptorConverterError):
    """Exception raised for errors during code/diagram generation."""
    pass