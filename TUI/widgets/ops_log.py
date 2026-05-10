from textual.widget import Widget
from textual.widgets import Static


class OpsLog(Widget):
    def __init__(self):
        super().__init__()
        self.log_entries = []
        self.max_entries = 100  # Limit log size to prevent memory issues
        self.static = Static("")
        
    def compose(self):
        yield self.static
        
    def add_entry(self, entry):
        self.log_entries.append(entry)
        if len(self.log_entries) > self.max_entries:
            self.log_entries = self.log_entries[-self.max_entries:]
        self._update_display()
        
    def clear(self):
        self.log_entries = []
        self._update_display()
        
    def _update_display(self):
        if not self.log_entries:
            content = "No operations yet"
        else:
            content = "\n".join(self.log_entries)
        self.static.update(content)
        
    def render(self):
        return ""