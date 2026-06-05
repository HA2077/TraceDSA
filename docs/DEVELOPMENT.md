# Development

Setup guide for working on TraceDSA locally.

---

## Prerequisites

- **C++23 compiler** — GCC 11+ (Linux), MinGW-w64 (Windows), GCC via Homebrew (macOS)
- **Python 3.10+**
- **make**

Verify your environment:

```bash
g++ --std=c++23 --version
python3 --version
make --version
```

---

## Quick Start

```bash
# 1. Build all 9 C++ interactive binaries
make -f makefile.inter

# 2. Run the TUI
cd tracedsa && python -m tracedsa
```

---

## Project Tour

```
TraceDSA/
├── Makefile                    # Test runner (build + run + clean)
├── makefile.inter              # Interactive binaries builder
├── pyproject.toml              # Python package config
│
├── C++ Source (alphabetical)
│   ├── ArrayList/ArrayList.h   # Templated dynamic array (header-only)
│   ├── BST/BST.h / .cpp        # Binary Search Tree
│   ├── LinkedList/
│   │   ├── LinkedList.h/cpp       # Singly Linked List
│   │   └── DoublyLinkedList.h/cpp # Doubly Linked List
│   ├── PriorityQueue/
│   │   ├── Heap.h / .cpp          # Min-Heap + Max-Heap
│   ├── Queue/
│   │   ├── Queue.h / .cpp         # Queue (array-backed)
│   │   ├── QueueAsLinkedList.h/cpp  # Queue (linked list)
│   │   └── CircularQueue.h / .cpp   # Circular Queue
│   └── Stack/
│       ├── Stack.h / .cpp            # Stack (array-backed)
│       └── StackAsLinkedList.h / .cpp # Stack (linked list)
│
├── tracedsa/                   # Python TUI package
│   ├── __main__.py             # App entry point
│   ├── bridge.py               # DSBridge subprocess manager
│   ├── screens/                # One file per screen
│   │   ├── splash.py
│   │   ├── menu.py
│   │   ├── info_screen.py
│   │   ├── trace_screen.py
│   │   ├── confirm_dialog.py
│   │   └── help_screen.py
│   └── widgets/                # ASCII visualizer components
│       ├── ascii_array.py
│       ├── ascii_tree.py
│       ├── ascii_heap.py
│       └── ops_log.py
│
├── docs/                       # Documentation
└── TestingModules.cpp          # Standalone test runner entry point (Test the DS/A here without the TUI)
```

---

## Building C++ Binaries

### Interactive binaries (for the TUI)

```bash
make -f makefile.inter
```

This builds all binaries into `tracedsa/bins/linux/`:

```
tracedsa/bins/linux/
├── stack
├── stackll
├── queue
├── queuell
├── circqueue
├── ll
├── dll
├── bst
└── heap
```

### Build a single binary

```bash
make -f makefile.inter stack     # Only stack
make -f makefile.inter bst       # Only BST
make -f makefile.inter heap      # Only heap
```

### Test runner

```bash
make          # Builds and runs the test runner (TestingModules.cpp)
```

---

## Running the TUI

```bash
# From repo root
cd tracedsa && python -m tracedsa

# Or after pip install
tdsa
```

---

## Testing

### Binary protocol tests

Tests all 9 binaries by sending commands and verifying response prefixes:

```bash
cd tracedsa && python3 test_all_interactive.py
```

Each test:
1. Spawns the binary
2. Checks for `READY`
3. Sends a sequence of commands
4. Verifies each response starts with `OK` or `ERROR`
5. Sends `EXIT` and expects `BYE`

### Manual binary testing

Test a single binary directly:

```bash
echo -e "PUSH 10\nPUSH 20\nPRINT\nPOP\nEXIT" | ./tracedsa/bins/linux/stack
```

Expected output:

```
READY
OK Stack: [10]
OK Stack: [10 20]
OK Stack: [10 20]
OK Stack: [10]
BYE
```

---

## Adding a New Interactive Binary

1. Create `*_interactive.cpp` in the DS folder (e.g., `MyDS/my_ds_interactive.cpp`).

2. Implement the stdin/stdout protocol:

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "MyDS.h"

int main() {
    MyDS ds;
    std::cout << "READY" << std::endl;
    std::cout.flush();

    std::string line;
    while (std::getline(std::cin, line)) {
        std::istringstream iss(line);
        std::string cmd;
        iss >> cmd;

        if (cmd == "ACTION") {
            int val;
            if (iss >> val) {
                ds.action(val);
                std::cout << "OK " << ds.toString() << std::endl;
            } else {
                std::cout << "ERROR Invalid value" << std::endl;
            }
        }
        // ... other commands ...
        else if (cmd == "EXIT") {
            std::cout << "BYE" << std::endl;
            break;
        } else {
            std::cout << "ERROR Unknown command: " << cmd << std::endl;
        }
        std::cout.flush();
    }
}
```

3. Add target to `makefile.inter`:
   ```makefile
   SRCS_MYDS = MyDS/MyDS.cpp MyDS/MyDS_interactive.cpp
   myds: dirs
   	$(CXX) $(CXXFLAGS) $(SRCS_MYDS) -o $(BINS)/myds
   ```
   Add `myds` to the `all` target.

4. Add config to `trace_screen.py` `MODULE_CONFIGS`.

5. Add info data to `info_screen.py` `MODULE_INFO`.

6. Add binary name to `splash.py` `BINARY_NAMES`.

---

## Known Issues

- **Heap CLEAR response** — cleared heap always prints `toStringMinHeap()`. In Max-Heap mode, the widget briefly shows "min" on empty state. Next operation corrects it.
- **Binary path fallback** — `_launch_module` falls back to `./TUI/bins/linux/{name}` if `get_binary()` fails.
- `cout.flush()` is required after every C++ response — forgetting it causes the Python subprocess to hang indefinitely.

---

## Cross-Platform Builds

### Windows (MinGW)

```bash
make -f makefile.windows
```

Output goes to `tracedsa/bins/windows/` with `.exe` extension.

### macOS (GCC via Homebrew)

```bash
brew install gcc
make -f makefile.macos
```

Output goes to `tracedsa/bins/macos/`.
