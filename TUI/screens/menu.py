import os
import re
import random

from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Static, Button, Input
from textual.screen import Screen
from textual.binding import Binding
from textual.widgets import Footer

from .info_screen import ModuleInfoScreen
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
        overflow-y: auto;
    }

    #header-section {
        layout: vertical;
        align: center middle;
        width: 100%;
        height: auto;
        background: #16213e;
        border: round #0f3460;
        padding: 0 2;
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
        border: round #0f3460;
        color: #e0e0e0;
    }

    #middle_section {
        layout: vertical;
        align: center middle;
        width: 100%;
        height: auto;
        background: #16213e;
        border: round #0f3460;
        padding: 0 2;
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

    #section_header {
        color: #00d4ff;
        text-style: bold;
        text-align: center;
        width: 100%;
        padding: 0 2;
        background: #16213e;
        border: round #0f3460;
        height: auto;
        margin-bottom: 1;
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

    #button_section Horizontal Button {
        margin: 0 1;
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
        border: round #00d4ff;
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
        border: round #0f3460;
        color: #e0e0e0;
    }

    Button.success:hover {
        background: #00d4ff;
        color: #1a1a2e;
        border: round #00d4ff;
    }

    Button.default {
        min-width: 12;
        background: #16213e;
        border: round #0f3460;
        color: #666680;
    }

    Button.default:hover {
        color: #e0e0e0;
        border: round #00d4ff;
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
        "PriorityQueue": ["Heap"],
        "Algorithms": [],
    }

    FUN_FACTS = [
    "A stack follows LIFO — last in, first out.",
    "Your CPU uses a call stack to track function calls.",
    "Undo/redo in every text editor is just two stacks.",
    "DFS graph traversal can be implemented with a stack.",
    "Bad programmers worry about the code. Good programmers worry about data structures and their relationships. — Linus Torvalds",
    "Function call stack = the backbone of every program crash traceback you've ever read.",
    "A queue follows FIFO — first in, first out.",
    "OS schedulers use priority queues to manage processes.",
    "BFS graph traversal uses a queue under the hood.",
    "Circular queues avoid the wasted space of linear queues.",
    "Print spoolers, task schedulers, and bread lines all speak Queue.",
    "Premature optimization is the root of all evil. — Donald Knuth",
    "Linked lists excel at O(1) insertions and deletions.",
    "Your RAM is essentially a giant implicit linked structure.",
    "The Linux kernel uses doubly linked lists extensively.",
    "Linked lists trade random access for flexible memory use.",
    "Random numbers should not be generated with a method chosen at random. — Donald Knuth",
    "A pointer is just a memory address wearing a fancy hat.",
    "BSTs keep data sorted for O(log n) average lookup.",
    "A perfectly balanced BST is basically a binary search.",
    "In-order traversal of a BST gives sorted output.",
    "AVL trees self-balance to guarantee O(log n) worst case.",
    "The first BST was described by P.F. Windley in 1960.",
    "An algorithm must be seen to be believed. — Donald Knuth",
    "Red-black trees: because perfectly balanced is too much work.",
    "Heaps give O(1) access to the min or max element.",
    "Heapsort runs in O(n log n) with O(1) extra space.",
    "Python's heapq module is a min-heap by default.",
    "A heap is complete — every level filled left to right.",
    "If you optimize everything, you will always be unhappy. — Donald Knuth",
    "Dijkstra's algorithm uses a min-heap to find shortest paths fast.",
    "Arrays have O(1) access because memory is contiguous.",
    "Hash tables offer O(1) average lookup via hashing.",
    "The word 'algorithm' comes from Al-Khwarizmi's name.",
    "Graphs model everything: maps, social networks, compilers.",
    "A trie can autocomplete words in O(L) where L is length.",
    "Most interview problems reduce to 5 core DS patterns.",
    "Talk is cheap. Show me the code. — Linus Torvalds",
    "Computer Science is no more about computers than astronomy is about telescopes. — Edsger W. Dijkstra",
    "Programs are meant to be read by humans and only incidentally for computers to execute. — Donald Knuth",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. — Martin Fowler",
    "There are only two hard things in Computer Science: cache invalidation and naming things. — Phil Karlton",
    "If debugging is the process of removing software bugs, then programming must be the process of putting them in. — Edsger Dijkstra",
    "Given enough eyeballs, all bugs are shallow. — Linus Torvalds",
    "Intelligence is the ability to avoid doing work, yet getting the work done. — Linus Torvalds",
    "Science is what we understand well enough to explain to a computer. Art is everything else we do. — Donald Knuth",
    "A programming language is a tool that has a profound influence on our thinking habits. — Edsger Dijkstra",
    "Code never lies, comments sometimes do. — Ron Jeffries",
    "The best programs are written so that computing machines can perform them quickly and so that human beings can understand them clearly. — Donald Knuth",
    "Legacy code is code without tests. — Michael Feathers",
    "Simplicity is the ultimate sophistication. — Leonardo da Vinci",
    "Developers are drawn to complexity like moths to a flame, frequently with the same result. — Neal Ford",
    "Make illegal states unrepresentable. — Yaron Minsky",
    "First, solve the problem. Then, write the code. — John Johnson",
    "All models are wrong but some models are useful. — George Box",
    "Beware of bugs in the above code; I have only proved it correct, not tried it. — Donald Knuth",
    "Smart data structures and dumb code works a lot better than the other way around. — Eric S. Raymond",
    "I am not a visionary. I'm an engineer. I'm happy with the people who are wandering around looking at the stars but I am looking at the ground and I want to fix the pothole before I fall in. — Linus Torvalds",
    "Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program. — Linus Torvalds",
    "The enjoyment of one's tools is an essential ingredient of successful work. — Donald Knuth",
    "The computer is simply an instrument whose music is ideas. — Alan Kay",
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
            Static("Categories", id="section_header"),
            Container(id="button_section"),
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
    "   ┌─────┐\n   │  5  │  ← TOP\n   ├─────┤\n   │  3  │\n   ├─────┤\n   │  7  │\n   └─────┘",
    "    PUSH\n      ↓\n   ┌─────┐\n   │  A  │\n   ├─────┤\n   │  B  │\n   ├─────┤\n   │  C  │\n   └─────┘\n      ↑\n     POP",
    "   FRONT → ┌───┬───┬───┐ ← REAR\n          │ 1 │ 2 │ 3 │\n          └───┴───┴───┘",
    "  ENQUEUE →  ┌───┐ ┌───┐ ┌───┐\n             │ 7 │→│ 5 │→│ 3 │ → DEQUEUE\n             └───┘ └───┘ └───┘",
    "  NULL ←──┬──→ ┌───┐ ←──┬──→ ┌───┐\n          │    │ A │    │    │ B │\n          └──→ └───┘ ───→ └──→ └───┘ → NULL",
    "       5\n      / \\\n     3   7\n    / \\\n   1   4",
    "      [8]\n     /   \\\n   [3]   [10]\n   / \\\n [1] [6]",
    "       [1]\n      /   \\\n    [3]   [2]\n   / \\\n [7] [6]",
    "  ┌───┬───┬───┬───┐\n  │ 4 │ 2 │ 7 │ 1 │\n  └───┴───┴───┴───┘\n    0   1   2   3",
    "  ┌────┬────┬────┬────┐\n  │ 10 │ 20 │ 30 │ 40 │\n  └────┴────┴────┴────┘\n    0    1    2    3",
    "  ┌─────────┬─────────┐\n  │  key    │  value  │\n  ├─────────┼─────────┤\n  │  \"dsa\"  │   42    │\n  │  \"ai\"   │   99    │\n  └─────────┴─────────┘",
    "     A ─── B\n     │     │\n     C ─── D",
    "    (A)──→(B)──→(D)\n     ↓     ↓\n    (C)──→(E)",
    "       ROOT\n        │\n    ┌───┴───┐\n    ↓       ↓\n    a       b\n    │       │\n    ↓       ↓\n    p       a\n    │\n    ↓\n    p\n    │\n    ↓\n    l\n    │\n    ↓\n    e",
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
        self.query_one("#section_header").display = False

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
        self.query_one("#section_header").display = True
        if self.show_level_2:
            self._build_level_2_buttons(self.selected_category)
        else:
            self._build_level_1_buttons()

    def _show_level_1(self) -> None:
        self.show_level_2 = False
        self.selected_category = None
        self.query_one("#section_header").update("Categories")
        self._build_level_1_buttons()

    def _show_level_2(self, category: str) -> None:
        self.show_level_2 = True
        self.selected_category = category
        self.query_one("#section_header").update("Modules")
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

        if button_id == "category_Algorithms":
            self.notify("Sorting & Searching algorithms coming in a future release!", severity="information")
            return

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
            "Heap": "heap",
        }

        binary_name = module_mapping.get(module_name, module_name.lower().replace(" ", ""))

        try:
            import sys
            sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
            from bridge import get_binary
            import platform
            binary_path = get_binary(binary_name)
            os_path = platform.system().lower()
        except Exception:
            binary_path = f"./TUI/bins/{os_path}/{binary_name}"

        if os.path.exists(binary_path):
            self.app.push_screen(ModuleInfoScreen(binary_name, module_name))
        else:
            self.notify(f"Module '{module_name}' not yet implemented", severity="warning")

    def action_quit(self) -> None:
        self.app.exit()