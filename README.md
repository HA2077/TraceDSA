# Data Structures in C++ (DS All In One)
**A collection of foundational Data Structures implemented from scratch in C++, built for a better understanding of the data structure course I am taking.**

## 🚀 Current Modules

* **Stack:** Implemented using a custom `ArrayList` (LIFO). Includes manual boundary checking to ensure stability during `pop` operations.
* **Queue:** Implemented using a custom `ArrayList` (FIFO). Utilizes dynamic resizing to eliminate fixed-size limitations.
* **Singly Linked List:** Built using custom `Node` structs and `nullptr` for modern memory safety (C++23 standard). Supports insertion and deletion at both ends and by specific value.
* **Binary Search Tree (BST):** Implemented with insert, remove, find operations and three traversal methods (Pre-order, In-order, Post-order).
* **Priority Queue (Heap):** Implemented with both Min-Heap and Max-Heap functionality, supporting insert, extract-min/max, and peek operations.

## 🛠️ Extended Roadmap

As the semester progresses, the following structures will be implemented in sync with the course syllabus:

- [x] **ArrayList:** Manual implementation of a dynamic array (resizing logic).
- [x] **Trees:** Binary Search Trees (BST) and traversal algorithms (In-order, Pre-order, Post-order).
- [x] **Priority Queues:** Implementation using Heaps.
- [ ] **Unified TUI:** A Terminal User Interface for real-time visualization of data states.
    * *Note: Still evaluating whether to use Python for the TUI wrapper or keep it pure C++.*

## 💻 Tech Stack
* **Language:** C++23 (utilizing `nullptr` and modern standards).
* **Environment:** Linux / Windows GCC.
* **Key Improvement:** Stack and Queue now use a custom ArrayList implementation instead of STL vector or fixed arrays.