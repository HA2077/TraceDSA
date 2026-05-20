from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Static, Button
from textual.screen import Screen
from textual.binding import Binding
from .menu import MainMenu


class SplashScreen(Screen):

    BINDINGS = [
        Binding("enter", "start_app", "Start"),
        Binding("s", "start_app", "Start"),
    ]

    BINARY_NAMES = [
        "stack", "stackll", "queue", "queuell",
        "circqueue", "ll", "dll", "bst", "heap"
    ]

    DEFAULT_CSS = """
    SplashScreen {
        align: center middle;
        background: #1a1a2e;
    }

    #splash-container {
        layout: vertical;
        align: center middle;
        width: 60;
        height: auto;
        background: #16213e;
        border: solid #00d4ff;
        padding: 2 4;
    }

    #links-row {
        layout: horizontal;
        width: 100%;
        height: auto;
        align: center middle;
        margin-bottom: 1;
    }

    #pypi-btn, #github-btn {
        background: transparent;
        color: #00d4ff;
        border: none;
        width: auto;
        min-width: 8;
        text-style: bold;
    }

    #pypi-btn:hover, #github-btn:hover {
        background: transparent;
        color: #ffffff;
        text-style: bold underline;
    }

    #pypi-btn:focus, #github-btn:focus {
        background: transparent;
        border: none;
        color: #ffffff;
        text-style: bold underline;
    }

    #link-sep {
        color: #666680;
        width: 3;
        text-align: center;
    }

    #ascii-line-1, #ascii-line-2, #ascii-line-3,
    #ascii-line-4, #ascii-line-5, #ascii-line-6 {
        color: #00d4ff;
        text-style: bold;
        width: 100%;
        text-align: center;
    }

    #tagline {
        color: #ffffff;
        text-align: center;
        width: 100%;
        margin-top: 1;
    }

    #pertag {
        color: #ffffff;
        text-align: center;
        width: 100%;
        margin-top: 1;
    }

    #start-row {
        width: 100%;
        height: auto;
        align: center middle;
        margin: 1 0;
    }

    #start-button {
        width: 20;
        background: #00d4ff;
        color: #1a1a2e;
        text-style: bold;
        border: none;
    }

    #start-button:hover {
        background: #ffffff;
        color: #1a1a2e;
    }

    #start-button:focus {
        background: #ffffff;
        color: #1a1a2e;
        border: solid #ffffff;
    }

    #start-button:disabled {
        opacity: 40%;
    }

    #progress-text {
        color: #666680;
        text-align: center;
        width: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Container(
            Container(
                Button("PyPI", id="pypi-btn"),
                Static("|", id="link-sep"),
                Button("GitHub", id="github-btn"),
                id="links-row"
            ),
            Static("██╗  ██╗ █████╗ ", id="ascii-line-1"),
            Static("██║  ██║██╔══██╗", id="ascii-line-2"),
            Static("███████║███████║", id="ascii-line-3"),
            Static("██╔══██║██╔══██║", id="ascii-line-4"),
            Static("██║  ██║██║  ██║", id="ascii-line-5"),
            Static("╚═╝  ╚═╝╚═╝  ╚═╝", id="ascii-line-6"),
            Static("Presents", id="pertag"),
            Static("T  R  A  C  E  D  S  A", id="tagline"),
            Container(
                Button("START", id="start-button", disabled=True),
                id="start-row"
            ),
            Static("Initializing...", id="progress-text"),
            id="splash-container"
        )

    def on_mount(self) -> None:
        self._total_bridges = len(self.BINARY_NAMES)
        self._start_button = self.query_one("#start-button")
        self._progress_text = self.query_one("#progress-text")
        self.animate_ascii_art()
        self._init_next_bridge(0)

    def animate_ascii_art(self) -> None:
        selectors = [
            "#ascii-line-1", "#ascii-line-2", "#ascii-line-3",
            "#ascii-line-4", "#ascii-line-5", "#ascii-line-6"
        ]
        for s in selectors:
            self.query_one(s).styles.visibility = "hidden"

        def show_line(index):
            if index < len(selectors):
                self.query_one(selectors[index]).styles.visibility = "visible"
                self.set_timer(0.08, lambda: show_line(index + 1))

        show_line(0)

    def _init_next_bridge(self, index: int) -> None:
        if index >= len(self.BINARY_NAMES):
            self._start_button.disabled = False
            self._start_button.focus()
            self._progress_text.update("✓ All modules loaded — press S or ENTER to start")
            return

        name = self.BINARY_NAMES[index]
        self.app.initialize_bridge(name)
        self._progress_text.update(
            f"Loading {name}... ({index + 1}/{self._total_bridges})"
        )
        self.set_timer(0.1, lambda: self._init_next_bridge(index + 1))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn = event.button.id
        if btn == "start-button":
            self.action_start_app()
        elif btn == "pypi-btn":
            import webbrowser
            webbrowser.open("https://pypi.org/project/tracedsa/")
        elif btn == "github-btn":
            import webbrowser
            webbrowser.open("https://github.com/HA2077/TraceDSA")

    def action_start_app(self) -> None:
        if self._start_button.disabled:
            return
        self.app.switch_screen(MainMenu())