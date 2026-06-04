from textual.widgets import Static


class ASCIIArray(Static):
    def __init__(self, data=None, title="Array"):
        super().__init__("")
        self.data = data or []
        self.title = title

    def update_data(self, data):
        self.data = data or []
        self.update(self._build_display())

    def _build_display(self):
        if not self.data:
            return f"{self.title}\n\n  ┌─────────┐\n  │ [empty] │\n  └─────────┘"

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

    def _render_stack(self):
        lines = [f"{self.title}", "", "  top", "   │"]
        for i, item in enumerate(self.data):
            lines.append(f" ┌─────┐")
            lines.append(f" │{self._pad(item)}│")
            lines.append(f" └─────┘")
            if i < len(self.data) - 1:
                lines.append("   │")
        lines.append(" bottom")
        return "\n".join(lines)

    def _render_queue(self):
        padded = [self._pad(item) for item in self.data]

        dash_count = max(0, 6 * len(padded) - 6)
        top = "front" + "─" * dash_count + "rear"
        box_top = "  ┌" + "─────┬" * (len(padded) - 1) + "─────┐"
        box_mid = "  │" + "│".join(padded) + "│"
        box_bot = "  └" + "─────┴" * (len(padded) - 1) + "─────┘"

        return f"{self.title}\n\n{top}\n{box_top}\n{box_mid}\n{box_bot}"

    def _render_singly_linked(self):
        tops, mids, bots = [], [], []
        for item in self.data:
            tops.append("┌─────┐   ")
            mids.append(f"│{self._pad(item)}│──→")
            bots.append("└─────┘   ")

        lines = [f"{self.title}", ""]
        lines.append("  " + "".join(tops))
        lines.append("  " + "".join(mids))
        lines.append("  " + "".join(bots))
        if self.data:
            null_offset = "  " + " " * (len(self.data) * 10 - 4)
            lines.append(null_offset + "NULL")
        return "\n".join(lines)

    def _render_doubly_linked(self):
        tops, mids, bots = [], [], []
        for item in self.data:
            tops.append("┌─────┐   ")
            mids.append(f"│{self._pad(item)}│←→ ")
            bots.append("└─────┘   ")

        if self.data:
            mids[-1] = mids[-1].replace("←→ ", "   ")

        lines = [f"{self.title}", ""]
        lines.append("  " + "".join(tops))
        lines.append("  " + "".join(mids))
        lines.append("  " + "".join(bots))
        if self.data:
            lines.append("  NULL" + "          " * (len(self.data) - 1) + "  NULL")
        return "\n".join(lines)

    def _render_array(self):
        padded = [self._pad(item) for item in self.data]

        top = "  ┌" + "─────┬" * (len(padded) - 1) + "─────┐"
        mid = "  │" + "│".join(padded) + "│"
        bot = "  └" + "─────┴" * (len(padded) - 1) + "─────┘"

        indices = "   "
        for i in range(len(self.data)):
            indices += str(i).center(5) + " "

        return f"{self.title}\n\n{top}\n{mid}\n{bot}\n{indices}"

    def _pad(self, val):
        s = str(val)
        if len(s) > 5:
            return s[:5]
        return s.center(5)
