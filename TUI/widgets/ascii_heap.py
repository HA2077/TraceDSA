from textual.widget import Widget
from textual.widgets import Static


class ASCIIHeap(Widget):
    def __init__(self, heap_data=None, title="Heap", heap_type="min"):
        super().__init__()
        self.heap_data = heap_data or []
        self.title = title
        self.heap_type = heap_type
        self.view_mode = "tree"

    def compose(self):
        self._static = Static("")
        yield self._static

    def update_heap(self, heap_data):
        self.heap_data = heap_data or []
        self._refresh_display()

    def toggle_view(self):
        self.view_mode = "array" if self.view_mode == "tree" else "tree"
        self._refresh_display()

    def _refresh_display(self):
        self._static.update(self._render())

    def _render(self):
        if not self.heap_data:
            return f"{self.title} ({self.heap_type}-heap): [empty]"

        if self.view_mode == "tree":
            return self._render_as_tree()
        return self._render_as_array()

    def _render_as_array(self):
        cells = []
        for item in self.heap_data:
            cells.append(f"│ {self._pad(item)} │")

        top = "  ┌" + "─────┬" * (len(cells) - 1) + "─────┐"
        mid = "  " + "  ".join(cells)
        bot = "  └" + "─────┴" * (len(cells) - 1) + "─────┘"

        indices = "  "
        for i in range(len(self.heap_data)):
            indices += f"  {i}  "

        return f"{self.title} ({self.heap_type}-heap)\n\n{top}\n{mid}\n{bot}\n{indices}"

    def _render_as_tree(self):
        if not self.heap_data:
            return f"{self.title}: Empty Heap"

        lines = [f"{self.title} ({self.heap_type}-heap)", ""]
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

        if has_left or has_right:
            if has_left:
                self._draw_heap_tree(left, new_prefix, not has_right, lines)
            if has_right:
                self._draw_heap_tree(right, new_prefix, True, lines)

    def _pad(self, val):
        s = str(val)
        if len(s) > 5:
            return s[:5]
        return s.center(5)