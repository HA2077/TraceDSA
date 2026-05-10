from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static, Button, Input, Label
from textual.screen import Screen
from textual.binding import Binding
from rich.text import Text
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from bridge import DSBridge
from widgets.ascii_array import ASCIIArray
from widgets.ascii_tree import ASCII2DTree
from widgets.ascii_heap import ASCIIHeap
from widgets.ops_log import OpsLog


class TraceWindow(Screen):
    
    BINDINGS = [
        Binding("escape", "go_back", "Back"),
        Binding("backspace", "go_back", "Back"),
    ]
    
    def __init__(self, binary_name: str, display_name: str):
        super().__init__()
        self.binary_name = binary_name
        self.display_name = display_name
        self.bridge = None
        self.ascii_widget = None
        self.log_widget = None
        self.input_field = None
        
        self.operation_buttons = {
            "stack": [
                ("PUSH [value]", "push_btn", "PUSH"),
                ("POP", "pop_btn", "POP"),
                ("PEEK", "peek_btn", "PEEK"),
                ("PRINT", "print_btn", "PRINT"),
                ("CLEAR", "clear_btn", "CLEAR"),
            ],
            "queue": [
                ("ENQUEUE [value]", "enqueue_btn", "ENQUEUE"),
                ("DEQUEUE", "dequeue_btn", "DEQUEUE"),
                ("PEEK", "peek_btn", "PEEK"),
                ("PRINT", "print_btn", "PRINT"),
                ("CLEAR", "clear_btn", "CLEAR"),
            ],
            "bst": [
                ("INSERT [value]", "insert_btn", "INSERT"),
                ("REMOVE [value]", "remove_btn", "REMOVE"),
                ("FIND [value]", "find_btn", "FIND"),
                ("INORDER", "inorder_btn", "INORDER"),
                ("PREORDER", "preorder_btn", "PREORDER"),
                ("POSTORDER", "postorder_btn", "POSTORDER"),
                ("CLEAR", "clear_btn", "CLEAR"),
            ],
            "heap": [
                ("ENQUEUE [value]", "enqueue_btn", "ENQUEUE"),
                ("DEQUEUE MIN", "dequeue_min_btn", "DEQUEUE MIN"),
                ("PEEK MIN", "peek_min_btn", "PEEK MIN"),
                ("PRINT", "print_btn", "PRINT"),
                ("CLEAR", "clear_btn", "CLEAR"),
            ],
            "default": [
                ("OP [value]", "op_btn", "OP"),
                ("CLEAR", "clear_btn", "CLEAR"),
            ]
        }
    
    def compose(self) -> ComposeResult:
        yield Container(
            Container(
                Button("← Back", id="back_button", variant="default"),
                Static(self.display_name.upper(), id="module_name"),
                id="trace_header"
            ),
            
            # Main content: ASCII visualization and operation log
            Horizontal(
                Container(
                    # Will be replaced with actual widget in on_mount
                    Static("Initializing...", id="ascii_placeholder"),
                    id="ascii_panel"
                ),
                
                Container(
                    Static("Operation Log", id="log_header"),
                    # Will be replaced with actual widget in on_mount
                    Static("", id="log_content"),
                    id="log_panel"
                ),
                id="main_content"
            ),
            
            # Bottom bar: Operation buttons
            Container(
                id="button_container"
            ),
            
            id="trace_window_container"
        )
    
    def on_mount(self) -> None:
        try:
            self.bridge = DSBridge(self.binary_name)
        except Exception as e:
            self.notify(f"Failed to connect to {self.binary_name}: {e}", severity="error")
            self.app.pop_screen()
            return
        
        # Get references to containers
        ascii_container = self.query_one("#ascii_panel")
        log_container = self.query_one("#log_panel")
        
        # Clear the containers and mount our actual widgets
        ascii_container.remove_children()
        log_container.remove_children()
        
        # Initialize and mount the appropriate ASCII widget based on binary type
        if self.binary_name in ["stack", "stackll", "queue", "queuell", "circqueue"]:
            self.ascii_widget = ASCIIArray(title=self.display_name)
            ascii_container.mount(self.ascii_widget)
        elif self.binary_name == "bst":
            self.ascii_widget = ASCII2DTree(title=self.display_name)
            ascii_container.mount(self.ascii_widget)
        elif self.binary_name == "heap":
            # For heap, we'll determine min/max from the display name
            heap_type = "min" if "Min" in self.display_name else "max"
            self.ascii_widget = ASCIIHeap(title=self.display_name, heap_type=heap_type)
            ascii_container.mount(self.ascii_widget)
        else:
            # Fallback to generic array widget
            self.ascii_widget = ASCIIArray(title=self.display_name)
            ascii_container.mount(self.ascii_widget)
        
        self.log_widget = OpsLog()
        log_container.mount(self.log_widget)
        self.input_field = None  # Will be set when needed
        
        self._build_operation_buttons()
        
        self._clear_log()
        self._log_operation(f"Connected to {self.display_name}")
        
        if self.binary_name in ["stack", "stackll", "queue", "queuell", "circqueue"]:
            self.ascii_widget.update_data([])  # Empty array
        elif self.binary_name == "bst":
            self.ascii_widget.update_tree([])  # Empty tree
        elif self.binary_name == "heap":
            self.ascii_widget.update_heap([])  # Empty heap
    
    def _build_operation_buttons(self) -> None:
        """Build operation buttons based on the binary type"""
        container = self.query_one("#button_container")
        container.remove_children()
        
        # Get button configuration for this binary type
        button_configs = self.operation_buttons.get(
            self.binary_name, 
            self.operation_buttons["default"]
        )
        
        buttons = []
        for label, button_id, command_prefix in button_configs:
            if "[value]" in label:
                input_id = button_id.replace("_btn", "_input")
                btn = Button(label.replace("[value]", ""), id=button_id)
                buttons.append(("input", input_id, label, btn))
            else:
                btn = Button(label, id=button_id)
                buttons.append(("button", button_id, label, btn))
        
        for i in range(0, len(buttons), 3):
            group = buttons[i:i+3]
            button_widgets = []
            
            for btn_type, btn_id, btn_label, btn in group:
                if btn_type == "input":
                    input_field = Input(placeholder="value", id=btn_id)
                    container.mount(Horizontal(input_field, btn, id=f"{btn_id}_group"))
                    if "push" in btn_id.lower() or "enqueue" in btn_id.lower() or "insert" in btn_id.lower():
                        self.input_field = input_field  # Store reference for Enter key
                else:
                    # Regular button
                    container.mount(btn)
                    button_widgets.append(btn)
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        
        if button_id == "back_button":
            self.action_go_back()
            return
        
        # Find the command associated with this button
        command = self._get_command_for_button(button_id)
        if command:
            self._execute_command(command)
    
    def _get_command_for_button(self, button_id: str) -> str:
        command_map = {
            "back_button": "EXIT",  # Handled separately
            
            # Stack operations
            "push_input": lambda: f"PUSH {self.query_one('#push_input').value}",
            "pop_btn": "POP",
            "peek_btn": "PEEK",
            "print_btn": "PRINT",
            "clear_btn": lambda: self._clear_and_reset(),
            
            # Queue operations
            "enqueue_input": lambda: f"ENQUEUE {self.query_one('#enqueue_input').value}",
            "dequeue_btn": "DEQUEUE",
            
            # BST operations
            "insert_input": lambda: f"INSERT {self.query_one('#insert_input').value}",
            "remove_input": lambda: f"REMOVE {self.query_one('#remove_input').value}",
            "find_input": lambda: f"FIND {self.query_one('#find_input').value}",
            "inorder_btn": "INORDER",
            "preorder_btn": "PREORDER",
            "postorder_btn": "POSTORDER",
            
            # Heap operations
            "dequeue_min_btn": "DEQUEUE MIN",
            "peek_min_btn": "PEEK MIN",
        }
        
        if button_id in command_map:
            mapping = command_map[button_id]
            if callable(mapping):
                return mapping()
            return mapping
        return None
    
    def _clear_and_reset(self) -> str:
        self._clear_log()
        self._log_operation(f"Cleared {self.display_name}")
        self._update_ascii_art("[]")
        self.bridge.close()
        self.bridge = DSBridge(self.binary_name)
        return ""  # No command to send
    
    def _execute_command(self, command: str) -> None:
        """Execute a command and update the display"""
        if not command:  # Special case like clear
            return
            
        try:
            response = self.bridge.send(command)
            
            self._log_operation(f"> {command}")
            self._log_operation(f"< {response}")
            
            self._update_ascii_art_from_response(response)
            
            # Clear input field if applicable
            if self.input_field and self.input_field.has_focus:
                self.input_field.value = ""
                
        except Exception as e:
            self._log_operation(f"ERROR: {str(e)}")
            self.notify(f"Command failed: {str(e)}", severity="error")
    
    def _log_operation(self, message: str) -> None:
        if self.log_widget:
            self.log_widget.add_entry(message)
    
    def _clear_log(self) -> None:
        if self.log_widget:
            self.log_widget.clear()
    
    def _update_ascii_art(self, art: str) -> None:
        if self.ascii_widget:
            # For our custom widgets, we need to update their internal data and refresh
            if hasattr(self.ascii_widget, 'update_data'):
                # ASCIIArray widget
                try:
                    # Try to parse as array data like "[1 2 3]"
                    if art.startswith('[') and art.endswith(']'):
                        content = art[1:-1].strip()
                        if content:
                            data = [int(x.strip()) for x in content.split() if x.strip()]
                            self.ascii_widget.update_data(data)
                        else:
                            self.ascii_widget.update_data([])
                    else:
                        # Just update with the raw string for now
                        self.ascii_widget.update_data([])
                except ValueError:
                    # If parsing fails, keep current data
                    pass
            elif hasattr(self.ascii_widget, 'update_tree'):
                # ASCII2DTree widget
                try:
                    # Try to parse as tree traversal data
                    if art.startswith('[') and art.endswith(']'):
                        content = art[1:-1].strip()
                        if content:
                            data = [int(x.strip()) for x in content.split() if x.strip()]
                            self.ascii_widget.update_tree(data)
                        else:
                            self.ascii_widget.update_tree([])
                    else:
                        self.ascii_widget.update_tree([])
                except ValueError:
                    self.ascii_widget.update_tree([])
            elif hasattr(self.ascii_widget, 'update_heap'):
                # ASCIIHeap widget
                try:
                    # Try to parse as heap array data
                    if art.startswith('[') and art.endswith(']'):
                        content = art[1:-1].strip()
                        if content:
                            data = [int(x.strip()) for x in content.split() if x.strip()]
                            self.ascii_widget.update_heap(data)
                        else:
                            self.ascii_widget.update_heap([])
                    else:
                        self.ascii_widget.update_heap([])
                except ValueError:
                    self.ascii_widget.update_heap([])
            else:
                # Fallback - just refresh the widget
                self.ascii_widget.refresh()
    
    def _update_ascii_art_from_response(self, response: str) -> None:
        """Update ASCII art based on binary response"""
        if response.startswith("OK"):
            # Extract meaningful part of response for display
            if ": [" in response:
                # Format like "OK Stack: [1 2 3]"
                content = response.split(": [", 1)[1].rstrip("]")
                if content.strip():
                    self._update_ascii_art(f"[{content}]")
                else:
                    self._update_ascii_art("[]")
            elif "Forward:" in response and "Backward:" in response:
                # Doubly linked list format
                self._update_ascii_art(response[3:])  # Remove "OK "
            elif "In-order:" in response or "Pre-order:" in response or "Post-order:" in response:
                # BST traversals
                self._update_ascii_art(response[3:])  # Remove "OK "
            elif "Min-Heap:" in response or "Max-Heap:" in response:
                # Heap format
                self._update_ascii_art(response[3:])  # Remove "OK "
            else:
                # Generic OK response
                self._update_ascii_art(response[3:].strip() or "[]")
        elif response.startswith("ERROR"):
            # Show error in ASCII art area
            self._update_ascii_art(f"ERROR: {response[6:]}")
        else:
            # Unexpected response format
            self._update_ascii_art(f"? {response}")
    
    def action_go_back(self) -> None:
        if self.bridge:
            self.bridge.close()
        self.app.pop_screen()
    
    def on_key(self, event) -> None:
        if event.key == "enter" and self.input_field and self.input_field.has_focus:
            focused_id = self.input_field.id
            if focused_id == "push_input":
                self.app.post_message(self.__class__.ButtonPressed(self.query_one("#push_btn")))
            elif focused_id == "enqueue_input":
                self.app.post_message(self.__class__.ButtonPressed(self.query_one("#enqueue_btn")))
            elif focused_id == "insert_input":
                self.app.post_message(self.__class__.ButtonPressed(self.query_one("#insert_btn")))
            elif focused_id == "remove_input":
                self.app.post_message(self.__class__.ButtonPressed(self.query_one("#remove_btn")))
            elif focused_id == "find_input":
                self.app.post_message(self.__class__.ButtonPressed(self.query_one("#find_btn")))
            # Add more as needed


from bridge import DSBridge