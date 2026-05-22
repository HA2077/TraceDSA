import os
import re
import random

from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static, Button, Label, Input
from textual.screen import Screen
from textual.binding import Binding

from .trace_screen import TraceWindow


class MainMenu(Screen):

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("escape", "quit", "Quit"),
    ]

    DEFAULT_CSS = """
    .search-category-header {
        color: #00d4ff;
        text-style: bold;
        width: 100%;
        padding: 0 0 0 1;
        margin-top: 1;
        margin-bottom: 0;
    }

    .no-results {
        color: #666680;
        text-align: center;
        width: 100%;
        margin-top: 2;
    }

    #search_results_container {
        layout: vertical;
        width: 100%;
        height: auto;
        padding: 0 2;
    }
    """
    
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
        self._module_id_map = {}
        self._mount_counter = 0
    
    def _next_id(self, prefix: str) -> str:
        self._mount_counter += 1
        return f"{prefix}_{self._mount_counter}"
    
    def _sanitize_id(self, text: str) -> str:
        sanitized = re.sub(r'[^a-zA-Z0-9_-]', '_', text)
        if sanitized and sanitized[0].isdigit():
            sanitized = '_' + sanitized
        return sanitized
    
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
        self._show_level_1()
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
    
    def on_input_changed(self, event: Input.Changed) -> None:
        value = event.value.strip()
        if not value:
            self._restore_normal_state()
        else:
            self._show_search_results(value)

    def _collect_matches(self, query: str) -> list:
        q = query.lower()
        matches = []
        for category, modules in self.CATEGORY_MODULES.items():
            cat_match = q in category.lower()
            if cat_match:
                for module in modules:
                    matches.append((category, module))
            else:
                for module in modules:
                    if q in module.lower():
                        matches.append((category, module))
        return matches

    def _show_search_results(self, query: str) -> None:
        self.show_level_2 = False
        self.query_one("#middle_section").display = False

        matches = self._collect_matches(query)
        container = self.query_one("#button_section")
        container.remove_children()
        self._module_id_map.clear()

        if not matches:
            container.mount(Static("No matching modules", classes="no-results"))
            return

        current_category = None
        for category, module in matches:
            if category != current_category:
                container.mount(Static(category, classes="search-category-header"))
                current_category = category
            safe_id = self._sanitize_id(module)
            search_id = self._next_id("search")
            self._module_id_map[search_id] = module
            container.mount(Button(module, variant="success", id=search_id))

    def _restore_normal_state(self) -> None:
        self.query_one("#middle_section").display = True
        if self.show_level_2:
            self._build_level_2_buttons(self.selected_category)
        else:
            self._build_level_1_buttons()

    def _show_level_1(self) -> None:
        self.show_level_2 = False
        self.selected_category = None
        self._build_level_1_buttons()
    
    def _show_level_2(self, category: str) -> None:
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
        
        for i in range(0, len(buttons), 3):
            row_buttons = buttons[i:i+3]
            container.mount(Horizontal(*row_buttons, id=f"level1_row_{i//3}"))
    
    def _build_level_2_buttons(self, category: str) -> None:
        container = self.query_one("#button_section")
        container.remove_children()
        
        modules = self.CATEGORY_MODULES.get(category, [])
        buttons = []
        self._module_id_map.clear()
        
        back_btn = Button("← Back", variant="default", id="back_button")
        buttons.append(back_btn)
        
        for module in modules:
            safe_id = self._sanitize_id(module)
            self._module_id_map[safe_id] = module
            btn = Button(module, variant="success", id=f"module_{safe_id}")
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
                container.mount(back_button)
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        
        if button_id.startswith("category_"):
            category = button_id.replace("category_", "")
            self._show_level_2(category)
        elif button_id.startswith("module_"):
            safe_id = button_id.replace("module_", "")
            module = self._module_id_map.get(safe_id)
            if module:
                self._launch_module(module)
        elif button_id.startswith("search_"):
            module = self._module_id_map.get(button_id)
            if module:
                self._launch_module(module)
        elif button_id == "back_button":
            self._show_level_1()
    
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