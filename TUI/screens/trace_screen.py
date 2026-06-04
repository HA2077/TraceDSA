from cProfile import label

from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Static, Button, Input
from textual.screen import Screen
from textual.binding import Binding
from textual.widgets import Footer

import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from bridge import DSBridge
from widgets.ascii_array import ASCIIArray
from widgets.ascii_tree import ASCIIBranchTree
from widgets.ascii_heap import ASCIIHeap
from widgets.ops_log import OpsLog
from .help_screen import HelpScreen


class TraceWindow(Screen):

    BINDINGS = [
        Binding("escape", "go_back", "Back"),
        Binding("h", "show_help", "Help"),
        Binding("?", "show_help", "Help"),
    ]

    _FOCUS_DESCRIPTIONS = {
        "back_button": "Return to the main menu",
        "push_btn": "PUSH <value> — Add to top of stack",
        "pop_btn": "POP — Remove and return the top element",
        "peek_btn": "PEEK — View the top element without removing it",
        "print_btn": "PRINT — Display the current state",
        "clear_btn": "CLEAR — Remove all elements",
        "enqueue_btn": "ENQUEUE <value> — Add to the back of the queue",
        "dequeue_btn": "DEQUEUE — Remove and return the front element",
        "insert_btn": "INSERT <value> — Insert into the tree",
        "remove_btn": "REMOVE <value> — Remove from the tree",
        "find_btn": "FIND <value> — Search for a value in the tree",
        "inorder_btn": "INORDER — In-order traversal (sorted)",
        "preorder_btn": "PREORDER — Pre-order traversal (root first)",
        "postorder_btn": "POSTORDER — Post-order traversal (children first)",
        "insert_start_btn": "INSERT_START <value> — Insert at the beginning",
        "insert_end_btn": "INSERT_END <value> — Insert at the end",
        "del_start_btn": "DELETE_START — Remove the first element",
        "del_end_btn": "DELETE_END — Remove the last element",
        "delete_val_btn": "DELETE_VAL <value> — Remove a node by its value",
        "enqueue_min_btn": "ENQUEUE_MIN <value> — Insert into min-heap",
        "dequeue_min_btn": "DEQUEUE_MIN — Extract the minimum element",
        "peek_min_btn": "PEEK_MIN — View the minimum element",
        "print_min_btn": "PRINT_MIN — Display min-heap contents",
        "enqueue_max_btn": "ENQUEUE_MAX <value> — Insert into max-heap",
        "dequeue_max_btn": "DEQUEUE_MAX — Extract the maximum element",
        "peek_max_btn": "PEEK_MAX — View the maximum element",
        "print_max_btn": "PRINT_MAX — Display max-heap contents",
    }

    _STATE_COMMANDS = {
        "PUSH", "POP", "ENQUEUE", "DEQUEUE",
        "INSERT", "INSERT_START", "INSERT_END",
        "DELETE_START", "DELETE_END", "DELETE_VAL",
        "ENQUEUE_MIN", "DEQUEUE_MIN", "ENQUEUE_MAX", "DEQUEUE_MAX",
        "PRINT", "PRINT_MIN", "PRINT_MAX", "CLEAR",
    }

    MODULE_CONFIGS = {
        "stack": {
            "ascii_type": "array",
            "buttons": [
                ("PUSH", "push_btn", True),
                ("POP", "pop_btn", False),
                ("PEEK", "peek_btn", False),
                ("PRINT", "print_btn", False),
                ("CLEAR", "clear_btn", False),
            ],
        },
        "stackll": {
            "ascii_type": "array",
            "buttons": [
                ("PUSH", "push_btn", True),
                ("POP", "pop_btn", False),
                ("PEEK", "peek_btn", False),
                ("PRINT", "print_btn", False),
                ("CLEAR", "clear_btn", False),
            ],
        },
        "queue": {
            "ascii_type": "array",
            "buttons": [
                ("ENQUEUE", "enqueue_btn", True),
                ("DEQUEUE", "dequeue_btn", False),
                ("PEEK", "peek_btn", False),
                ("PRINT", "print_btn", False),
                ("CLEAR", "clear_btn", False),
            ],
        },
        "queuell": {
            "ascii_type": "array",
            "buttons": [
                ("ENQUEUE", "enqueue_btn", True),
                ("DEQUEUE", "dequeue_btn", False),
                ("PEEK", "peek_btn", False),
                ("PRINT", "print_btn", False),
                ("CLEAR", "clear_btn", False),
            ],
        },
        "circqueue": {
            "ascii_type": "array",
            "buttons": [
                ("ENQUEUE", "enqueue_btn", True),
                ("DEQUEUE", "dequeue_btn", False),
                ("PEEK", "peek_btn", False),
                ("PRINT", "print_btn", False),
                ("CLEAR", "clear_btn", False),
            ],
        },
        "ll": {
            "ascii_type": "linked",
            "buttons": [
                ("INSERT_START", "insert_start_btn", True),
                ("INSERT_END", "insert_end_btn", True),
                ("DELETE_START", "del_start_btn", False),
                ("DELETE_END", "del_end_btn", False),
                ("DELETE_VAL", "delete_val_btn", True),
                ("PRINT", "print_btn", False),
                ("CLEAR", "clear_btn", False),
            ],
        },
        "dll": {
            "ascii_type": "doubly",
            "buttons": [
                ("INSERT_START", "insert_start_btn", True),
                ("INSERT_END", "insert_end_btn", True),
                ("DELETE_START", "del_start_btn", False),
                ("DELETE_END", "del_end_btn", False),
                ("PRINT", "print_btn", False),
                ("CLEAR", "clear_btn", False),
            ],
        },
        "bst": {
            "ascii_type": "tree",
            "buttons": [
                ("INSERT", "insert_btn", True),
                ("REMOVE", "remove_btn", True),
                ("FIND", "find_btn", True),
                ("INORDER", "inorder_btn", False),
                ("PREORDER", "preorder_btn", False),
                ("POSTORDER", "postorder_btn", False),
                ("PRINT", "print_btn", False),
                ("CLEAR", "clear_btn", False),
            ],
        },
        "heap": {
            "ascii_type": "heap",
            "buttons": [
                ("ENQUEUE_MIN", "enqueue_min_btn", True),
                ("DEQUEUE_MIN", "dequeue_min_btn", False),
                ("PEEK_MIN", "peek_min_btn", False),
                ("PRINT_MIN", "print_min_btn", False),
                ("ENQUEUE_MAX", "enqueue_max_btn", True),
                ("DEQUEUE_MAX", "dequeue_max_btn", False),
                ("PEEK_MAX", "peek_max_btn", False),
                ("PRINT_MAX", "print_max_btn", False),
                ("CLEAR", "clear_btn", False),
            ],
        },
    }

    def __init__(self, binary_name: str, display_name: str):
        super().__init__()
        self.binary_name = binary_name
        self.display_name = display_name
        self.bridge = None
        self.ascii_widget = None
        self.log_widget = None
        self.input_fields = {}
        self._active_input = None

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Container(
            Container(
                Button("← Back", id="back_button", variant="default"),
                Static(self.display_name.upper(), id="module_name"),
                id="trace_header"
            ),
            Horizontal(
                Container(
                    Static("Loading...", id="ascii_placeholder"),
                    id="ascii_panel"
                ),
                Container(
                    Static("Operation Log", id="log_header"),
                    id="log_panel"
                ),
                id="main_content"
            ),
            Container(id="button_container"),
            Static("", id="status_bar"),
            id="trace_window_container"
        )

    def action_show_help(self) -> None:
        self.app.push_screen(HelpScreen())

    def on_mount(self) -> None:
        bridge = self.app.get_bridge(self.binary_name)
        if bridge:
            self.bridge = bridge
        else:
            try:
                self.bridge = DSBridge(self.binary_name)
            except Exception as e:
                self.notify(f"Failed to connect to {self.binary_name}: {e}", severity="error")
                self.app.pop_screen()
                return

        ascii_container = self.query_one("#ascii_panel")
        log_container = self.query_one("#log_panel")

        ascii_container.remove_children()
        log_container.remove_children()

        config = self.MODULE_CONFIGS.get(self.binary_name, self.MODULE_CONFIGS.get("stack"))
        ascii_type = config["ascii_type"]

        if ascii_type in ("array", "linked", "doubly"):
            self.ascii_widget = ASCIIArray(title=self.display_name)
        elif ascii_type == "tree":
            self.ascii_widget = ASCIIBranchTree(title=self.display_name)
        elif ascii_type == "heap":
            heap_type = "min" if "Min" in self.display_name else "max"
            self.ascii_widget = ASCIIHeap(title=self.display_name, heap_type=heap_type)
        else:
            self.ascii_widget = ASCIIArray(title=self.display_name)

        ascii_container.mount(self.ascii_widget)

        self.log_widget = OpsLog()
        log_container.mount(self.log_widget)

        self._build_operation_buttons()

        self.log_widget.add_entry(f"Connected to {self.display_name}")

        if ascii_type in ("array", "linked", "doubly"):
            self.ascii_widget.update_data([])
        elif ascii_type == "tree":
            self.ascii_widget.update_tree([])
        elif ascii_type == "heap":
            self.ascii_widget.update_heap([])

        try:
            first_input = self.query_one("Input", expect_type=Input)
            first_input.focus()
        except Exception:
            pass

        self.query_one("#status_bar").update(
            "Tab to navigate, Enter to execute, Escape to go back"
        )

    def on_widget_focused(self, event) -> None:
        widget = event.widget
        sb = self.query_one("#status_bar")
        if isinstance(widget, Button):
            desc = self._FOCUS_DESCRIPTIONS.get(widget.id)
            sb.update(desc if desc else "Tab to navigate, Enter to execute, Escape to go back")
        elif isinstance(widget, Input):
            sb.update("Enter a numeric value")

    def _build_operation_buttons(self) -> None:
        container = self.query_one("#button_container")
        container.remove_children()

        config = self.MODULE_CONFIGS.get(self.binary_name)
        if not config:
            return

        button_specs = config["buttons"]

        for label, btn_id, needs_input in button_specs:
            if needs_input:
                input_id = f"{btn_id}_input"
                input_widget = Input(placeholder="value", id=input_id)
                btn = Button(label, id=btn_id)
                self.input_fields[btn_id] = input_widget
                container.mount(input_widget)
                container.mount(btn)
            else:
                btn = Button(label, id=btn_id)
                container.mount(btn)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id

        if button_id == "back_button":
            self.action_go_back()
            return

        command = self._build_command(button_id)
        if command:
            self._execute_command(command)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        btn_id = event.input.id.replace("_input", "")
        command = self._build_command(btn_id)
        if command:
            self._execute_command(command)

    def _build_command(self, button_id: str) -> str | None:
        config = self.MODULE_CONFIGS.get(self.binary_name)
        if not config:
            return None

        for label, btn_id, needs_input in config["buttons"]:
            if btn_id == button_id:
                if needs_input:
                    input_widget = self.input_fields.get(btn_id)
                    if input_widget:
                        value = input_widget.value.strip()
                        if not value:
                            self.notify("Please enter a value", severity="warning")
                            input_widget.focus()
                            return None
                        if not value.lstrip('-').isdigit() or (value.startswith('-') and len(value) == 1):
                            self.notify(f"Numbers only — got '{value}'", severity="error")
                            input_widget.value = ""
                            input_widget.focus()
                            return None
                        return f"{label} {value}"
                    return None
                else:
                    return label

        return None

    def _execute_command(self, command: str) -> None:
        if not command:
            return

        if not self.bridge or not self.bridge.is_alive():
            self.log_widget.add_entry("ERROR: Connection to binary lost")
            self.notify("Connection lost. Press Escape to go back.", severity="error")
            return

        try:
            response = self.bridge.send(command)

            self.log_widget.add_entry(f"> {command}")
            self.log_widget.add_entry(f"< {response}")

            if command.split()[0] in self._STATE_COMMANDS:
                self._update_ascii_from_response(response)

            if command.split()[0] in ("PUSH", "ENQUEUE", "INSERT", "INSERT_START", "INSERT_END", "ENQUEUE_MIN", "ENQUEUE_MAX", "REMOVE", "FIND", "DELETE_VAL"):
                for inp in self.input_fields.values():
                    inp.value = ""

        except Exception as e:
            self.log_widget.add_entry(f"ERROR: {str(e)}")
            self.notify(f"Command failed: {str(e)}", severity="error")

    def _update_ascii_from_response(self, response: str) -> None:
        if response.startswith("ERROR"):
            return

        if not response.startswith("OK"):
            return

        content = response[3:].strip()

        ascii_type = self.MODULE_CONFIGS.get(self.binary_name, {}).get("ascii_type", "array")

        if ascii_type in ("array", "linked", "doubly"):
            self._update_array_widget(content)
        elif ascii_type == "tree":
            self._update_tree_widget(content)
        elif ascii_type == "heap":
            self._update_heap_widget(content)

    def _update_array_widget(self, content: str) -> None:
        if not self.ascii_widget:
            return

        if "Forward:" in content and "Backward:" in content:
            forward_part = content.split("Forward:")[1].split("Backward:")[0].strip("[] ")
            if forward_part.strip():
                try:
                    cleaned = forward_part.replace("<->", " ")
                    data = [int(x.strip()) for x in cleaned.split() if x.strip() and x.strip().isdigit()]
                    self.ascii_widget.update_data(data)
                except ValueError:
                    pass
            else:
                self.ascii_widget.update_data([])
            return

        if "Linked List:" in content:
            list_part = content.split("Linked List:")[1].strip("[] ")
            if list_part.strip():
                try:
                    cleaned = list_part.replace("->", " ").replace("<->", " ")
                    data = [int(x.strip()) for x in cleaned.split() if x.strip() and x.strip().isdigit()]
                    self.ascii_widget.update_data(data)
                except ValueError:
                    pass
            else:
                self.ascii_widget.update_data([])
            return

        if "[" in content and "]" in content:
            start = content.index("[") + 1
            end = content.rindex("]")
            inner = content[start:end].strip()
            if inner:
                try:
                    cleaned = inner.replace("->", " ").replace("<->", " ")
                    data = [int(x.strip()) for x in cleaned.split() if x.strip() and x.strip().lstrip("-").isdigit()]
                    self.ascii_widget.update_data(data)
                except ValueError:
                    pass
            else:
                self.ascii_widget.update_data([])
        else:
            self.ascii_widget.update_data([])

    def _update_tree_widget(self, content: str) -> None:
        if not self.ascii_widget:
            return

        if "[" in content and "]" in content:
            start = content.index("[") + 1
            end = content.rindex("]")
            inner = content[start:end].strip()
            if inner:
                try:
                    cleaned = inner.replace("->", " ").replace("<->", " ")
                    data = [int(x.strip()) for x in cleaned.split() if x.strip() and x.strip().lstrip("-").isdigit()]
                    self.ascii_widget.update_tree(data)
                except ValueError:
                    self.ascii_widget.update_tree([])
            else:
                self.ascii_widget.update_tree([])
        else:
            self.ascii_widget.update_tree([])

    def _update_heap_widget(self, content: str) -> None:
        if not self.ascii_widget:
            return

        if "Min-Heap:" in content or "Max-Heap:" in content:
            if "Min-Heap:" in content:
                self.ascii_widget.heap_type = "min"
                part = content.split("Min-Heap:")[1]
            else:
                self.ascii_widget.heap_type = "max"
                part = content.split("Max-Heap:")[1]

            part = part.strip("[] ")
            if part:
                try:
                    cleaned = part.replace("->", " ").replace("<->", " ")
                    data = [int(x.strip()) for x in cleaned.split() if x.strip() and x.strip().lstrip("-").isdigit()]
                    self.ascii_widget.update_heap(data)
                except ValueError:
                    self.ascii_widget.update_heap([])
            else:
                self.ascii_widget.update_heap([])
        elif "[" in content and "]" in content:
            start = content.index("[") + 1
            end = content.rindex("]")
            inner = content[start:end].strip()
            if inner:
                try:
                    cleaned = inner.replace("->", " ").replace("<->", " ")
                    data = [int(x.strip()) for x in cleaned.split() if x.strip() and x.strip().lstrip("-").isdigit()]
                    self.ascii_widget.update_heap(data)
                except ValueError:
                    self.ascii_widget.update_heap([])
            else:
                self.ascii_widget.update_heap([])
        else:
            self.ascii_widget.update_heap([])

    def action_go_back(self) -> None:
        if self.bridge:
            self.bridge.close()
        self.app.pop_screen()