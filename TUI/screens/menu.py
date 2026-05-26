import os
import re
import random

from textual.app import ComposeResult
from textual.containers import Container, Horizontal, ScrollableContainer
from textual.widgets import Static, Button, Input
from textual.screen import Screen
from textual.binding import Binding
from textual.widgets import Footer

from .trace_screen import TraceWindow
from .help_screen import HelpScreen


class MainMenu(Screen):

    BINDINGS = [
        Binding("/", "focus_search", "Search"),
        Binding("q", "show_confirm_quit", "Quit"),
        Binding("h", "show_help", "Help"),
        Binding("?", "show_help", "Help"),
    ]

    DEFAULT_CSS = """
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
        margin-bottom: 1;
    }

    #search_wrapper {
        layout: horizontal;
        align: center middle;
        width: 100%;
        height: auto;
    }

    #search_input {
        width: 50;
        background: #1a1a2e;
        border: solid #0f3460;
        color: #e0e0e0;
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

    #button_scroll {
        width: 100%;
        height: 1fr;
        background: transparent;
    }

    #button_section {
        layout: vertical;
        align: center middle;
        width: 100%;
        height: auto;
        padding: 1 2;
    }

    #button_section Horizontal {
        align: center middle;
        width: 100%;
        height: auto;
        margin-bottom: 1;
    }

    #button_section > Button {
        margin-bottom: 1;
        align: center middle;
    }

    /* === Buttons === */
    Button.primary {
        min-width: 24;
        padding: 0 3;
        background: #16213e;
        border: solid #00d4ff;
        color: #00d4ff;
    }

    Button.primary:hover {
        background: #00d4ff;
        color: #1a1a2e;
    }

    Button.success {
        min-width: 22;
        padding: 0 3;
        background: #1a1a2e;
        border: solid #0f3460;
        color: #e0e0e0;
    }

    Button.success:hover {
        background: #00d4ff;
        color: #1a1a2e;
        border: solid #00d4ff;
    }

    Button.default {
        min-width: 12;
        background: #16213e;
        border: solid #0f3460;
        color: #666680;
    }

    Button.default:hover {
        color: #e0e0e0;
        border: solid #00d4ff;
    }

    /* Search results */
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
        "Your CPU uses a call stack to track function calls",
        "Undo/redo in every text editor is just two stacks",
        "DFS graph traversal can be implemented with a stack",

        "A queue follows FIFO — first in, first out",
        "OS schedulers use priority queues to manage processes",
        "BFS graph traversal uses a queue under the hood",
        "Circular queues avoid the wasted space of linear queues",

        "Linked lists excel at O(1) insertions and deletions",
        "Your RAM is essentially a giant implicit linked structure",
        "The Linux kernel uses doubly linked lists extensively",
        "Linked lists trade random access for flexible memory use",

        "BSTs keep data sorted for O(log n) average lookup",
        "A perfectly balanced BST is basically a binary search",
        "In-order traversal of a BST gives sorted output",
        "AVL trees self-balance to guarantee O(log n) worst case",
        "The first BST was described by P.F. Windley in 1960",

        "Heaps give O(1) access to the min or max element",
        "Heapsort runs in O(n log n) with O(1) extra space",
        "Python's heap module is a min-heap by default",
        "A heap is complete — every level filled left to right",

        "Arrays have O(1) access because memory is contiguous",
        "Hash tables offer O(1) average lookup via hashing",
        "Dijkstra's algorithm uses a min-heap for efficiency",
        "The word 'algorithm' comes from Al-Khwarizmi's name",
        "Graphs model everything: maps, social networks, compilers",
        "A trie can autocomplete words in O(L) where L is length",
        "Most interview problems reduce to 5 core DS patterns",
        "This one is special one the probability of this showing up is 3.6%"
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
        yield Footer()
        yield Container(
            Container(
                Static("Choose a Data Structure or Algorithm", id="title"),
                Container(
                    Input(placeholder="[ 🔍 Search... ]", id="search_input"),
                    id="search_wrapper"
                ),
                id="header-section"
            ),
            Container(
                Static(self._get_random_dsa_art(), id="random_art"),
                Static(self.random_fact, id="fun_fact"),
                id="middle_section"
            ),
            ScrollableContainer(
                Container(id="button_section"),
                id="button_scroll"
            ),
            id="main_menu_container"
        )

    def on_mount(self) -> None:
        self._show_level_1()
        self.query_one("#search_input").focus()

    def action_focus_search(self) -> None:
        self.query_one("#search_input").focus()

    def action_show_help(self) -> None:
        self.app.push_screen(HelpScreen())

    def _get_random_dsa_art(self) -> str:
        arts = [
            "  [top]  \n  [ 5 ]  \n  [ 3 ]  \n  [ 7 ]  \n[bottom]",
            "  ┌─────┐\n  │  9  │\n  │  4  │\n  │  1  │\n  └─────┘",
            "  PUSH →\n  [ A ]  \n  [ B ]  \n  [ C ]  \n  ← POP",

            "[front] [ 1 ] [ 2 ] [ 3 ] [rear]",
            "enq→ [ 7 ][ 5 ][ 3 ][ 1 ] →deq",

            "[ 5 ] -> [ 3 ] -> [ 7 ] -> [NULL]",
            "┌───┐  ┌───┐  ┌───┐\n│ 1 │→ │ 2 │→ │ 3 │→ NULL\n└───┘  └───┘  └───┘",
            "NULL ← [ A ] ↔ [ B ] ↔ [ C ] → NULL",

            "    5    \n   / \\   \n  3   7  \n / \\     \n1   4    ",
            "      8\n    /   \\\n   3     10\n  / \\      \\\n 1   6     14",
            "   [50]\n  /    \\\n[30]  [70]\n /  \\\n[20][40]",

            "[ 1 ]\n[ 3 ] [ 2 ]\n[ 5 ] [ 4 ] [ 6 ] [ 7 ]",
            "      [1]\n    [3] [2]\n  [7][6][5][4]",
            "min→ [1][3][2][7][6][5][4]",

            "┌───┬───┬───┬───┐\n│ 4 │ 2 │ 7 │ 1 │\n└───┴───┴───┴───┘\n  0   1   2   3",
            "[ 10 | 20 | 30 | 40 | 50 ]",

            "  A --- B\n  |  \\  |\n  C --- D",
            "  (A)→(B)→(D)\n   ↓    ↓\n  (C)→(E)",
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
        self._module_id_map.clear()

        back_btn = Button("← Back", variant="default", id="back_button")
        module_buttons = []

        for module in modules:
            safe_id = self._sanitize_id(module)
            self._module_id_map[safe_id] = module
            module_buttons.append(Button(module, variant="success", id=f"module_{safe_id}"))

        container.mount(back_btn)
        for i in range(0, len(module_buttons), 3):
            container.mount(Horizontal(*module_buttons[i:i+3], id=f"level2_row_{i//3}"))

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
            import sys
            sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
            from bridge import get_binary
            binary_path = get_binary(binary_name)
        except Exception:
            binary_path = f"./TUI/bins/linux/{binary_name}"

        if os.path.exists(binary_path):
            self.app.push_screen(TraceWindow(binary_name, module_name))
        else:
            self.notify(f"Module '{module_name}' not yet implemented", severity="warning")

    def action_quit(self) -> None:
        self.app.exit()