# File: raptor_converter/generation/graphviz_generator.py
"""
GraphvizGenerator
Generates Graphviz (.dot) text from an AST.
"""
from .base_generator import AstVisualizer

class GraphvizGenerator(AstVisualizer):

    def generate(self, ast):
        self.dot_code = "digraph Flowchart {\n"
        self.dot_code += '  graph [splines=ortho];\n'
        self.dot_code += '  node [fontname="Helvetica", fontsize=10, style="rounded,filled", fillcolor=white];\n'
        self.dot_code += '  edge [fontname="Helvetica", fontsize=9];\n\n'
        
        start_node = self._add_node("Start", shape=self._get_start_shape())
        
        entry, last_node = self._generate_from_nodes(ast["body"])
        
        if entry:
            self._add_edge(start_node, entry)
            
        last_node = last_node or start_node # Handle empty flowchart
        
        end_node = self._add_node("End", shape=self._get_start_shape())
        if last_node: # Only add edge if there was a real exit
            self._add_edge(last_node, end_node)
            
        self.dot_code += "}\n"
        return self.dot_code
        
    # --- Overridden methods ---
    
    def _get_start_shape(self): return "ellipse"
    def _get_process_shape(self): return "box"
    def _get_io_shape(self): return "parallelogram"
    def _get_decision_shape(self): return "diamond"
    def _get_merge_shape(self): return "point"

    def _add_node(self, label, shape, **kwargs):
        node_id = f"node{self.node_count}"
        self.node_count += 1
        
        # Escape for DOT format
        safe_label = label.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        
        attrs = [f'label="{safe_label}"', f'shape={shape}']
        
        if shape == "point":
            attrs.extend(['width="0.1"', 'height="0.1"', 'label=""'])
        if shape == "ellipse":
             attrs.append('fillcolor="#f8f8f8"')
        if shape == "diamond":
             attrs.append('fillcolor="#f0f8ff"')

        self.dot_code += f'  {node_id} [{", ".join(attrs)}];\n'
        return node_id
        
    def _add_edge(self, from_node, to_node, label=None):
        if not from_node or not to_node:
            return
        attrs = [f'xlabel="{label}"'] if label else []
        self.dot_code += f'  {from_node} -> {to_node} [{", ".join(attrs)}];\n'