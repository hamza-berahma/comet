"""
Abstract Base Class for all parsers.
"""
from abc import ABC, abstractmethod

class BaseParser(ABC):
    """
    Defines the interface for a parser.
    It must take a string content and return an AST.
    """
    
    @abstractmethod
    def parse(self, content: str) -> dict:
        """
        Parses the input string content into an Abstract Syntax Tree (AST).
        
        Args:
            content: The string content of the file.
            
        Returns:
            A dictionary representing the root of the AST.
            
        Raises:
            ParsingError: If any syntax or structural error occurs.
        """
        pass