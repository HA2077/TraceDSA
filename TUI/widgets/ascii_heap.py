from textual.widgets import Static


class ASCIIHeap(Static):
    def __init__(self, heap_data=None, title="Heap", heap_type="min"):
        super().__init__("")
        self.heap_data = heap_data or []
        self.title = title
        self.heap_type = heap_type
        self.view_mode = "tree"

    def update_heap(self, heap_data):
        self.heap_data = heap_data or []
        self.update(self._render())

    def toggle_view(self):
        self.view_mode = "array" if self.view_mode == "tree" else "tree"
        self.update(self._render())

    def view_mode_label(self):
        return "(tree view)" if self.view_mode == "tree" else "(array view)"

    def _render(self):
        if not self.heap_data:
            return f"{self.title} ({self.heap_type}-heap)\n\n  ┌─────────┐\n  │ [empty] │\n  └─────────┘"

        if self.view_mode == "tree":
            return self._render_as_tree()
        return self._render_as_array()

    def _render_as_array(self):
        padded = [self._pad(item) for item in self.heap_data]

        top = "  ┌" + "─────┬" * (len(padded) - 1) + "─────┐"
        mid = "  │" + "│".join(padded) + "│"
        bot = "  └" + "─────┴" * (len(padded) - 1) + "─────┘"

        indices = "   "
        for i in range(len(self.heap_data)):
            indices += str(i).center(5) + " "

        return f"{self.title} ({self.heap_type}-heap) {self.view_mode_label()}\n\n{top}\n{mid}\n{bot}\n{indices}"

    def _render_as_tree(self):
        lines = [f"{self.title} ({self.heap_type}-heap) {self.view_mode_label()}", ""]
        self._draw_heap_tree(0, "", True, lines)
        return "\n".join(lines)

    def _draw_heap_tree(self, index, prefix, is_last, lines):
        if index >= len(self.heap_data):
            return

        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}[{self.heap_data[index]}]")

        new_prefix = prefix + ("    " if is_last else "│   ")

        left = 2 * index + 1
        right = 2 * index + 2

        has_left = left < len(self.heap_data)
        has_right = right < len(self.heap_data)

        if has_left:
            self._draw_heap_tree(left, new_prefix, not has_right, lines)
        if has_right:
            self._draw_heap_tree(right, new_prefix, True, lines)

    def _pad(self, val):
        s = str(val)
        if len(s) > 5:
            return s[:5]
        return s.center(5)
