from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Static, Button
from textual.screen import Screen
from textual.binding import Binding
from menu import MainMenu


class SplashScreen(Screen):
    
    BINDINGS = [
        Binding("enter", "start_app", "Start"),
        Binding("s", "start_app", "Start"),
    ]
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("[PyPI]", id="pypi-link", classes="link"),
            Static("[GitHub]", id="github-link", classes="link"),
            Static(""),
            Static("██╗  ██╗ █████╗ ", id="ascii-line-1"),
            Static("██║  ██║██╔══██╗", id="ascii-line-2"),
            Static("███████║███████║", id="ascii-line-3"),
            Static("██╔══██║██╔══██║", id="ascii-line-4"),
            Static("██║  ██║██║  ██║", id="ascii-line-5"),
            Static("╚═╝  ╚═╝╚═╝  ╚═╝", id="ascii-line-6"),
            Static(""),
            Static("              Presents  T R A C E D S A              ", id="tagline"),
            Static(""),
            Static("[ START ]", id="start-button"),
            id="splash-container"
        )
    
    def on_mount(self) -> None:
        self.animate_ascii_art()
        self.query_one("#start-button").focus()
    
    def animate_ascii_art(self) -> None:
        ascii_lines = [
            "#ascii-line-1",
            "#ascii-line-2", 
            "#ascii-line-3",
            "#ascii-line-4",
            "#ascii-line-5",
            "#ascii-line-6"
        ]
        
        for line_selector in ascii_lines:
            line = self.query_one(line_selector)
            line.styles.visibility = "hidden"
        
        def show_line(index):
            if index < len(ascii_lines):
                line = self.query_one(ascii_lines[index])
                line.styles.visibility = "visible"
                self.set_timer(0.1, lambda: show_line(index + 1))
        
        show_line(0)
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start-button":
            self.action_start_app()
        elif event.button.id == "pypi-link":
            self.action_open_pypi()
        elif event.button.id == "github-link":
            self.action_open_github()
    
    def action_start_app(self) -> None:
        """Start the application - transition to main menu"""
        self.app.pop_screen()  # Remove splash
        self.app.push_screen(MainMenu())  # Show main menu
    
    def action_open_pypi(self) -> None:
        import webbrowser
        webbrowser.open("https://pypi.org/project/tracedsa/")
    
    def action_open_github(self) -> None:
        import webbrowser
        webbrowser.open("https://github.com/HA2077/TraceDSA")