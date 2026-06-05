# Contributing

Contributions are welcome! New data structures, bug fixes, documentation, UI improvements. Please read this guide before opening a pull request.

---

## Getting Started

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/HA2077/TraceDSA.git
   cd TraceDSA
   ```
3. Build the C++ interactive binaries:
   ```bash
   make -f makefile.inter
   ```
4. Verify the TUI runs:
   ```bash
   cd tracedsa && python -m tracedsa
   ```

---

## Code Style

### C++23

- Standard: `-std=c++23 -Wall -Wextra -Wpedantic`
- Compiler: GCC (primary), MinGW (Windows)
- **No STL containers** — use the custom `ArrayList` instead of `std::vector`
- `toString()` must return `std::string` — never `void` with `cout`
- `cout` / `iostream` is reserved for the stdin/stdout protocol only
- Do not add operation logs or debug output to DS methods

### Python (Textual TUI)

- All styling via `DEFAULT_CSS` or `.styles` inline — no external `.tcss` files
- Follow existing patterns in `screens/` and `widgets/`
- `DSBridge` should be the only interface to C++ binaries

---

## Adding a New Data Structure

### C++ Side

1. Create a new folder (e.g., `MyDS/`) with `MyDS.h` and `MyDS.cpp`.
2. Implement the data structure **without STL containers**.
3. Create `MyDS_interactive.cpp` following the stdin/stdout protocol:
   - Print `READY` on startup
   - Command loop reading from `cin`
   - Respond with `OK <data>` or `ERROR <message>`
   - Handle `EXIT` → `BYE`
   - `cout.flush()` after every response
4. Add the `.cpp` files to `makefile.inter`:
   ```makefile
   SRCS_MYDS = MyDS/MyDS.cpp MyDS/MyDS_interactive.cpp
   myds: dirs
   	$(CXX) $(CXXFLAGS) $(SRCS_MYDS) -o $(BINS)/myds
   ```
   Add `myds` to `all` target.
5. Add the DS `.cpp` to `Makefile` (test runner) for standalone testing.

### Python Side

1. Add the binary name to `BINARY_NAMES` in `screens/splash.py`.
2. Add a config entry to `MODULE_CONFIGS` in `screens/trace_screen.py`:
   ```python
   "myds": {
       "ascii_type": "array",  # or "tree", "heap", "linked", "doubly"
       "buttons": [
           ("ACTION", "action_btn", needs_input_bool),
       ],
   }
   ```
3. Add info data to `MODULE_INFO` in `screens/info_screen.py`:
   ```python
   "myds": {
       "title": "My DS",
       "summary": "...",
       "methods": [("method()", "description")],
       "big_o": ["op — O(1)"],
       "pros": [...],
       "cons": [...],
       "usage": [...],
       "source_url": "https://github.com/HA2077/TraceDSA/blob/main/MyDS/MyDS.cpp",
   }
   ```
4. If the ASCII visualization needs a new widget, create it in `widgets/` following the existing patterns.

---

## Bridge Protocol

Each C++ interactive binary follows this contract:

```
READY                          ← printed on startup
> PUSH 10                     ← Python sends command + arg
< OK Stack: [10]              ← C++ responds
> POP
< OK Stack: [empty]
> POP
< ERROR Cannot pop from empty stack
> EXIT
< BYE
```

---

## Pull Request Process

1. Create a feature branch from `main`.
2. Make your changes, keeping commits focused and descriptive.
3. Verify the C++ test runner still passes:
   ```bash
   make && ./main
   ```
4. Verify the Python bridge tests pass:
   ```bash
   python3 tracedsa/test_all_interactive.py
   ```
5. Verify the TUI launches without errors:
   ```bash
   cd tracedsa && python -m tracedsa
   ```
6. Open a pull request with a clear description of what changed and why.

---

## Reporting Issues

Use the [GitHub issue tracker](https://github.com/HA2077/TraceDSA/issues). Include:

- Steps to reproduce
- Expected vs actual behavior
- Terminal output / error logs
- OS and Python version
