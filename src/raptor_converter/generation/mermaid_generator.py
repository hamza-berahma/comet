# File: raptor_converter/generation/mermaid_generator.py
"""
MermaidGenerator
Generates Mermaid flowchart text from an AST.
"""
from .base_generator import AstVisualizer

class MermaidGenerator(AstVisualizer):
    
    def generate(self, ast):
        self.node_defs = []
        self.edge_defs = []
        
        start_node = self._add_node("Start", shape=self._get_start_shape())
        
        entry, last_node = self._generate_from_nodes(ast["body"])
        
        if entry:
            self._add_edge(start_node, entry)
            
        last_node = last_node or start_node # Handle empty flowchart
        
        end_node = self._add_node("End", shape=self._get_start_shape())
        if last_node: # Only add edge if there was a real exit
            self._add_edge(last_node, end_node)
            
        return "graph TD;\n" + "\n".join(self.node_defs) + "\n\n" + "\n".join(self.edge_defs)

    # --- Overridden methods ---

    def _get_start_shape(self): return "start"
    def _get_process_shape(self): return "box"
    def _get_io_shape(self): return "parallelogram"
    def _get_decision_shape(self): return "diamond"
    def _get_merge_shape(self): return "point"

    def _add_node(self, label, shape, **kwargs):
        node_id = f"N{self.node_count}"
        self.node_count += 1
        
        # Mermaid labels must be in quotes, and quotes inside must be escaped
        safe_label = label.replace('"', '#quot;')
        
        shapes = {
            "box": ('["', '"]'), 
            "parallelogram": ('[/"', '/"]'), 
            "diamond": ('{"', '"}'), 
            "point": ('(("', '"))'), 
            "start": ('("', '")'),
            "ellipse": ('("', '")') # Fallback for base class
        }
        shape_open, shape_close = shapes[shape]
        
        self.node_defs.append(f'  {node_id}{shape_open}{safe_label}{shape_close}')
        return node_id

    def _add_edge(self, from_node, to_node, label=None):
        if not from_node or not to_node:
            return
        arrow = f'--"{label}"-->' if label else '-->'
        self.edge_defs.append(f'  {from_node} {arrow} {to_node}')