from textual.widget import Widget


class ASCIIHeap(Widget):
    def __init__(self, heap_data=None, title="Heap", heap_type="min"):
        super().__init__()
        self.heap_data = heap_data or []
        self.title = title
        self.heap_type = heap_type  # "min" or "max"
        
    def update_heap(self, heap_data):
        self.heap_data = heap_data or []
        self.refresh()
        
    def render(self):
        if not self.heap_data:
            return f"{self.title} ({self.heap_type}-heap): []"
            
        # Display as array representation with boxes
        array_str = " ".join([f"[{x}]" for x in self.heap_data])
        return f"{self.title} ({self.heap_type}-heap): {array_str}"
        
        # Optional: Could also render as tree structure
        # return self._render_as_tree()
        
    def _render_as_tree(self):
        """Render heap as tree structure (for future enhancement)"""
        if not self.heap_data:
            return f"{self.title}: Empty Heap"
            
        # Simple level-by-level representation
        result = f"{self.title} ({self.heap_type}-heap):\n"
        level = 0
        index = 0
        n = len(self.heap_data)
        
        while index < n:
            level_start = index
            level_end = min(index + (2 ** level), n)
            level_values = self.heap_data[level_start:level_end]
            
            # Calculate spacing for tree-like appearance
            spacing = "  " * (2 - level) if level < 2 else ""
            result += spacing + " ".join([f"[{v}]" for v in level_values]) + "\n"
            
            index = level_end
            level += 1
            
        return result