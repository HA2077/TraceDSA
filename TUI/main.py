#!/usr/bin/env python3
from textual.app import App, ComposeResult
from textual.binding import Binding

from screens.splash import SplashScreen
from screens.confirm_dialog import ConfirmDialog

import platform
import os

from bridge import DSBridge


SHORTCUTS = {
    "global": [
        ("q", "Quit (with confirmation)", "All screens"),
        ("h / ?", "Show this help screen", "All screens"),
    ],
    "splash": [
        ("enter / s", "Start application", "SplashScreen"),
    ],
    "menu": [
        ("/", "Focus search bar to filter modules", "MainMenu"),
        ("escape", "Quit (with confirmation)", "MainMenu"),
    ],
    "trace": [
        ("escape", "Return to main menu", "TraceWindow"),
        ("Tab", "Cycle through buttons and inputs", "TraceWindow"),
    ],
}


class TraceDSApp(App):
    CSS_PATH = None

    SHORTCUTS = SHORTCUTS

    DEFAULT_CSS = """
    /* === App & Screen === */
    App {
        background: #1a1a2e;
        color: #e0e0e0;
    }

    Screen {
        background: #1a1a2e;
        height: 100%;
    }

    Static, Label {
        color: #e0e0e0;
    }

    Container {
        background: transparent;
    }

    /* === Main Menu === */
    #main_menu_container {
        layout: vertical;
        width: 100%;
        height: 100%;
    }

    #header-section {
        layout: vertical;
        align: center middle;
        width: 100%;
        height: auto;
        background: #16213e;
        border: solid #0f3460;
        padding: 1 2;
        margin-bottom: 1;
    }

    #title {
        color: #ffffff;
        text-style: bold;
        text-align: center;
        width: 100%;
    }

    #search_input {
        width: 40;
        margin: 1 0;
        background: #1a1a2e;
        border: solid #0f3460;
        color: #e0e0e0;
    }

    #search_input:focus {
        border: solid #00d4ff;
    }

    #search_input > .input--placeholder {
        color: #666680;
    }

    #middle_section {
        layout: vertical;
        align: center middle;
        width: 100%;
        height: auto;
        background: #16213e;
        border: solid #0f3460;
        padding: 1 2;
        margin-bottom: 1;
    }

    #random_art {
        color: #00d4ff;
        text-align: center;
        width: 100%;
    }

    #fun_fact {
        color: #e0e0e0;
        text-align: center;
        text-style: italic;
        width: 100%;
        margin-top: 1;
    }

    #button_section {
        layout: vertical;
        align: center middle;
        width: 100%;
        height: 1fr;
        padding: 1 2;
        overflow-y: auto;
        overflow-x: hidden;
    }

    #button_section Horizontal {
        margin-bottom: 1;
    }

    /* === Buttons === */
    Button {
        background: #16213e;
        color: #e0e0e0;
        border: solid #0f3460;
        text-style: bold;
    }

    Button:hover {
        background: #00d4ff;
        color: #1a1a2e;
    }

    Button:focus {
        border: solid #00d4ff;
        text-style: bold underline;
    }

    Button.primary {
        color: #00d4ff;
        border: solid #00d4ff;
    }

    Button.primary:hover {
        background: #00d4ff;
        color: #1a1a2e;
    }

    Button.success {
        color: #ffffff;
        border: solid #0f3460;
    }

    Button.success:hover {
        background: #00d4ff;
        color: #1a1a2e;
    }

    Button.default {
        color: #666680;
        border: solid #0f3460;
    }

    Button.default:hover {
        color: #e0e0e0;
        border: solid #00d4ff;
    }

    /* === Trace Window === */
    #trace_window_container {
        layout: vertical;
        width: 100%;
        height: 100%;
    }

    #trace_header {
        layout: horizontal;
        content-align: left middle;
        width: 100%;
        height: auto;
        background: #16213e;
        border: solid #0f3460;
        padding: 0 2;
    }

    #trace_header #back_button {
        width: auto;
        color: #666680;
    }

    #trace_header #back_button:hover {
        color: #00d4ff;
    }

    #module_name {
        color: #ffffff;
        text-style: bold;
        text-align: center;
        width: 1fr;
    }

    #main_content {
        layout: horizontal;
        width: 100%;
        height: 1fr;
    }

    #ascii_panel {
        width: 60%;
        height: 100%;
        background: #16213e;
        border: solid #0f3460;
        padding: 1 2;
        overflow: auto;
    }

    #ascii_placeholder {
        color: #666680;
        text-align: center;
    }

    #ascii_panel Static {
        width: 100%;
        height: auto;
    }

    ASCIIArray, ASCIIBranchTree, ASCIIHeap {
        width: 100%;
        height: 100%;
    }

    #log_panel {
        width: 40%;
        height: 100%;
        background: #16213e;
        border: solid #0f3460;
        layout: vertical;
        padding: 0 1;
    }

    #log_header {
        color: #00d4ff;
        text-style: bold;
        width: 100%;
        text-align: center;
        padding: 1 0;
    }

    #log_panel RichLog {
        background: #1a1a2e;
        color: #e0e0e0;
        width: 100%;
        height: 1fr;
    }

    OpsLog {
        width: 100%;
        height: 1fr;
    }

    #button_container {
        width: 100%;
        height: auto;
        background: #16213e;
        border: solid #0f3460;
        padding: 1 2;
        layout: horizontal;
        overflow-x: auto;
    }

    #button_container Horizontal {
        width: auto;
        margin-right: 1;
    }

    /* === Status Bar === */
    #status_bar {
        color: #666680;
        text-style: italic;
        width: 100%;
        height: auto;
        padding: 0 2;
        background: #16213e;
        border-top: solid #0f3460;
    }

    /* === Inputs === */
    Input {
        background: #1a1a2e;
        color: #e0e0e0;
        border: solid #0f3460;
        width: 12;
        margin-right: 1;
    }

    Input:focus {
        border: solid #00d4ff;
    }

    Input > .input--placeholder {
        color: #666680;
    }

    /* === Scrollbar === */
    ScrollBar {
        background: #1a1a2e;
    }

    ScrollBar:hover {
        background: #16213e;
    }

    ScrollBar > .scrollbar--thumb {
        background: #00d4ff;
    }

    ScrollBar > .scrollbar--thumb:hover {
        background: #ffffff;
    }
    """

    TITLE = "TraceDSA"
    SUB_TITLE = "Data Structures Visualization"

    BINDINGS = [
        Binding("q", "show_confirm_quit", "Quit", priority=True),
    ]

    def __init__(self):
        super().__init__()
        self.bridges = {}

    def initialize_bridge(self, name: str) -> bool:
        sysname = platform.system().lower()
        binary_path = f"TUI/bins/{sysname}/{name}"
        if os.path.exists(binary_path):
            try:
                self.bridges[name] = DSBridge(name)
                return True
            except Exception:
                return False
        return False

    def get_bridge(self, name: str):
        return self.bridges.get(name)

    def compose(self) -> ComposeResult:
        yield from []

    def on_mount(self) -> None:
        self.push_screen(SplashScreen())

    def action_show_confirm_quit(self) -> None:
        from screens.confirm_dialog import ConfirmDialog
        if isinstance(self.screen, ConfirmDialog):
            self.exit()
        else:
            self.push_screen(ConfirmDialog())

    def action_quit(self) -> None:
        for bridge in self.bridges.values():
            bridge.close()
        self.exit()


def main():
    app = TraceDSApp()
    app.run()


if __name__ == "__main__":
    main()