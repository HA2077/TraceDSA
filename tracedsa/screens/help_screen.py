from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Static, Button
from textual.screen import Screen
from textual.binding import Binding

class HelpScreen(Screen):

    DEFAULT_CSS = """
    HelpScreen {
        align: center middle;
        background: rgba(0, 0, 0, 0.7);
    }
    #help-box {
        width: 54;
        height: auto;
        padding: 2 3;
        background: #16213e;
        border: solid #00d4ff;
    }
    .hlp-section {
        color: #00d4ff;
        text-style: bold;
        width: 100%;
        margin-top: 1;
    }
    .hlp-row {
        color: #e0e0e0;
        width: 100%;
    }
    .hlp-key {
        color: #ffffff;
        text-style: bold;
    }
    .hlp-dismiss {
        color: #666680;
        width: 100%;
        text-align: center;
        margin-top: 1;
    }
    #help-box Button {
        margin-top: 1;
        width: 14;
    }
    """

    BINDINGS = [
        Binding("h", "dismiss", "Close"),
        Binding("?", "dismiss", "Close"),
        Binding("escape", "dismiss", "Close"),
    ]

    def compose(self) -> ComposeResult:
        yield Container(
            Static("K E Y B O A R D   S H O R T C U T S", classes="hlp-section"),
            Static(""),
            Container(id="help-entries"),
            Static("", id="help-spacer"),
            Static("[ h, ?, escape, or Close button to dismiss ]", classes="hlp-dismiss"),
            Button("Close", id="help-close", variant="default"),
            id="help-box"
        )

    def on_mount(self) -> None:
        entries = self.query_one("#help-entries")
        shortcuts = getattr(self.app, "SHORTCUTS", {})
        for group, items in shortcuts.items():
            entries.mount(Static(f"  {group.upper()}", classes="hlp-section"))
            for key_str, desc, _scope in items:
                entries.mount(Static(
                    f"    [{key_str}]  {desc}", classes="hlp-row", markup=False
                ))
            entries.mount(Static(""))

    def action_dismiss(self) -> None:
        self.app.pop_screen()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "help-close":
            self.app.pop_screen()