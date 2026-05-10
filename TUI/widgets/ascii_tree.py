from textual.widget import Widget


class ASCII2DTree(Widget):
    
    def __init__(self, tree_data=None, title="BST"):
        super().__init__()
        self.tree_data = tree_data or []
        self.title = title
        
    def update_tree(self, tree_data):
        """Update the tree data to display"""
        self.tree_data = tree_data or []
        self.refresh()
        
    def render(self):
        """Render the tree as ASCII art with branches"""
        if not self.tree_data:
            return f"{self.title}: Empty Tree"
            
        # For now, we'll display traversal data since that's what we get from the BST
        # In a future enhancement, we could build an actual tree structure
        if isinstance(self.tree_data, list) and len(self.tree_data) > 0:
            if isinstance(self.tree_data[0], str) and self.tree_data[0].startswith('['):
                return f"{self.title}:\n" + " ".join(self.tree_data)
            else:
                # Regular list of values
                return f"{self.title} (In-order): [{' '.join(map(str, self.tree_data))}]"
        else:
            return f"{self.title}: {self.tree_data}"