<div align="center">

# TraceDSA

**Interactive Data Structures Visualizer** - Built with C++23 + Python Textual TUI

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/tracedsa)](https://pypi.org/project/tracedsa/)
[![GitHub repo](https://img.shields.io/badge/GitHub-HA2077/TraceDSA-lightgrey)](https://github.com/HA2077/TraceDSA)

</div>

![TraceDSA Screenshot](docs/Trace.png)

## Features

- 9 data structures with live ASCII visualization
- C++23 backend binaries via subprocess bridge
- Real-time operation log with color-coded responses
- DS info screen for summary, Big O, pros/cons, usage
- Search and filter modules from the menu
- Min/Max heap toggle
- Cross-platform support (Linux, Windows, macOS)
- Zero-config install via pipx

## What is it

TraceDSA is a terminal user interface that wraps custom C++23 data structure implementations in an interactive Python TUI. It lets you explore how stacks, queues, trees, and heaps behave with live ASCII art, operation logging, and instant feedback after every command.

## Install & Run

```bash
pip install tracedsa
tdsa
```
Or for Modern Linux distros:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install tracedsa
tdsa
```

Press `s` or click **START** on the splash screen.

## Data Structures

| Category | Implementations | Visualization |
|----------|----------------|---------------|
| **Stack** | Array, Linked List | Vertical |
| **Queue** | Array, Linked List, Circular | Horizontal |
| **Linked List** | Singly, Doubly | Arrow nodes |
| **BST** | Binary Search Tree | Sideways tree |
| **Heap** | Min-Heap, Max-Heap | Tree + Array |

## How it works

TraceDSA spawns standalone C++23 binaries and communicates via a simple stdin/stdout protocol. The Python Textual TUI sends commands (PUSH 10, ENQUEUE 5, etc.) and updates visualizations instantly. No STL containers everything built from scratch.

## Project Architecture

```
TraceDSA/
├── C++ Core (no STL containers)
│   ├── ArrayList/          (header-only dynamic array)
│   ├── Stack/, Queue/, LinkedList/, BST/, PriorityQueue/
│   └── *_interactive.cpp   (stdin/stdout bridge)
│
├── tracedsa/ (Python TUI)
│   ├── __main__.py
│   ├── bridge.py
│   ├── screens/
│   ├── widgets/ (ascii_array, ascii_tree, ascii_heap, etc.)
│   └── bins/{linux,windows,macos}/   ← compiled binaries
|
└── makefiles/
|    ├── Makefile         (Running the TestingModules.cpp file)
|    ├── makefile.windows (build Windows binaries with MinGW)
|    ├── makefile.inter   (build C++ interactive binaries for Linux)
|    └── makefile.macos   (build macOS binaries with clang)
|
└── pyproject.toml  (package config for pipx installation)
└── docs/  (screenshots, architecture diagrams, design docs)
```

## Development

### Prerequisites

- C++23 compiler (g++)
- Python 3.10+
- make

### Build & Run

```bash
# 1. Build C++ interactive binaries
make -f makefile.inter

# 2. Run the TUI
cd tracedsa && python -m tracedsa
```

For Windows builds:

```bash
make -f makefile.windows
```

## Requirements

- Python 3.10+
- C++23 compliant compiler for development (g++ recommended)

## Built With

- **Python** — [Textual](https://github.com/Textualize/textual) framework for the TUI
- **C++23** — All data structures implemented from scratch (no STL containers)

## Roadmap

- [ ] Sorting & Searching algorithms
- [ ] Keyboard shortcuts for all operations
- [ ] Session export / snapshots
- [ ] Comprehensive test suite

## Contributing

Contributions are welcome! New data structures, bug fixes, docs, UI improvements 
please read `CONTRIBUTING.md` first.

## Author

**HA** - [GitHub](https://github.com/HA2077) · [LinkedIn](https://www.linkedin.com/in/hassanahmedcs/)

## License

MIT [LICENSE](LICENSE)

---

Made with ❤️ for learning and teaching Data Structures & Algorithms.
