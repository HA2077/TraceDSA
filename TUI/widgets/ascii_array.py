from textual.widget import Widget
from textual.widgets import Static

class ASCIIArray(Widget):
    def __init__(self, data=None, title="Array"):
        super().__init__()
        self.data = data or []
        self.title = title

    def compose(self):
        self._static = Static("")
        yield self._static

    def update_data(self, data):
        self.data = data or []
        self._refresh_display()

    def _refresh_display(self):
        self._static.update(self._render())

    def _render(self):
        if not self.data:
            return f"{self.title}: [empty]"

        if "Stack" in self.title:
            return self._render_stack()
        elif "Queue" in self.title or "queue" in self.title.lower():
            return self._render_queue()
        elif "Doubly" in self.title or "DLL" in self.title:
            return self._render_doubly_linked()
        elif "Linked" in self.title or "LL" in self.title:
            return self._render_singly_linked()
        else:
            return self._render_array()

    # The following methods generate ASCII art for different data structures
    def _render_stack(self):
        lines = [f"{self.title}", ""]
        lines.append("  top")
        lines.append("   │")
        for i, item in enumerate(self.data):
                lines.append(f" ┌─────┐")
                lines.append(f" │{self._pad(item)}│")
                lines.append(f" └─────┘")
                lines.append(f"   │")
        lines.append("   │")
        lines.append(" bottom")
        return "\n".join(lines)

    def _render_queue(self):
        if not self.data:
            return f"{self.title}: [empty]"

        cells = []
        for item in self.data:
            cells.append(f"│ {self._pad(item)} │")

        top = "front" + "─" * (len(cells) * 7 - 5) + "rear"
        box_top = "  ┌" + "─────┬" * (len(cells) - 1) + "─────┐"
        box_mid = "  " + "  ".join(cells)
        box_bot = "  └" + "─────┴" * (len(cells) - 1) + "─────┘"

        return f"{self.title}\n\n{top}\n{box_top}\n{box_mid}\n{box_bot}"

    def _render_singly_linked(self):
        if not self.data:
            return f"{self.title}: [empty]"

        nodes = []
        for item in self.data:
            nodes.append(f"┌─────┐")
            nodes.append(f"│ {self._pad(item)} │──→")
            nodes.append(f"└─────┘")

        lines = [f"{self.title}", ""]
        for i in range(0, len(nodes), 3):
            lines.append("  " + "  ".join(nodes[i:i+3]))

        lines.append("       " * (len(self.data) - 1) + "  NULL")
        return "\n".join(lines)

    def _render_doubly_linked(self):
        if not self.data:
            return f"{self.title}: [empty]"

        nodes = []
        for item in self.data:
            nodes.append(f"┌─────┐")
            nodes.append(f"│ {self._pad(item)} │")
            nodes.append(f"└─────┘")

        lines = [f"{self.title}", ""]
        for i in range(0, len(nodes), 3):
            lines.append("  " + "  ".join(nodes[i:i+3]))

        connector = "  "
        for i in range(len(self.data)):
            if i == 0:
                connector += "  ↔  "
            else:
                connector += "  ↔  "
        lines.append(connector)
        lines.append("  NULL" + "      " * (len(self.data) - 1) + "  NULL")
        return "\n".join(lines)

    def _render_array(self):
        cells = []
        for item in self.data:
            cells.append(f"│ {self._pad(item)} │")

        top = "  ┌" + "─────┬" * (len(cells) - 1) + "─────┐"
        mid = "  " + "  ".join(cells)
        bot = "  └" + "─────┴" * (len(cells) - 1) + "─────┘"

        indices = "  "
        for i in range(len(self.data)):
            indices += f"  {i}  "

        return f"{self.title}\n\n{top}\n{mid}\n{bot}\n{indices}"

    def _pad(self, val):
        s = str(val)
        if len(s) > 5:
            return s[:5]
        return s.center(5)