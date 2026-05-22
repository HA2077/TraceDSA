from textual.widget import Widget
from textual.widgets import Static


class ASCIIBranchTree(Widget):

    def __init__(self, tree_data=None, title="BST"):
        super().__init__()
        self.tree_data = tree_data or []
        self.title = title
        self._root = None

    def compose(self):
        self._static = Static("")
        yield self._static

    def _extract_values(self, data):
        if not data:
            return []
        if isinstance(data[0], str) and data[0].startswith("["):
            content = data[0].strip("[]").split()
            try:
                return [int(x) for x in content if x.strip()]
            except ValueError:
                return data
        try:
            return [int(x) for x in data]
        except (ValueError, TypeError):
            return data

    def update_tree(self, tree_data):
        tree_data = tree_data or []
        if tree_data == self.tree_data and self._root is not None:
            self._refresh_display()
            return
        self.tree_data = tree_data
        values = self._extract_values(tree_data)
        self._root = self._build_bst(values)
        self._refresh_display()

    def _refresh_display(self):
        if hasattr(self, "_static") and self._static is not None:
            self._static.update(self._render())

    def _build_bst(self, values):
        if not values:
            return None
        root = None
        for v in values:
            root = self._insert_node(root, v)
        return root

    def _insert_node(self, node, val):
        if node is None:
            return {"val": val, "left": None, "right": None}
        if val < node["val"]:
            node["left"] = self._insert_node(node["left"], val)
        elif val > node["val"]:
            node["right"] = self._insert_node(node["right"], val)
        return node

    def _render(self):
        if self._root is None:
            return f"{self.title}\n\n  ┌─────────┐\n  │ [empty] │\n  └─────────┘"

        lines = []
        self._draw_tree(self._root, "", True, lines)
        return f"{self.title}\n\n" + "\n".join(lines)

    def _draw_tree(self, node, prefix, is_last, lines):
        if node is None:
            return

        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}{node['val']}")

        new_prefix = prefix + ("    " if is_last else "│   ")

        if node["left"] is not None or node["right"] is not None:
            if node["left"]:
                self._draw_tree(node["left"], new_prefix, node["right"] is None, lines)

            if node["right"]:
                self._draw_tree(node["right"], new_prefix, True, lines)
