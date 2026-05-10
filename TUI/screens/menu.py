from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static, Button, Label, Input
from textual.screen import Screen
from textual.binding import Binding
import random

from .trace_screen import TraceWindow


class MainMenu(Screen):

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("escape", "quit", "Quit"),
    ]
    
    CATEGORY_MODULES = {
        "Stack": ["Stack (Array)", "Stack (LinkedList)"],
        "Queue": ["Queue (Array)", "Queue (LinkedList)", "Circular Queue"],
        "LinkedList": ["Singly LinkedList", "Doubly LinkedList"],
        "BST": ["Binary Search Tree"],
        "Heap": ["Min-Heap", "Max-Heap"],
    }
    
    FUN_FACTS = [
        "A stack follows LIFO — last in, first out",
        "A queue follows FIFO — first in, first out",
        "Linked lists excel at insertions/deletions",
        "BSTs keep data sorted for fast lookup",
        "Heaps provide efficient priority access",
        "Hash tables offer O(1) average lookup",
        "Trees are great for hierarchical data",
        "Graphs model complex relationships",
    ]
    
    def __init__(self):
        super().__init__()
        self.selected_category = None
        self.show_level_2 = False
        self.random_fact = random.choice(self.FUN_FACTS)
    
    def compose(self) -> ComposeResult:
        yield Container(
            Container(
                Static("Choose a Data Structure or Algorithm", id="title"),
                Input(placeholder="[ 🔍 Search... ]", id="search_input"),
                id="header-section"
            ),
            
            Container(
                Static(self._get_random_dsa_art(), id="random_art", classes="ascii_art"),
                Static(self.random_fact, id="fun_fact"),
                id="middle_section"
            ),
            
            Container(
                id="button_section"
            ),
            
            id="main_menu_container"
        )
    
    def on_mount(self) -> None:
        self.show_level_1()  # Start with level 1 (categories)
        self.query_one("#search_input").focus()
    
    def _get_random_dsa_art(self) -> str:
        arts = [
            # Stack visualization
            "  [top]  \n  [ 5 ]  \n  [ 3 ]  \n  [ 7 ]  \n[bottom]",
            # Queue visualization  
            "[front] [ 1 ] [ 2 ] [ 3 ] [rear]",
            # Linked list visualization
            "[ 5 ] -> [ 3 ] -> [ 7 ] -> [NULL]",
            # BST visualization
            "    5    \n   / \\   \n  3   7  \n / \\     \n1   4    ",
            # Heap visualization
            "[ 1 ]\n[ 3 ] [ 2 ]\n[ 5 ] [ 4 ] [ 6 ] [ 7 ]",
        ]
        return random.choice(arts)
    
    def show_level_1(self) -> None:
        self.show_level_2 = False
        self.selected_category = None
        self._build_level_1_buttons()
    
    def show_level_2(self, category: str) -> None:
        self.show_level_2 = True
        self.selected_category = category
        self._build_level_2_buttons(category)
    
    def _build_level_1_buttons(self) -> None:
        container = self.query_one("#button_section")
        container.remove_children()
        
        buttons = []
        for category in self.CATEGORY_MODULES.keys():
            btn = Button(category, variant="primary", id=f"category_{category}")
            buttons.append(btn)
        
        # Arrange buttons in rows of 3
        for i in range(0, len(buttons), 3):
            row_buttons = buttons[i:i+3]
            container.mount(Horizontal(*row_buttons, id=f"level1_row_{i//3}"))
    
    def _build_level_2_buttons(self, category: str) -> None:
        container = self.query_one("#button_section")
        container.remove_children()
        
        modules = self.CATEGORY_MODULES.get(category, [])
        buttons = []
        
        # Back button
        back_btn = Button("← Back", variant="default", id="back_button")
        buttons.append(back_btn)
        
        # Module buttons
        for module in modules:
            btn = Button(module, variant="success", id=f"module_{module}")
            buttons.append(btn)
        
        if buttons:
            back_button = buttons[0]
            module_buttons = buttons[1:] if len(buttons) > 1 else []
            
            if module_buttons:
                container.mount(back_button)
                for i in range(0, len(module_buttons), 3):
                    row_buttons = module_buttons[i:i+3]
                    container.mount(Horizontal(*row_buttons, id=f"level2_row_{i//3}"))
            else:
                # Just back button
                container.mount(back_button)
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        
        if button_id.startswith("category_"):
            category = button_id.replace("category_", "")
            self.show_level_2(category)
        elif button_id.startswith("module_"):
            module = button_id.replace("module_", "")
            self._launch_module(module)
        elif button_id == "back_button":
            self.show_level_1()
    
    def _launch_module(self, module_name: str) -> None:
        module_mapping = {
            "Stack (Array)": "stack",
            "Stack (LinkedList)": "stackll",
            "Queue (Array)": "queue",
            "Queue (LinkedList)": "queuell",
            "Circular Queue": "circqueue",
            "Singly LinkedList": "ll",
            "Doubly LinkedList": "dll",
            "Binary Search Tree": "bst",
            "Min-Heap": "heap",
            "Max-Heap": "heap",
        }
        
        binary_name = module_mapping.get(module_name, module_name.lower().replace(" ", ""))
        
        try:
            # Import here to avoid circular imports
            import sys
            sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
            from bridge import get_binary
            binary_path = get_binary(binary_name)
        except Exception:
            binary_path = f"./TUI/bins/linux/{binary_name}"
            alternatives = {
                "heap-min": "heap",
                "heap-max": "heap",
            }
            if binary_name in alternatives:
                binary_name = alternatives[binary_name]
                binary_path = f"./TUI/bins/linux/{binary_name}"
        
        if os.path.exists(binary_path):
            self.app.push_screen(TraceWindow(binary_name, module_name))
        else:
            self.notify(f"Module '{module_name}' not yet implemented", severity="warning")
    
    def action_quit(self) -> None:
        self.app.exit()


import os