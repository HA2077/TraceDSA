from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static, Button
from textual.screen import Screen
from textual.binding import Binding
import webbrowser

from .trace_screen import TraceWindow
from .help_screen import HelpScreen


MODULE_INFO = {
    "stack": {
        "title": "Stack (Array)",
        "summary": "A stack is a LIFO (Last In, First Out) data structure built on top of a dynamic array. Elements are added (pushed) and removed (popped) from the top only. The underlying ArrayList doubles its capacity when full, giving amortized O(1) push.",
        "methods": [
            ("push(val)", "Add an element to the top of the stack"),
            ("pop()", "Remove and return the top element"),
            ("peek()", "View the top element without removing it"),
            ("clear()", "Remove all elements from the stack"),
        ],
        "big_o": [
            "push — O(1) amortized",
            "pop — O(1)",
            "peek — O(1)",
            "clear — O(n)",
        ],
        "pros": [
            "O(1) push/pop/peek",
            "Simple and intuitive API",
            "Contiguous memory (cache-friendly)",
        ],
        "cons": [
            "Resizing is O(n)",
            "No random access",
            "Dynamic resizing overhead",
        ],
        "usage": [
            "CPU function call stack",
            "Undo/redo in text editors",
            "Expression evaluation (postfix)",
        ],
        "source_url": "https://github.com/HA2077/TraceDSA/blob/main/Stack/Stack.cpp",
    },
    "stackll": {
        "title": "Stack (LinkedList)",
        "summary": "A stack implemented using a singly linked list. Elements are pushed and popped from the head of the list (O(1)). Unlike the array-backed version, there is no resizing overhead, but each element carries the cost of a pointer.",
        "methods": [
            ("push(val)", "Insert a new node at the head (top)"),
            ("pop()", "Remove and return the head node"),
            ("peek()", "Return the head node's value without removing"),
            ("clear()", "Remove all nodes from the list"),
        ],
        "big_o": [
            "push — O(1)",
            "pop — O(1)",
            "peek — O(1)",
            "clear — O(n)",
        ],
        "pros": [
            "O(1) push/pop/peek",
            "No resizing needed",
            "Unbounded growth",
        ],
        "cons": [
            "Extra memory per element (pointer)",
            "Not cache-friendly",
            "No random access",
        ],
        "usage": [
            "Undo/redo with unbounded history",
            "Parsing nested structures",
            "Backtracking algorithms",
        ],
        "source_url": "https://github.com/HA2077/TraceDSA/blob/main/Stack/StackAsLinkedList.cpp",
    },
    "queue": {
        "title": "Queue (Array)",
        "summary": "A FIFO (First In, First Out) queue backed by a dynamic array. Elements are enqueued at the rear and dequeued from the front. Uses a growth strategy similar to ArrayList for the underlying storage.",
        "methods": [
            ("enqueue(val)", "Add an element to the rear of the queue"),
            ("dequeue()", "Remove and return the front element"),
            ("peek()", "View the front element without removing"),
            ("clear()", "Remove all elements from the queue"),
        ],
        "big_o": [
            "enqueue — O(1) amortized",
            "dequeue — O(1)",
            "peek — O(1)",
            "clear — O(n)",
        ],
        "pros": [
            "O(1) enqueue/dequeue/peek",
            "FIFO ordering (fair)",
            "Contiguous memory",
        ],
        "cons": [
            "Resizing is O(n)",
            "Front pointer management",
            "Wasted space if not compacted",
        ],
        "usage": [
            "BFS graph traversal",
            "CPU task scheduling",
            "Print spooler buffer",
        ],
        "source_url": "https://github.com/HA2077/TraceDSA/blob/main/Queue/Queue.cpp",
    },
    "queuell": {
        "title": "Queue (LinkedList)",
        "summary": "A FIFO queue implemented with a singly linked list. Two pointers (head and tail) give O(1) enqueue and dequeue. No resizing is needed, making it suitable for unpredictable workloads.",
        "methods": [
            ("enqueue(val)", "Append a new node at the tail (rear)"),
            ("dequeue()", "Remove and return the head node (front)"),
            ("peek()", "Return the head node's value without removing"),
            ("clear()", "Remove all nodes from the queue"),
        ],
        "big_o": [
            "enqueue — O(1)",
            "dequeue — O(1)",
            "peek — O(1)",
            "clear — O(n)",
        ],
        "pros": [
            "O(1) enqueue/dequeue/peek",
            "No resizing overhead",
            "Unbounded growth",
        ],
        "cons": [
            "Extra memory per element (pointer)",
            "Not cache-friendly",
            "Pointer management complexity",
        ],
        "usage": [
            "IO buffers with variable load",
            "Event-driven simulations",
            "Task queues in web servers",
        ],
        "source_url": "https://github.com/HA2077/TraceDSA/blob/main/Queue/QueueAsLinkedList.cpp",
    },
    "circqueue": {
        "title": "Circular Queue",
        "summary": "A fixed-size queue that reuses array slots by wrapping around via modular arithmetic. When the rear reaches the end, it wraps to index 0 if space is available. No resizing means predictable performance.",
        "methods": [
            ("enqueue(val)", "Add an element at the rear (wraps around)"),
            ("dequeue()", "Remove and return the front element"),
            ("peek()", "View the front element without removing"),
            ("clear()", "Reset front, rear, and size"),
        ],
        "big_o": [
            "enqueue — O(1)",
            "dequeue — O(1)",
            "peek — O(1)",
            "clear — O(1)",
        ],
        "pros": [
            "All operations O(1)",
            "Fixed memory footprint",
            "No resizing overhead",
            "No memory fragmentation",
        ],
        "cons": [
            "Fixed maximum capacity",
            "Wasted slot if not full",
            "Modulo arithmetic overhead",
        ],
        "usage": [
            "Ring buffers in audio/video",
            "Fixed-size task pools",
            "Hardware FIFO buffers",
        ],
        "source_url": "https://github.com/HA2077/TraceDSA/blob/main/Queue/CircularQueue.cpp",
    },
    "ll": {
        "title": "Singly Linked List",
        "summary": "A linear collection of nodes where each node holds data and a pointer to the next node. Singly linked lists excel at O(1) insertions and deletions at the head, but require O(n) traversal for access.",
        "methods": [
            ("insertAtStart(val)", "Insert a new node at the head (O(1))"),
            ("insertAtEnd(val)", "Append a new node at the tail (O(n))"),
            ("deleteAtStart()", "Remove the head node (O(1))"),
            ("deleteAtEnd()", "Remove the tail node (O(n))"),
            ("deleteWithVal(val)", "Remove the first node with matching value"),
            ("clear()", "Remove all nodes from the list"),
        ],
        "big_o": [
            "insertAtStart — O(1)",
            "insertAtEnd — O(n)",
            "deleteAtStart — O(1)",
            "deleteAtEnd — O(n)",
            "deleteWithVal — O(n)",
            "clear — O(n)",
        ],
        "pros": [
            "O(1) head insert/delete",
            "Dynamic size (no resizing)",
            "Simple pointer structure",
        ],
        "cons": [
            "O(n) access by index",
            "O(n) tail operations",
            "Extra memory per element",
            "No backward traversal",
        ],
        "usage": [
            "Hash table chaining",
            "Adjacency lists for graphs",
            "Stack/queue implementations",
        ],
        "source_url": "https://github.com/HA2077/TraceDSA/blob/main/LinkedList/LinkedList.cpp",
    },
    "dll": {
        "title": "Doubly Linked List",
        "summary": "A linked list where each node has both a next and a prev pointer, enabling O(1) insertions and deletions at both ends. The toString() method shows both forward and backward traversals.",
        "methods": [
            ("insertAtStart(val)", "Insert at the head (O(1))"),
            ("insertAtEnd(val)", "Insert at the tail (O(1))"),
            ("deleteAtStart()", "Remove the head node (O(1))"),
            ("deleteAtEnd()", "Remove the tail node (O(1))"),
            ("clear()", "Remove all nodes from the list"),
        ],
        "big_o": [
            "insertAtStart — O(1)",
            "insertAtEnd — O(1)",
            "deleteAtStart — O(1)",
            "deleteAtEnd — O(1)",
            "clear — O(n)",
        ],
        "pros": [
            "O(1) insert/delete at both ends",
            "Bidirectional traversal",
            "Efficient for deque implementations",
        ],
        "cons": [
            "Extra memory per node (two pointers)",
            "More complex pointer management",
            "Not cache-friendly",
        ],
        "usage": [
            "Implementation of deque",
            "Navigation (forward/backward) history",
            "LRU cache eviction",
        ],
        "source_url": "https://github.com/HA2077/TraceDSA/blob/main/LinkedList/DoublyLinkedList.cpp",
    },
    "bst": {
        "title": "Binary Search Tree",
        "summary": "A tree-based data structure where each node has at most two children. For every node, values in its left subtree are smaller and values in its right subtree are larger. Supports O(log n) average-case search, insert, and delete.",
        "methods": [
            ("insert(val)", "Insert a value into the BST"),
            ("remove(val)", "Remove a value (handles leaf, one child, two children)"),
            ("find(val)", "Search for a value — returns true or false"),
            ("clear()", "Remove all nodes from the tree"),
            ("inorder()", "Sorted order traversal"),
            ("preorder()", "Root-first traversal"),
            ("postorder()", "Children-first traversal"),
        ],
        "big_o": [
            "insert — O(log n) avg, O(n) worst",
            "remove — O(log n) avg, O(n) worst",
            "find — O(log n) avg, O(n) worst",
            "traversals — O(n)",
        ],
        "pros": [
            "O(log n) average search/insert/delete",
            "In-order gives sorted output",
            "Versatile for range queries",
        ],
        "cons": [
            "O(n) worst case (unbalanced)",
            "Self-balancing is complex",
            "No O(1) operations",
        ],
        "usage": [
            "Database indexes",
            "File system directory structures",
            "Expression trees in compilers",
        ],
        "source_url": "https://github.com/HA2077/TraceDSA/blob/main/BST/BST.cpp",
    },
    "heap": {
        "title": "Heap (Min/Max)",
        "summary": "A complete binary tree implemented on an array where each parent is smaller (min-heap) or larger (max-heap) than its children. Supports O(log n) insert and extract, with O(1) peek at the root. This implementation supports both min and max modes.",
        "methods": [
            ("enqueue(val)", "Insert a value into the heap"),
            ("dequeueMin()", "Extract the minimum value (min-heap)"),
            ("dequeueMax()", "Extract the maximum value (max-heap)"),
            ("peekMin()", "View the minimum value without removing"),
            ("peekMax()", "View the maximum value without removing"),
            ("clear()", "Remove all elements from the heap"),
            ("toggle", "Switch between min-heap and max-heap mode"),
        ],
        "big_o": [
            "enqueue — O(log n)",
            "dequeueMin — O(log n)",
            "dequeueMax — O(log n)",
            "peek — O(1)",
            "clear — O(1)",
        ],
        "pros": [
            "O(1) access to min/max",
            "O(log n) insert and extract",
            "Space-efficient (array-backed)",
        ],
        "cons": [
            "No search for arbitrary values",
            "Not stable (order of equal elements)",
            "Only limited to min/max access",
        ],
        "usage": [
            "Priority queues (scheduling)",
            "Dijkstra's shortest path",
            "Heap sort algorithm",
        ],
        "source_url": "https://github.com/HA2077/TraceDSA/blob/main/PriorityQueue/Heap.cpp",
    },
}


class ModuleInfoScreen(Screen):

    BINDINGS = [
        Binding("escape", "go_back", "Back"),
        Binding("h", "show_help", "Help"),
        Binding("?", "show_help", "Help"),
    ]

    DEFAULT_CSS = """
    ModuleInfoScreen {
        background: #1a1a2e;
    }

    #info_container {
        layout: vertical;
        width: 100%;
        height: 100%;
        overflow-y: auto;
    }

    #info_header {
        layout: horizontal;
        content-align: left middle;
        width: 100%;
        height: auto;
        background: #16213e;
        border: round #0f3460;
        padding: 0 2;
    }

    #info_header #back_button {
        width: auto;
        color: #666680;
    }

    #info_header #back_button:hover {
        color: #00d4ff;
    }

    #info_title {
        color: #ffffff;
        text-style: bold;
        text-align: center;
        width: 1fr;
    }

    #info_body {
        layout: vertical;
        width: 100%;
        height: auto;
        padding: 1 2;
    }

    .section-header {
        color: #00d4ff;
        text-style: bold;
        width: 100%;
        height: auto;
        margin-top: 1;
        margin-bottom: 0;
    }

    .section-body {
        color: #e0e0e0;
        width: 100%;
        height: auto;
        margin-bottom: 0;
    }

    .method-row {
        width: 100%;
        height: auto;
    }

    .method-name {
        color: #e0e0e0;
        text-style: bold;
        width: auto;
        margin-right: 1;
    }

    .method-desc {
        color: #666680;
        width: 1fr;
    }

    .big-o-text {
        color: #e0e0e0;
        width: 100%;
        height: auto;
        margin-left: 1;
    }

    #pros-cons {
        width: 100%;
        height: auto;
    }

    #pros-col, #cons-col {
        width: 1fr;
        height: auto;
    }

    .section-subheader {
        color: #00d4ff;
        text-style: bold;
        width: 100%;
        height: auto;
        margin-bottom: 0;
    }

    .pros-item, .cons-item {
        color: #e0e0e0;
        width: 100%;
        height: auto;
    }

    .usage-item {
        color: #e0e0e0;
        width: 100%;
        height: auto;
    }

    #source_btn {
        width: auto;
        margin-top: 1;
    }

    #trace_btn {
        width: 100%;
        margin-top: 1;
        margin-bottom: 1;
    }
    """

    def __init__(self, binary_name: str, display_name: str):
        super().__init__()
        self.binary_name = binary_name
        self.display_name = display_name

    def compose(self) -> ComposeResult:
        yield Container(
            Container(
                Button("← Back", id="back_button", variant="default"),
                Static(self.display_name.upper(), id="info_title"),
                id="info_header"
            ),
            Container(id="info_body"),
            id="info_container"
        )

    def on_mount(self) -> None:
        info = MODULE_INFO.get(self.binary_name)
        if not info:
            self.app.pop_screen()
            return

        body = self.query_one("#info_body")

        body.mount(Static("Summary", classes="section-header"))
        body.mount(Static(info["summary"], classes="section-body"))

        body.mount(Static("Methods", classes="section-header"))
        for name, desc in info["methods"]:
            body.mount(Horizontal(
                Static(f"• {name}", classes="method-name"),
                Static(f"— {desc}", classes="method-desc"),
                id=f"method_{name.replace('(', '').replace(')', '').replace(' ', '_')}",
                classes="method-row"
            ))

        body.mount(Static("Big O Notation", classes="section-header"))
        for line in info["big_o"]:
            body.mount(Static(f"• {line}", classes="big-o-text"))

        body.mount(Static("Pros & Cons", classes="section-header"))
        body.mount(Horizontal(
            Vertical(
                Static("Pros", classes="section-subheader"),
                *[Static(f"• {p}", classes="pros-item") for p in info["pros"]],
                id="pros-col"
            ),
            Vertical(
                Static("Cons", classes="section-subheader"),
                *[Static(f"• {c}", classes="cons-item") for c in info["cons"]],
                id="cons-col"
            ),
            id="pros-cons"
        ))

        body.mount(Static("Real-Life Usage", classes="section-header"))
        for u in info["usage"]:
            body.mount(Static(f"• {u}", classes="usage-item"))

        body.mount(Button("📂  View Source Code", id="source_btn", variant="default"))
        body.mount(Button("  TRACE  ", id="trace_btn", variant="primary"))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back_button":
            self.action_go_back()
        elif button_id == "trace_btn":
            self.app.push_screen(TraceWindow(self.binary_name, self.display_name))
        elif button_id == "source_btn":
            info = MODULE_INFO.get(self.binary_name)
            if info:
                webbrowser.open(info["source_url"])

    def action_go_back(self) -> None:
        self.app.pop_screen()

    def action_show_help(self) -> None:
        self.app.push_screen(HelpScreen())
