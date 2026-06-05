# Architecture

TraceDSA is a three-layer system: a Python Textual TUI that communicates with standalone C++23 interactive binaries via a stdin/stdout subprocess bridge.

---

## System Layers

### Layer 1: Python TUI (Textual)

The user interface lives in `tracedsa/` and is built with the [Textual](https://github.com/Textualize/textual) framework. All styling is inline — no external `.tcss` files (`App.CSS_PATH = None`).

```
tracedsa/
├── __main__.py           # TraceDSApp, global DEFAULT_CSS, bridge init, SHORTCUTS dict
├── bridge.py             # DSBridge — subprocess wrapper
├── screens/
│   ├── splash.py         # Animated ASCII reveal, async bridge init (9 binaries), START
│   ├── menu.py           # 2-level category→module nav, real-time search filter
│   ├── info_screen.py    # DS info: summary, Big O, pros/cons, usage, source link
│   ├── trace_screen.py   # Operation window: ASCII viz + buttons + log + status bar
│   ├── confirm_dialog.py # Yes/No exit confirmation
│   └── help_screen.py    # Renders SHORTCUTS dict
└── widgets/
    ├── ascii_array.py    # Stack (vertical), Queue (horizontal), Singly/Doubly LL, Array
    ├── ascii_tree.py     # BST rendering via sideways CLI tree (├── └──)
    ├── ascii_heap.py     # Min/Max heap: tree view + array view toggle
    └── ops_log.py        # RichLog with color-coded entries (OK=cyan, ERROR=bold red)
```

**Screen flow:**

```
Splash ──enter/s──→ MainMenu ──click module──→ InfoScreen ──TRACE──→ TraceWindow
   ↑                    │                          │                    │
   │                    │ q/escape                 │ ← Back             │ Escape
   │                    ↓                          ↓                    ↓
   │              ConfirmDialog               MainMenu             MainMenu
   └──────────────────────┘
      (q again → exit)
```

### Layer 2: Bridge (`tracedsa/bridge.py`)

`DSBridge` wraps a `subprocess.Popen` to the C++ binary:

- **`__init__(name)`** — spawns `bins/{os}/{name}`, consumes `READY` line
- **`send(command)`** — writes command to stdin, returns response from stdout
- **`is_alive()`** — checks if process is still running
- **`close()`** — sends `EXIT`, then terminates

`get_binary(name)` resolves the platform-appropriate path:
- Linux → `bins/linux/{name}`
- Windows → `bins/windows/{name}.exe`
- macOS → `bins/macos/{name}`

Also ensures the binary is executable (chmod +x) on Unix systems.

### Layer 3: C++23 Backend (9 interactive binaries)

Each binary follows the same pattern:

```cpp
int main() {
    DS instance;
    cout << "READY" << endl;
    cout.flush();

    string line;
    while (getline(cin, line)) {
        istringstream iss(line);
        string cmd;
        iss >> cmd;

        if (cmd == "PUSH") { ... }
        else if (cmd == "POP") { ... }
        // ...
        else if (cmd == "EXIT") {
            cout << "BYE" << endl;
            break;
        }
        cout.flush();  // critical — prevents Python subprocess hang
    }
}
```

Each binary is compiled from a `*_interactive.cpp` file paired with the DS implementation in `*.cpp`/`.h`. For example, `Stack/Stack.cpp` + `Stack/Stack_interactive.cpp`.

---

## Data Flow (per operation)

```
User clicks button / presses Enter
  → trace_screen._build_command(button_id)
  → trace_screen._execute_command(command)
    → DSBridge.send(command)
      → writes to C++ binary's stdin (text)
      → C++ parses, executes DS method
      → C++ writes response to stdout
      → Python reads response line
    ← returns response string
  → if command is state-changing:
      _update_ascii_from_response(response)
        → _update_array_widget() / _update_tree_widget() / _update_heap_widget()
        → widget.render() updates ASCII display
  → OpsLog.add_entry() color-codes and appends to log
  → input fields cleared (if applicable)
```

---

## CSS Architecture

All styles are defined in `DEFAULT_CSS` class variables — no external `.tcss` files.

| File | Scope |
|------|-------|
| `__main__.py` | Global: App, Screen, Button variants, Trace Window layout, Inputs, Scrollbar, Status bar |
| `screens/splash.py` | Splash-specific: ASCII art, links row, START button, progress text |
| `screens/menu.py` | Menu-specific: header, middle section, section header, category/module buttons, search results |
| `screens/info_screen.py` | Info-specific: section headers, pros/cons columns, source/trace buttons |
| `screens/confirm_dialog.py` | Dialog-specific: confirm-box, Yes/No buttons |
| `screens/help_screen.py` | Help-specific: help-box, section headers, key rows |

---

## Keyboard Shortcuts

| Key | Scope | Action |
|-----|-------|--------|
| `q` | Global (priority) | Confirm exit |
| `h` / `?` | All screens | Show help screen |
| `enter` / `s` | Splash | Start application |
| `/` | Menu | Focus search bar |
| `escape` | Menu | Confirm exit |
| `escape` | Trace | Confirm return to menu |
| `escape` | Confirm/Help | Dismiss |
| `y` / `n` | Confirm dialog | Yes / No |
| `Tab` | Trace | Cycle buttons/inputs |

---

## Key Design Decisions

- **No STL containers** — custom `ArrayList` replaces `std::vector`. Stack, Queue, and others use `ArrayList` internally.
- **`toString()` returns `std::string`** — never streams directly. Designed for TUI consumption.
- **`cout` reserved for protocol** — only protocol lines (OK, ERROR, BYE) go to stdout. No debug output.
- **`cout.flush()` after every response** — prevents Python subprocess from hanging.
- **Two Makefiles** — `Makefile` (test runner, `make`), `makefile.inter` (interactive binaries, `make -f makefile.inter`). Kept separate so `make` never builds interactive targets.
- **`ArrayList` is header-only** — templated, full implementation in `.h`. Never added to Makefile `SRCS`.

---

## Distribution

The Python package is built with Hatchling. Compiled C++ binaries are included as package data:

```toml
[tool.hatch.build.targets.wheel]
packages = ["tracedsa"]

[tool.hatch.build.targets.wheel.force-include]
"tracedsa/bins" = "tracedsa/bins"
```

The `tdsa` CLI entry point is registered in `pyproject.toml`:
```toml
[project.scripts]
tdsa = "tracedsa.__main__:main"
```
