#!/usr/bin/env python3
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer
from textual.binding import Binding
from textual.screen import Screen

from screens.splash import SplashScreen
from screens.menu import MainMenu
from screens.trace import TraceWindow

from bridge import DSBridge


class TraceDSApp(App):
    CSS_PATH = None
    TITLE = "TraceDSA"
    SUB_TITLE = "Data Structures Visualization"
    
    # Define available themes if needed
    # THEMES = {"default": "Theme()"}
    
    BINDINGS = [
        Binding("q", "quit", "Quit", priority=True),
        Binding("escape", "quit", "Quit", priority=True),
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
            binary_path = f"./TUI/bins/linux/{name}"
            if os.path.exists(binary_path):
                try:
                    self.bridges[name] = DSBridge(name)
                    print(f"✅ Initialized bridge for {name}")
                except Exception as e:
                    print(f"⚠️  Failed to initialize bridge for {name}: {e}")
            else:
                print(f"⚠️  Binary not found: {binary_path}")
    
    def get_bridge(self, name: str) -> DSBridge:
        return self.bridges.get(name)
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
    
    def on_mount(self) -> None:
        self.push_screen(SplashScreen())
    
    def action_quit(self) -> None:
        for bridge in self.bridges.values():
            bridge.close()
        self.exit()


import os