from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static, Button, Input, Label
from textual.screen import Screen
from textual.binding import Binding
from rich.text import Text
import os


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
                ("PUSH [value]", "push-input", "PUSH"),
                ("POP", "pop-btn", "POP"),
                ("PEEK", "peek-btn", "PEEK"),
                ("PRINT", "print-btn", "PRINT"),
                ("CLEAR", "clear-btn", "CLEAR"),
            ],
            "queue": [
                ("ENQUEUE [value]", "enqueue-input", "ENQUEUE"),
                ("DEQUEUE", "dequeue-btn", "DEQUEUE"),
                ("PEEK", "peek-btn", "PEEK"),
                ("PRINT", "print-btn", "PRINT"),
                ("CLEAR", "clear-btn", "CLEAR"),
            ],
            "bst": [
                ("INSERT [value]", "insert-input", "INSERT"),
                ("REMOVE [value]", "remove-input", "REMOVE"),
                ("FIND [value]", "find-input", "FIND"),
                ("INORDER", "inorder-btn", "INORDER"),
                ("PREORDER", "preorder-btn", "PREORDER"),
                ("POSTORDER", "postorder-btn", "POSTORDER"),
                ("CLEAR", "clear-btn", "CLEAR"),
            ],
            "heap": [
                ("ENQUEUE [value]", "enqueue-input", "ENQUEUE"),
                ("DEQUEUE MIN", "dequeue-min-btn", "DEQUEUE MIN"),
                ("PEEK MIN", "peek-min-btn", "PEEK MIN"),
                ("PRINT", "print-btn", "PRINT"),
                ("CLEAR", "clear-btn", "CLEAR"),
            ],
            "default": [
                ("OP [value]", "op-input", "OP"),
                ("CLEAR", "clear-btn", "CLEAR"),
            ]
        }
    
    def compose(self) -> ComposeResult:
        yield Container(
            Container(
                Button("← Back", id="back-button", variant="default"),
                Static(self.display_name.upper(), id="module-name"),
                id="trace-header"
            ),
            
            # Main content: ASCII visualization and operation log
            Horizontal(
                # Left panel: Live ASCII art visualization
                Container(
                    Static("~live ASCII art~", id="ascii-placeholder"),
                    id="ascii-panel"
                ),
                
                # Right panel: Operation log
                Container(
                    Static("Operation Log", id="log-header"),
                    Static("", id="log-content"),
                    id="log-panel"
                ),
                id="main-content"
            ),
            
            # Bottom bar: Operation buttons
            Container(
                id="button-container"
            ),
            
            id="trace-window-container"
        )
    
    def on_mount(self) -> None:
        try:
            self.bridge = DSBridge(self.binary_name)
        except Exception as e:
            self.notify(f"Failed to connect to {self.binary_name}: {e}", severity="error")
            self.app.pop_screen()
            return
        
        # Get references to widgets
        self.ascii_widget = self.query_one("#ascii-placeholder")
        self.log_widget = self.query_one("#log-content")
        self.input_field = None  # Will be set when needed
        
        # Build operation buttons based on binary type
        self._build_operation_buttons()
        
        # Clear log and show initial state
        self._clear_log()
        self._log_operation(f"Connected to {self.display_name}")
        self._update_ascii_art("Initializing...")
    
    def _build_operation_buttons(self) -> None:
        """Build operation buttons based on the binary type"""
        container = self.query_one("#button-container")
        container.remove_children()
        
        # Get button configuration for this binary type
        button_configs = self.operation_buttons.get(
            self.binary_name, 
            self.operation_buttons["default"]
        )
        
        # Create buttons in groups
        buttons = []
        for label, button_id, command_prefix in button_configs:
            if "[value]" in label:
                # This is an input field + button combo
                input_id = button_id.replace("-btn", "-input")
                btn = Button(label.replace("[value]", ""), id=button_id)
                buttons.append(("input", input_id, label, btn))
            else:
                # Regular button
                btn = Button(label, id=button_id)
                buttons.append(("button", button_id, label, btn))
        
        for i in range(0, len(buttons), 3):
            group = buttons[i:i+3]
            button_widgets = []
            
            for btn_type, btn_id, btn_label, btn in group:
                if btn_type == "input":
                    # Create input field + button pair
                    input_field = Input(placeholder="value", id=btn_id)
                    container.mount(Horizontal(input_field, btn, id=f"{btn_id}-group"))
                    if "push" in btn_id.lower() or "enqueue" in btn_id.lower() or "insert" in btn_id.lower():
                        self.input_field = input_field  # Store reference for Enter key
                else:
                    # Regular button
                    container.mount(btn)
                    button_widgets.append(btn)
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses"""
        button_id = event.button.id
        
        if button_id == "back-button":
            self.action_go_back()
            return
        
        # Find the command associated with this button
        command = self._get_command_for_button(button_id)
        if command:
            self._execute_command(command)
    
    def _get_command_for_button(self, button_id: str) -> str:
        """Get the command string for a button ID"""
        # Map button IDs to commands
        command_map = {
            "back-button": "EXIT",  # Handled separately
            
            # Stack operations
            "push-input": lambda: f"PUSH {self.query_one('#push-input').value}",
            "pop-btn": "POP",
            "peek-btn": "PEEK",
            "print-btn": "PRINT",
            "clear-btn": lambda: self._clear_and_reset(),
            
            # Queue operations
            "enqueue-input": lambda: f"ENQUEUE {self.query_one('#enqueue-input').value}",
            "dequeue-btn": "DEQUEUE",
            
            # BST operations
            "insert-input": lambda: f"INSERT {self.query_one('#insert-input').value}",
            "remove-input": lambda: f"REMOVE {self.query_one('#remove-input').value}",
            "find-input": lambda: f"FIND {self.query_one('#find-input').value}",
            "inorder-btn": "INORDER",
            "preorder-btn": "PREORDER",
            "postorder-btn": "POSTORDER",
            
            # Heap operations
            "dequeue-min-btn": "DEQUEUE MIN",
            "peek-min-btn": "PEEK MIN",
        }
        
        if button_id in command_map:
            mapping = command_map[button_id]
            if callable(mapping):
                return mapping()
            return mapping
        return None
    
    def _clear_and_reset(self) -> str:
        """Clear the data structure and return command"""
        self._clear_log()
        self._log_operation(f"Cleared {self.display_name}")
        self._update_ascii_art("[]")
        # Reconnect bridge to reset state
        self.bridge.close()
        self.bridge = DSBridge(self.binary_name)
        return ""  # No command to send
    
    def _execute_command(self, command: str) -> None:
        """Execute a command and update the display"""
        if not command:  # Special case like clear
            return
            
        try:
            # Send command to binary
            response = self.bridge.send(command)
            
            # Log the operation
            self._log_operation(f"> {command}")
            self._log_operation(f"< {response}")
            
            # Update ASCII art based on response
            self._update_ascii_art_from_response(response)
            
            # Clear input field if applicable
            if self.input_field and self.input_field.has_focus:
                self.input_field.value = ""
                
        except Exception as e:
            self._log_operation(f"ERROR: {str(e)}")
            self.notify(f"Command failed: {str(e)}", severity="error")
    
    def _log_operation(self, message: str) -> None:
        """Add a message to the operation log"""
        if self.log_widget:
            current_content = self.log_widget.renderable
            if hasattr(current_content, 'plain'):
                current_text = current_content.plain
            else:
                current_text = str(current_content) if current_content else ""
            
            new_text = f"{current_text}\n{message}" if current_text else message
            self.log_widget.update(new_text)
            
            # Auto-scroll to bottom (simulated by ensuring last lines are visible)
            # In a real implementation, we'd use a RichLog or similar widget
    
    def _clear_log(self) -> None:
        """Clear the operation log"""
        if self.log_widget:
            self.log_widget.update("")
    
    def _update_ascii_art(self, art: str) -> None:
        """Update the ASCII art display"""
        if self.ascii_widget:
            self.ascii_widget.update(art)
    
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
        """Go back to the previous screen"""
        if self.bridge:
            self.bridge.close()
        self.app.pop_screen()
    
    def on_key(self, event) -> None:
        """Handle key presses"""
        if event.key == "enter" and self.input_field and self.input_field.has_focus:
            # Find which button to trigger based on focused input
            focused_id = self.input_field.id
            if focused_id == "push-input":
                self.app.post_message(self.__class__.ButtonPressed(self.query_one("#push-btn")))
            elif focused_id == "enqueue-input":
                self.app.post_message(self.__class__.ButtonPressed(self.query_one("#dequeue-btn")))
            elif focused_id == "insert-input":
                self.app.post_message(self.__class__.ButtonPressed(self.query_one("#remove-btn")))
            elif focused_id == "find-input":
                self.app.post_message(self.__class__.ButtonPressed(self.query_one("#find-btn")))
            # Add more as needed


from bridge import DSBridge