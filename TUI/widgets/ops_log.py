from textual.widget import Widget
from textual.widgets import RichLog
from rich.text import Text

class OpsLog(Widget):
    def __init__(self, max_entries=100):
        super().__init__()
        self.max_entries = max_entries
        self._rich_log = None

    def compose(self):
        self._rich_log = RichLog(auto_scroll=True, markup=False)
        yield self._rich_log

    def add_entry(self, message: str) -> None:
        if message.startswith("ERROR"):
            text = Text(message, style="bold red")
        elif message.startswith("OK"):
            text = Text(message, style="cyan")
        else:
            text = Text(message, style="dim")

        self._rich_log.write(text)

        while self._rich_log.line_count > self.max_entries:
            self._rich_log.clear()

    def clear(self) -> None:
        self._rich_log.clear()