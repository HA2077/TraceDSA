# TraceDSA Roadmap

This document tracks the planned development direction for TraceDSA. The project is actively maintained contributions toward any of these are welcome.

---

## v1.0.x — Polish & Stability (Current)

Bug fixes and UX improvements on the shipped foundation.

- [ ] Fix broken/misaligned ASCII art entries in the menu quote pool
- [ ] Fix heap min/max toggle state not updating immediately in all cases
- [ ] Wire tree/array toggle button for heap visualization (backend exists, no UI trigger yet)
- [ ] Add keyboard shortcuts for DS operations (`p` → PUSH, `o` → POP, etc.)
- [ ] Add arrow key navigation throughout menus
- [ ] Add confirm dialog on escape from trace screen
- [ ] Add clear-log button in trace view
- [ ] Harden ArrayList C++ implementation edge cases

---

## v1.1 — Sorting Algorithms

Extend TraceDSA beyond data structures into algorithm visualization.

- [ ] Bubble Sort
- [ ] Selection Sort
- [ ] Insertion Sort
- [ ] Merge Sort
- [ ] Quick Sort

Each algorithm will generate a step-by-step state list from the C++ backend. The Python TUI iterates through states with a configurable timer, showing each comparison and swap as it happens.

---

## v1.2 — Quality of Life

- [ ] Session export save a trace session as a log file
- [ ] Snapshots bookmark a state mid-trace and return to it
- [ ] Comprehensive test suite for C++ modules
- [ ] Speed control for algorithm playback

---

## Future Considerations

- Graph data structures (adjacency list / matrix)
- Search algorithm visualizations (BFS, DFS, Binary Search)

---

## Recently Shipped (v1.0.0 → v1.0.3)

- 9 data structure modules: Stack (Array/LL), Queue (Array/LL/Circular), Singly LL, Doubly LL, BST, Min/Max Heap
- Info screen per DS with Big O, pros/cons, use cases
- Custom `ArrayList` C++23 backend — no STL containers
- Custom stdin/stdout binary bridge protocol
- Cross-platform CI/CD — Linux, Windows, macOS via GitHub Actions
- Published to PyPI as `tdsa` CLI tool
- Menu redesign with categories, search, ASCII art pool
