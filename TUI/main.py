#!/usr/bin/env python3
from textual.app import App, ComposeResult
from textual.binding import Binding

from screens.splash import SplashScreen

import platform
import os

from bridge import DSBridge


class TraceDSApp(App):
    CSS_PATH = None

    DEFAULT_CSS = """
    /* === Color Variables === */
    $bg: #1a1a2e;
    $panel-bg: #16213e;
    $panel-border: #0f3460;
    $accent: #00d4ff;
    $text: #e0e0e0;
    $text-bright: #ffffff;
    $error: #ff4444;
    $ok: #00d4ff;
    $dim: #666680;

    /* === App === */
    App {
        background: $bg;
        color: $text;
    }

    Screen {
        background: $bg;
    }

    /* === Typography === */
    Static, Label {
        color: $text;
    }

    /* === Containers === */
    Container {
        background: transparent;
    }

    /* === Splash Screen === */
    #splash-container {
        layout: vertical;
        align: center middle;
        width: 60;
        height: auto;
        background: $panel-bg;
        border: solid $accent;
        padding: 2 4;
    }

    #pypi-link, #github-link {
        color: $accent;
        text-style: underline;
        width: auto;
    }

    #pypi-link:hover, #github-link:hover {
        color: $text-bright;
    }

    #ascii-line-1, #ascii-line-2, #ascii-line-3,
    #ascii-line-4, #ascii-line-5, #ascii-line-6 {
        color: $accent;
        text-style: bold;
        width: auto;
    }

    #tagline {
        color: $text-bright;
        text-align: center;
        width: 100%;
    }

    #start-button {
        width: auto;
        text-align: center;
    }

    #start-button Button {
        background: $accent;
        color: $bg;
        text-style: bold;
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
        background: $panel-bg;
        border: solid $panel-border;
        padding: 1 2;
    }

    #title {
        color: $text-bright;
        text-style: bold;
        text-align: center;
        width: 100%;
    }

    #search_input {
        width: 40;
        margin: 1 0;
        background: $bg;
        border: solid $panel-border;
        color: $text;
    }

    #search_input:focus {
        border: solid $accent;
    }

    #search_input > .input--placeholder {
        color: $dim;
    }

    #middle_section {
        layout: vertical;
        align: center middle;
        width: 100%;
        height: auto;
        background: $panel-bg;
        border: solid $panel-border;
        padding: 1 2;
        margin: 1 0;
    }

    #random_art {
        color: $accent;
        text-align: center;
        width: 100%;
    }

    #fun_fact {
        color: $text;
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
    }

    /* === Buttons === */
    Button {
        background: $panel-bg;
        color: $text;
        border: solid $panel-border;
        text-style: bold;
    }

    Button:hover {
        background: $accent;
        color: $bg;
    }

    Button:focus {
        border: solid $accent;
        text-style: bold underline;
    }

    Button.primary {
        color: $accent;
        border: solid $accent;
    }

    Button.primary:hover {
        background: $accent;
        color: $bg;
    }

    Button.success {
        color: $text-bright;
        border: solid $panel-border;
    }

    Button.success:hover {
        background: $accent;
        color: $bg;
    }

    Button.default {
        color: $dim;
        border: solid $panel-border;
    }

    Button.default:hover {
        color: $text;
        border: solid $accent;
    }

    /* === Trace Window === */
    #trace_window_container {
        layout: vertical;
        width: 100%;
        height: 100%;
    }

    #trace_header {
        layout: horizontal;
        width: 100%;
        height: auto;
        background: $panel-bg;
        border: solid $panel-border;
        padding: 0 2;
    }

    #trace_header #back_button {
        width: auto;
        color: $dim;
    }

    #trace_header #back_button:hover {
        color: $accent;
    }

    #module_name {
        color: $text-bright;
        text-style: bold;
        text-align: center;
        width: 1fr;
    }

    #main_content {
        width: 100%;
        height: 1fr;
    }

    #ascii_panel {
        width: 60%;
        height: 100%;
        background: $panel-bg;
        border: solid $panel-border;
        padding: 1 2;
    }

    #ascii_placeholder {
        color: $dim;
        text-align: center;
    }

    #log_panel {
        width: 40%;
        height: 100%;
        background: $panel-bg;
        border: solid $panel-border;
        layout: vertical;
        padding: 0 1;
    }

    #log_header {
        color: $accent;
        text-style: bold;
        width: 100%;
        text-align: center;
        padding: 1 0;
    }

    RichLog {
        background: $bg;
        color: $text;
        width: 100%;
        height: 1fr;
    }

    #button_container {
        width: 100%;
        height: auto;
        background: $panel-bg;
        border: solid $panel-border;
        padding: 1 2;
        layout: horizontal;
    }

    #button_container Horizontal {
        width: auto;
        margin-right: 1;
    }

    /* === Inputs in Trace Window === */
    Input {
        background: $bg;
        color: $text;
        border: solid $panel-border;
        width: 12;
        margin-right: 1;
    }

    Input:focus {
        border: solid $accent;
    }

    Input > .input--placeholder {
        color: $dim;
    }

    /* === Notification === */
    .notification {
        border: solid $accent;
    }

    /* === Scrollbar === */
    ScrollBar {
        background: $bg;
    }

    ScrollBar:hover {
        background: $panel-bg;
    }

    ScrollBar > .scrollbar--thumb {
        background: $accent;
    }

    ScrollBar > .scrollbar--thumb:hover {
        background: $text-bright;
    }
    """

    TITLE = "TraceDSA"
    SUB_TITLE = "Data Structures Visualization"

    BINDINGS = [
        Binding("q", "quit", "Quit", priority=True),
    ]

    def __init__(self):
        super().__init__()
        self.bridges = {}
        self._initialize_bridges()

    def _initialize_bridges(self):
        binary_names = [
            "stack", "stackll", "queue", "queuell",
            "circqueue", "ll", "dll", "bst", "heap"
        ]

        for name in binary_names:
            sysname = platform.system().lower()
            binary_path = f"TUI/bins/{sysname}/{name}"
            if os.path.exists(binary_path):
                try:
                    self.bridges[name] = DSBridge(name)
                except Exception:
                    pass

    def get_bridge(self, name: str):
        return self.bridges.get(name)

    def compose(self) -> ComposeResult:
        yield from []

    def on_mount(self) -> None:
        self.push_screen(SplashScreen())

    def action_quit(self) -> None:
        for bridge in self.bridges.values():
            bridge.close()
        self.exit()

def main():
    app = TraceDSApp()
    app.run()

if __name__ == "__main__":
    main()