from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Static, Button
from textual.screen import Screen
from textual.binding import Binding


class ConfirmDialog(Screen):

    DEFAULT_CSS = """
    ConfirmDialog {
        align: center middle;
        background: rgba(0, 0, 0, 0.7);
    }

    #confirm-box {
        width: 44;
        height: auto;
        padding: 2 4;
        background: #16213e;
        border: solid #00d4ff;
        align: center middle;
    }

    #confirm-title {
        text-align: center;
        width: 100%;
        color: #ffffff;
        text-style: bold;
        margin-bottom: 1;
    }

    #confirm-subtitle {
        text-align: center;
        width: 100%;
        color: #666680;
        margin-bottom: 1;
    }

    #confirm-buttons {
        align: center middle;
        width: 100%;
        height: auto;
        margin-top: 1;
    }

    #confirm-y {
        background: #16213e;
        border: solid #00d4ff;
        color: #00d4ff;
        width: 1;
        margin-right: 1;
    }

    #confirm-y:hover {
        background: #00d4ff;
        color: #1a1a2e;
    }

    #confirm-n {
        background: #16213e;
        border: solid #666680;
        color: #666680;
        width: 1;
    }

    #confirm-n:hover {
        background: #666680;
        color: #1a1a2e;
    }
    """

    BINDINGS = [
        Binding("y", "confirm", "Yes"),
        Binding("n", "cancel", "No"),
        Binding("escape", "cancel", "Cancel"),
    ]

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Exit TraceDSA?", id="confirm-title"),
            Static("All unsaved state will be lost.", id="confirm-subtitle"),
            Horizontal(
                Button("Yes  [y]", id="confirm-y"),
                Button("No   [n]", id="confirm-n"),
                id="confirm-buttons"
            ),
            id="confirm-box"
        )

    def action_confirm(self) -> None:
        self.app.exit()

    def action_cancel(self) -> None:
        self.app.pop_screen()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "confirm-y":
            self.app.exit()
        else:
            self.app.pop_screen()