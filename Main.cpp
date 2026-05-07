#include <iostream>
#include "Stack/Stack.h"
#include "Stack/StackAsLinkedList.h"
#include "Queue/Queue.h"
#include "Queue/QueueAsLinkedList.h"
#include "Queue/Circular Queue.h"
#include "LinkedList/LinkedList.h"
#include "LinkedList/DoublyLinkedList.h"
#include "ArrayList/ArrayList.h"
#include "BST/BST.h"
#include "PriorityQueue/Heap.h"
using namespace std;

int main(){
    cout << "===============================================" << endl;
    cout << "     DATA STRUCTURES - COMPREHENSIVE TESTS     " << endl;
    cout << "===============================================" << endl;
    
    // ==================== STACK AS ARRAY ====================
    cout << "\n\n=== TESTING STACK (ARRAY IMPLEMENTATION) ===" << endl;
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    cout << s.toString() << endl;
    cout << "Peek: " << s.peek() << endl;
    s.pop();
    cout << s.toString() << endl;
    s.pop();
    cout << s.toString() << endl;
    s.pop();
    cout << s.toString() << endl; // Should be empty
    
    // ==================== STACK AS LINKED LIST ====================
    cout << "\n\n=== TESTING STACK (LINKED LIST IMPLEMENTATION) ===" << endl;
    StackAsLinkedList sll;
    sll.push(100);
    sll.push(200);
    sll.push(300);
    cout << sll.toString() << endl;
    cout << "Peek: " << sll.peek() << endl;
    sll.pop();
    cout << sll.toString() << endl;
    sll.pop();
    cout << sll.toString() << endl;
    sll.pop();
    cout << sll.toString() << endl; // Should be empty
    
    // ==================== QUEUE AS ARRAY ====================
    cout << "\n\n=== TESTING QUEUE (ARRAY IMPLEMENTATION) ===" << endl;
    Queue q;
    q.Enqueue(5);
    q.Enqueue(15);
    q.Enqueue(25);
    cout << q.toString() << endl;
    q.Dequeue();
    cout << q.toString() << endl;
    q.Dequeue();
    cout << q.toString() << endl;
    q.Dequeue();
    cout << q.toString() << endl; // Should be empty

    cout << "\n--- Testing Queue Array Resizing ---" << endl;
    for(int i = 0; i < 12; i++)
        q.Enqueue(i * 10);
    cout << q.toString() << endl;
    
    // ==================== QUEUE AS LINKED LIST ====================
    cout << "\n\n=== TESTING QUEUE (LINKED LIST IMPLEMENTATION) ===" << endl;
    QueueAsLinkedList qll;
    qll.Enqueue(7);
    qll.Enqueue(14);
    qll.Enqueue(21);
    cout << qll.toString() << endl;
    qll.Dequeue();
    cout << qll.toString() << endl;
    qll.Dequeue();
    cout << qll.toString() << endl;
    qll.Dequeue();
    cout << qll.toString() << endl; // Should be empty
    
    // ==================== CIRCULAR QUEUE ====================
    cout << "\n\n=== TESTING CIRCULAR QUEUE ===" << endl;
    CircularQueue cq;
    cq.Enqueue(5);
    cq.Enqueue(15);
    cq.Enqueue(25);
    cout << cq.tostring() << endl;
    cq.Dequeue();
    cout << cq.tostring() << endl;
    cq.Dequeue();
    cout << cq.tostring() << endl;
    cq.Dequeue();
    cout << cq.tostring() << endl; // Should be empty

    // ==================== SINGLY LINKED LIST ====================
    cout << "\n\n=== TESTING SINGLY LINKED LIST ===" << endl;
    LinkedList ll;
    cout << "Inserting at start..." << endl;
    ll.insertAthestart(50);
    ll.insertAthestart(40);
    ll.insertAthestart(30);
    cout << "Inserting at end..." << endl;
    ll.insertAtTheEnd(60);
    ll.insertAtTheEnd(70);
    cout << ll.toString() << endl;
    cout << "Deleting at start..." << endl;
    ll.deleteAtTheStart();
    cout << ll.toString() << endl;
    cout << "Deleting at end..." << endl;
    ll.deleteAtTheEnd();
    cout << ll.toString() << endl;
    cout << "Deleting element with value 50..." << endl;
    ll.deletewithval(50);
    cout << ll.toString() << endl;
    
    // ==================== DOUBLY LINKED LIST ====================
    cout << "\n\n=== TESTING DOUBLY LINKED LIST ===" << endl;
    DoublyLinkedList dll;
    cout << "Inserting at start..." << endl;
    dll.insertAtTheStart(100);
    dll.insertAtTheStart(90);
    dll.insertAtTheStart(80);
    cout << "Inserting at end..." << endl;
    dll.insertAtTheEnd(110);
    dll.insertAtTheEnd(120);
    cout << dll.toString() << endl;
    cout << "Deleting at start..." << endl;
    dll.deleteAtTheStart();
    cout << dll.toString() << endl;
    cout << "Deleting at end..." << endl;
    dll.deleteAtTheEnd();
    cout << dll.toString() << endl;
    
    // ==================== ARRAY LIST ====================
    cout << "\n\n=== TESTING ARRAY LIST (DYNAMIC) ===" << endl;
    ArrayList<int> al;
    cout << "Adding elements..." << endl;
    al.add(1);
    al.add(2);
    al.add(3);
    al.add(4);
    al.add(5);
    cout << al.toString() << endl;
    
    cout << "Getting element at index 2: " << al.get(2) << endl;
    cout << "Setting element at index 2 to 99..." << endl;
    al.set(2, 99);
    cout << al.toString() << endl;
    
    cout << "Adding element 10 at index 1..." << endl;
    al.add(1, 10);
    cout << al.toString() << endl;
    
    cout << "Removing element at index 3..." << endl;
    al.remove(3);
    cout << al.toString() << endl;
    
    cout << "Size: " << al.getSize() << ", Capacity: " << al.getCapacity() << endl;
    
    // ==================== BINARY SEARCH TREE ====================
    cout << "\n\n=== TESTING BINARY SEARCH TREE (BST) ===" << endl;
    BST bst;
    
    cout << "Is empty: " << (bst.isEmpty() ? "true" : "false") << endl;
    
    cout << "\n--- Inserting values ---" << endl;
    int bstValues[] = {50, 30, 70, 20, 40, 60, 80};
    for (int value : bstValues) {
        bst.insert(value);
    }
    
    cout << "\nIs empty after insertions: " << (bst.isEmpty() ? "true" : "false") << endl;
    
    cout << "\n--- Traversals ---" << endl;
    cout << bst.preorder() << endl;
    cout << bst.inorder() << endl;
    cout << bst.postorder() << endl;
    
    cout << "\n--- Finding values ---" << endl;
    bst.find(60);
    bst.find(25);
    bst.find(50);
    
    cout << "\n--- Removing values ---" << endl;
    bst.remove(20);
    cout << bst.inorder() << endl;
    
    bst.remove(30);
    cout << bst.inorder() << endl;
    
    bst.remove(50);
    cout << bst.inorder() << endl;
    
    // ==================== PRIORITY QUEUE (HEAP) ====================
    cout << "\n\n=== TESTING PRIORITY QUEUE (HEAP) ===" << endl;
    Heap pq;
    
    // Test Min-Heap
    cout << "\n--- Testing Min-Heap ---" << endl;
    int values[] = {50, 30, 70, 20, 40, 60, 80};
    for (int value : values) {
        pq.enqueue(value);
        cout << "Enqueued: " << value << endl;
    }
    
    cout << pq.toStringMinHeap() << endl;
    cout << "Peek (min): " << pq.peekMin() << endl;
    cout << "Size: " << pq.getSize() << endl;
    
    cout << "\nDequeuing elements in order:" << endl;
    while (!pq.isEmpty()) {
        cout << "Dequeued: " << pq.dequeueMin() << endl;
    }
    
    // Test Max-Heap
    cout << "\n--- Testing Max-Heap ---" << endl;
    for (int value : values) {
        pq.enqueueMax(value);
        cout << "Enqueued: " << value << endl;
    }
    
    cout << pq.toStringMaxHeap() << endl;
    cout << "Peek (max): " << pq.peekMax() << endl;
    cout << "Size: " << pq.getSize() << endl;
    
    cout << "\nDequeuing elements in order (highest priority first):" << endl;
    while (!pq.isEmpty()) {
        cout << "Dequeued: " << pq.dequeueMax() << endl;
    }
    
    // Test clearing
    cout << "\n--- Testing Clear ---" << endl;
    for (int value : values) {
        pq.enqueue(value);
    }
    cout << pq.toStringMinHeap() << endl;
    pq.clear();
    cout << "Is empty after clear: " << (pq.isEmpty() ? "true" : "false") << endl;
    
    cout << "\n\n===============================================" << endl;
    cout << "       ALL TESTS COMPLETED SUCCESSFULLY      " << endl;
    cout << "===============================================" << endl;
    
    return 0;
}