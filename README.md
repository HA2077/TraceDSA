<div align="center">

# TraceDSA

**Visualize Data Structures in real time a Python TUI powered by C++23 binaries.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/tracedsa)](https://pypi.org/project/tracedsa/)

</div>

![TraceDSA SC](docs/Trace.png)

## Features

- 9 data structures with live ASCII visualization
- C++23 backend binaries via subprocess bridge
- Real-time operation log with color-coded responses
- DS info screen summary, Big O, pros/cons, usage
- Search and filter modules from the menu
- Min/Max heap toggle
- Works out of the box via pip

## What is it

TraceDSA is a terminal user interface that wraps custom C++23 data structure implementations in an interactive Python TUI. It lets you explore how stacks, queues, trees, and heaps behave with live ASCII art, operation logging, and instant feedback after every command.

## Install & Run

```bash
pip install tracedsa
tdsa
```

## Data Structures

| Category | Modules |
|----------|---------|
| **Stack** | Stack (Array), Stack (LinkedList) |
| **Queue** | Queue (Array), Queue (LinkedList), Circular Queue |
| **Linked List** | Singly LinkedList, Doubly LinkedList |
| **BST** | Binary Search Tree |
| **Heap** | Min-Heap, Max-Heap |

## How it works

TraceDSA uses a Python Textual TUI that spawns standalone C++23 interactive binaries as subprocesses. The TUI communicates with each binary via a simple stdin/stdout protocol (`PUSH 10` → `OK Stack: [10]`). Every button press sends a command, and the response updates the ASCII visualization and operation log in real time. No STL containers are used in the C++ backend every data structure is built from scratch.

## Requirements

- Python 3.10+
- Linux (Windows & macOS in progress)

## Built With

- **Python** — [Textual](https://github.com/Textualize/textual) framework for the TUI
- **C++23** — All data structures implemented from scratch (no STL containers)

## Author

**HA** [GitHub](https://github.com/HA2077) · [LinkedIn](https://www.linkedin.com/in/hassanahmedcs/)

## License

MIT see [LICENSE](LICENSE)

--- 

Made with ❤️ and stay tuned for updates!
