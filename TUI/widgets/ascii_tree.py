from textual.widget import Widget
from textual.widgets import Static


class ASCII2DTree(Widget):

    def __init__(self, tree_data=None, title="BST"):
        super().__init__()
        self.tree_data = tree_data or []
        self.title = title
        self._root = None

    def compose(self):
        self._static = Static("")
        yield self._static

    def update_tree(self, tree_data):
        self.tree_data = tree_data or []
        self._root = self._build_bst(self.tree_data)
        self._refresh_display()

    def _refresh_display(self):
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
        if not self.tree_data:
            return f"{self.title}: Empty Tree"

        if isinstance(self.tree_data[0], str) and self.tree_data[0].startswith("["):
            content = self.tree_data[0].strip("[]").split()
            try:
                values = [int(x) for x in content if x.strip()]
            except ValueError:
                return f"{self.title}:\n" + " ".join(self.tree_data)
            self._root = self._build_bst(values)
        else:
            try:
                values = [int(x) for x in self.tree_data]
            except (ValueError, TypeError):
                return f"{self.title}: {self.tree_data}"
            self._root = self._build_bst(values)

        if self._root is None:
            return f"{self.title}: Empty Tree"

        lines = []
        self._draw_tree(self._root, "", True, lines)
        return f"{self.title}\n\n" + "\n".join(lines)

    def _draw_tree(self, node, prefix, is_last, lines):
        if node is None:
            return

        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}{node['val']}")

        new_prefix = prefix + ("    " if is_last else "│   ")

        has_children = node["left"] is not None or node["right"] is not None

        if has_children:
            if node["left"]:
                self._draw_tree(node["left"], new_prefix, node["right"] is None, lines)
            else:
                pass

            if node["right"]:
                self._draw_tree(node["right"], new_prefix, True, lines)