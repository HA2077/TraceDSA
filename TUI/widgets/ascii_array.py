from textual.widget import Widget


class ASCIIArray(Widget):
    def __init__(self, data=None, title="Array"):
        super().__init__()
        self.data = data or []
        self.title = title
        
    def update_data(self, data):
        self.data = data
        self.refresh()
        
    def render(self):
        if not self.data:
            return f"{self.title}: []"
            
        # Create boxes for each element
        boxes = []
        for item in self.data:
            boxes.append(f"[{item}]")
            
        if "Stack" in self.title:
            return f"{self.title} (top):\n" + " → ".join(reversed(boxes))
        elif "Queue" in self.title:
            return f"{self.title} (front):\n" + " → ".join(boxes)
        else:
            return f"{self.title}: " + " ".join(boxes)