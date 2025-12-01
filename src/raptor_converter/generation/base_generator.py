# File: raptor_converter/generation/base_generator.py
"""
Base classes for all AST-to-output generators.
Contains the AstVisualizer base class, which provides shared logic
for both Mermaid and Graphviz generators.
"""
from abc import ABC, abstractmethod
from ..utils.exceptions import GenerationError
from .expression_utils import expression_to_string

class BaseGenerator(ABC):
    """Abstract interface for a generator."""
    @abstractmethod
    def generate(self, ast: dict) -> str:
        """
        Generates an output string from an AST.
        
        Args:
            ast: The Abstract Syntax Tree.
            
        Returns:
            The generated output as a string.
            
        Raises:
            GenerationError: If generation fails.
        """
        pass

class AstVisualizer(BaseGenerator):
    """
    Base class for visual generators (Mermaid, Graphviz).
    Handles the common AST traversal logic.
    """
    def __init__(self):
        self.node_count = 0
        self.loop_exit_stack = []

    # --- Abstract methods to be implemented by subclasses ---
    
    @abstractmethod
    def _add_node(self, label, shape, **kwargs):
        """Subclass implements this to create a node. Must return a unique node ID."""
        pass
        
    @abstractmethod
    def _add_edge(self, from_node_id, to_node_id, label=None):
        """Subclass implements this to create an edge."""
        pass

    def _get_start_shape(self): return "ellipse"
    def _get_process_shape(self): return "box"
    def _get_io_shape(self): return "parallelogram"
    def _get_decision_shape(self): return "diamond"
    def _get_merge_shape(self): return "point"


    # --- Expression to String (Fixed) ---
    
    def _expr_to_str(self, node):
        """Converts an expression AST node to a string, with parentheses."""
        try:
            return expression_to_string(node)
        except GenerationError:
            return "expr"

    # --- AST Traversal Logic ---

    def _generate_from_nodes(self, nodes):
        """
        Generates a chain of nodes from a list.
        Returns (entry_node_id, exit_node_id) for the chain.
        """
        if not nodes: 
            return None, None
            
        # Generate all nodes in the list
        generated = [self._generate_node(node) for node in nodes]
        
        # Link them sequentially
        for i in range(len(generated) - 1):
            exit_of_current, entry_of_next = generated[i][1], generated[i+1][0]
            if exit_of_current and entry_of_next:
                self._add_edge(exit_of_current, entry_of_next)
                
        # Return the entry of the first node and exit of the last
        first_entry = generated[0][0]
        last_exit = generated[-1][1]
        
        return first_entry, last_exit

    def _generate_node(self, node):
        """
        Generates a single node or subgraph.
        Returns (entry_node_id, exit_node_id) for the node.
        """
        node_type = node["type"]

        if node_type == "AssignmentStatement":
            label = f"{self._expr_to_str(node['left'])} := {self._expr_to_str(node['right'])}"
            n = self._add_node(label, shape=self._get_process_shape())
            return n, n
            
        if node_type == "ExpressionStatement":
            expr = node["expression"]
            if expr.get("callee") == "Output":
                label = f"OUTPUT: {self._expr_to_str(expr['arguments'][0])}"
                n = self._add_node(label, shape=self._get_io_shape())
                return n, n
                
        if node_type == "BreakStatement":
            if not self.loop_exit_stack:
                raise GenerationError("BREAK statement found outside of a loop.")
            break_entry = self._add_node(" ", shape=self._get_merge_shape())
            # Connect the break to the exit of the current loop
            self._add_edge(break_entry, self.loop_exit_stack[-1])
            return break_entry, None # No exit from a break
            
        if node_type == "IfStatement":
            cond_node = self._add_node(self._expr_to_str(node["test"]), shape=self._get_decision_shape())
            merge_node = self._add_node(" ", shape=self._get_merge_shape())
            
            # True branch
            true_entry, true_exit = self._generate_from_nodes(node["consequent"]["body"])
            self._add_edge(cond_node, true_entry or merge_node, label="True")
            if true_exit: self._add_edge(true_exit, merge_node)
            
            # False branch
            alt_body = node["alternate"]["body"] if node["alternate"] else []
            false_entry, false_exit = self._generate_from_nodes(alt_body)
            self._add_edge(cond_node, false_entry or merge_node, label="False")
            if false_exit: self._add_edge(false_exit, merge_node)

            return cond_node, merge_node
            
        if node_type == "WhileStatement":
            # Try to visualize as a Raptor-style mid-test loop first
            raptor_loop_nodes = self._try_visualize_raptor_loop(node)
            if raptor_loop_nodes:
                return raptor_loop_nodes
            
            # Fallback to standard While-loop visualization
            test_expr_str = self._expr_to_str(node["test"])
            cond_node = self._add_node(test_expr_str, shape=self._get_decision_shape())
            exit_node = self._add_node(" ", shape=self._get_merge_shape())
            
            self.loop_exit_stack.append(exit_node)
            
            # Body
            body_entry, body_exit = self._generate_from_nodes(node["body"]["body"])
            self._add_edge(cond_node, body_entry or cond_node, label="True")
            if body_exit: 
                self._add_edge(body_exit, cond_node) # Loop back edge
            
            self.loop_exit_stack.pop()
            
            self._add_edge(cond_node, exit_node, label="False") # Exit loop
            return cond_node, exit_node
            
        # Fallback for unknown nodes
        unknown = self._add_node(f"Unknown Node:\n{node_type}", shape="octagon")
        return unknown, unknown

    def _try_visualize_raptor_loop(self, node):
        """
        FIX: Attempts to find the `While(True) -> If(Break)` pattern
        and visualize it as a proper mid-test loop.
        """
        # Check for While(True)
        test = node["test"]
        if not (test["type"] == "Literal" and test["value"] is True):
            return None # Not a While(True) loop

        # Find the If-Break node
        body = node["body"]["body"]
        if_break_node = None
        if_break_index = -1
        for i, n in enumerate(body):
            if n["type"] == "IfStatement" and \
               n["consequent"]["body"] and \
               n["consequent"]["body"][0]["type"] == "BreakStatement" and \
               n["alternate"] is None:
                if_break_node = n
                if_break_index = i
                break
        
        if if_break_node is None:
            return None # Not a Raptor-style loop
            
        # We found it! Visualize it as a mid-test loop.
        body_before = body[:if_break_index]
        body_after = body[if_break_index + 1:]
        
        exit_condition_str = self._expr_to_str(if_break_node["test"])
        cond_node = self._add_node(exit_condition_str, shape=self._get_decision_shape())
        
        # This is the single exit point for the loop
        exit_node = self._add_node(" ", shape=self._get_merge_shape())
        self.loop_exit_stack.append(exit_node)
        
        # "True" branch (exit condition) goes to the loop exit
        self._add_edge(cond_node, exit_node, label="True") 
        
        # Generate the two parts of the body
        entry_before, exit_before = self._generate_from_nodes(body_before)
        entry_after, exit_after = self._generate_from_nodes(body_after)

        #--- Link everything up ---
        
        # 1. Entry point of the whole loop
        loop_entry = entry_before or cond_node
        
        # 2. Link exit of "before" to condition
        if exit_before:
            self._add_edge(exit_before, cond_node)
            
        # 3. Link "False" branch (continue loop) to "after" body
        continue_path = entry_after or loop_entry # If no "after", loop to start
        self._add_edge(cond_node, continue_path, label="False")
        
        # 4. Link exit of "after" to loop entry
        if exit_after:
            self._add_edge(exit_after, loop_entry)
            
        self.loop_exit_stack.pop()
        return loop_entry, exit_node