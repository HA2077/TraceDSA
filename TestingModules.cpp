#include <iostream>
#include "Stack/Stack.h"
#include "Stack/StackAsLinkedList.h"
#include "Queue/Queue.h"
#include "Queue/QueueAsLinkedList.h"
#include "Queue/CircularQueue.h"
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
     cout << "Pushed: 10 to the stack." << endl;
     s.push(20);
     cout << "Pushed: 20 to the stack." << endl;
     s.push(30);
     cout << "Pushed: 30 to the stack." << endl;
     cout << s.toString() << endl;
     cout << "Peek: " << s.peek() << endl;
     s.pop();
     cout << "Popped The Top Element From the stack." << endl;
     cout << s.toString() << endl;
     s.pop();
     cout << "Popped The Top Element From the stack." << endl;
     cout << s.toString() << endl;
     s.pop();
     cout << "Popped The Top Element From the stack." << endl;
     cout << s.toString() << endl; // Should be empty

     // Test underflow
     cout << "\n--- Testing Stack Underflow ---" << endl;
     try {
         s.pop();
     } catch (const std::underflow_error& e) {
         cout << "Caught expected error: " << e.what() << endl;
     }
    
    // ==================== STACK AS LINKED LIST ====================
    cout << "\n\n=== TESTING STACK (LINKED LIST IMPLEMENTATION) ===" << endl;
     StackAsLinkedList sll;
     sll.push(100);
     cout << "Pushed: 100 to the stack." << endl;
     sll.push(200);
     cout << "Pushed: 200 to the stack." << endl;
     sll.push(300);
     cout << "Pushed: 300 to the stack." << endl;
     cout << sll.toString() << endl;
     cout << "Peek: " << sll.peek() << endl;
     sll.pop();
     cout << "Popped The Top Element From the stack." << endl;
     cout << sll.toString() << endl;
     sll.pop();
     cout << "Popped The Top Element From the stack." << endl;
     cout << sll.toString() << endl;
     sll.pop();
     cout << "Popped The Top Element From the stack." << endl;
     cout << sll.toString() << endl; // Should be empty

     // Test underflow
     cout << "\n--- Testing StackAsLinkedList Underflow ---" << endl;
     try {
         sll.pop();
     } catch (const std::underflow_error& e) {
         cout << "Caught expected error: " << e.what() << endl;
     }
    
    // ==================== QUEUE AS ARRAY ====================
    cout << "\n\n=== TESTING QUEUE (ARRAY IMPLEMENTATION) ===" << endl;
     Queue q;
     q.Enqueue(5);
     cout << "Added element 5 to the queue" << endl;
     q.Enqueue(15);
     cout << "Added element 15 to the queue" << endl;
     q.Enqueue(25);
     cout << "Added element 25 to the queue" << endl;
     cout << q.toString() << endl;
     q.Dequeue();
     cout << "Removed Element 5 From the queue." << endl;
     cout << q.toString() << endl;
     q.Dequeue();
     cout << "Removed Element 15 From the queue." << endl;
     cout << q.toString() << endl;
     q.Dequeue();
     cout << "Removed Element 25 From the queue." << endl;
     cout << q.toString() << endl; // Should be empty

     // Test underflow
     cout << "\n--- Testing Queue Underflow ---" << endl;
     try {
         q.Dequeue();
     } catch (const std::underflow_error& e) {
         cout << "Caught expected error: " << e.what() << endl;
     }

     cout << "\n--- Testing Queue Array Resizing ---" << endl;
     for(int i = 0; i < 12; i++) {
         q.Enqueue(i * 10);
         cout << "Added element " << i*10 << " to the queue" << endl;
     }
     cout << q.toString() << endl;
    
    // ==================== QUEUE AS LINKED LIST ====================
    cout << "\n\n=== TESTING QUEUE (LINKED LIST IMPLEMENTATION) ===" << endl;
     QueueAsLinkedList qll;
     qll.Enqueue(7);
     cout << "Inserted: 7 at the end of the Queue." << endl;
     qll.Enqueue(14);
     cout << "Inserted: 14 at the end of the Queue." << endl;
     qll.Enqueue(21);
     cout << "Inserted: 21 at the end of the Queue." << endl;
     cout << qll.toString() << endl;
     qll.Dequeue();
     cout << "Deleted the first element from the Queue." << endl;
     cout << qll.toString() << endl;
     qll.Dequeue();
     cout << "Deleted the first element from the Queue." << endl;
     cout << qll.toString() << endl;
     qll.Dequeue();
     cout << "Deleted the first element from the Queue." << endl;
     cout << qll.toString() << endl; // Should be empty

     // Test underflow
     cout << "\n--- Testing QueueAsLinkedList Underflow ---" << endl;
     try {
         qll.Dequeue();
     } catch (const std::underflow_error& e) {
         cout << "Caught expected error: " << e.what() << endl;
     }
    
     // ==================== CIRCULAR QUEUE ====================
     cout << "\n\n=== TESTING CIRCULAR QUEUE ===" << endl;
     CircularQueue cq;
     cq.Enqueue(5);
     cout << "Added element 5 to the circular queue" << endl;
     cq.Enqueue(15);
     cout << "Added element 15 to the circular queue" << endl;
     cq.Enqueue(25);
     cout << "Added element 25 to the circular queue" << endl;
     cout << cq.toString() << endl;
     cq.Dequeue();
     cout << "Removed Element 5 From the queue." << endl;
     cout << cq.toString() << endl;
     cq.Dequeue();
     cout << "Removed Element 15 From the queue." << endl;
     cout << cq.toString() << endl;
     cq.Dequeue();
     cout << "Removed Element 25 From the queue." << endl;
     cout << cq.toString() << endl; // Should be empty

     // Test full queue
     cout << "\n--- Testing Circular Queue Full ---" << endl;
     CircularQueue cq2;
     for (int i=0; i<10; i++) {
         cq2.Enqueue(i);
         cout << "Enqueued " << i << " to circular queue" << endl;
     }
     cout << "Queue is now full (10/10)" << endl;
     cq2.Enqueue(100); // No-op (full)
     cout << "Tried to enqueue 100 (full queue, no-op)" << endl;

     // ==================== SINGLY LINKED LIST ====================
     cout << "\n\n=== TESTING SINGLY LINKED LIST ===" << endl;
     LinkedList ll;
     cout << "Inserting at start..." << endl;
     ll.insertAthestart(50);
     cout << "Inserted: 50 at the start of the list." << endl;
     ll.insertAthestart(40);
     cout << "Inserted: 40 at the start of the list." << endl;
     ll.insertAthestart(30);
     cout << "Inserted: 30 at the start of the list." << endl;
     cout << "Inserting at end..." << endl;
     ll.insertAtTheEnd(60);
     cout << "Inserted: 60 at the end of the list." << endl;
     ll.insertAtTheEnd(70);
     cout << "Inserted: 70 at the end of the list." << endl;
     cout << ll.toString() << endl;
     cout << "Deleting at start..." << endl;
     ll.deleteAtTheStart();
     cout << "Deleted the first element from the list." << endl;
     cout << ll.toString() << endl;
     cout << "Deleting at end..." << endl;
     ll.deleteAtTheEnd();
     cout << "Deleted the last element from the list." << endl;
     cout << ll.toString() << endl;
     cout << "Deleting element with value 50..." << endl;
     ll.deletewithval(50);
     cout << "Deleted: 50 from the list." << endl;
     cout << ll.toString() << endl;

     // Test underflow
     cout << "\n--- Testing LinkedList Underflow ---" << endl;
     try {
         ll.deleteAtTheStart();
         ll.deleteAtTheStart();
         ll.deleteAtTheStart(); // Should throw
     } catch (const std::underflow_error& e) {
         cout << "Caught expected error: " << e.what() << endl;
     }
    
     // ==================== DOUBLY LINKED LIST ====================
     cout << "\n\n=== TESTING DOUBLY LINKED LIST ===" << endl;
     DoublyLinkedList dll;
     cout << "Inserting at start..." << endl;
     dll.insertAtTheStart(100);
     cout << "Inserted: 100 at the start of the list." << endl;
     dll.insertAtTheStart(90);
     cout << "Inserted: 90 at the start of the list." << endl;
     dll.insertAtTheStart(80);
     cout << "Inserted: 80 at the start of the list." << endl;
     cout << "Inserting at end..." << endl;
     dll.insertAtTheEnd(110);
     cout << "Inserted: 110 at the end of the list." << endl;
     dll.insertAtTheEnd(120);
     cout << "Inserted: 120 at the end of the list." << endl;
     cout << dll.toString() << endl;
     cout << "Deleting at start..." << endl;
     dll.deleteAtTheStart();
     cout << "Deleted the first element from the list." << endl;
     cout << dll.toString() << endl;
     cout << "Deleting at end..." << endl;
     dll.deleteAtTheEnd();
     cout << "Deleted the last element from the list." << endl;
     cout << dll.toString() << endl;

     // Test underflow
     cout << "\n--- Testing DoublyLinkedList Underflow ---" << endl;
     try {
         dll.deleteAtTheStart();
         dll.deleteAtTheStart();
         dll.deleteAtTheStart(); // Should throw
     } catch (const std::underflow_error& e) {
         cout << "Caught expected error: " << e.what() << endl;
     }
    
     // ==================== ARRAY LIST ====================
     cout << "\n\n=== TESTING ARRAY LIST (DYNAMIC) ===" << endl;
     ArrayList<int> al;
     cout << "Adding elements..." << endl;
     for (int i=1; i<=5; i++) {
         al.add(i);
         cout << "Added " << i << ", Size: " << al.getSize() << ", Capacity: " << al.getCapacity() << endl;
     }
     cout << al.toString() << endl;
     
     cout << "Getting element at index 2: " << al.get(2) << endl;
     cout << "Setting element at index 2 to 99..." << endl;
     al.set(2, 99);
     cout << al.toString() << endl;
     
     cout << "Adding element 10 at index 1..." << endl;
     al.add(1, 10);
     cout << "Size: " << al.getSize() << ", Capacity: " << al.getCapacity() << endl;
     cout << al.toString() << endl;
     
     cout << "Removing element at index 3..." << endl;
     al.remove(3);
     cout << "Size: " << al.getSize() << ", Capacity: " << al.getCapacity() << endl;
     cout << al.toString() << endl;
     
     // Test resizing
     cout << "\n--- Testing ArrayList Resizing ---" << endl;
     ArrayList<int> al2;
     for (int i=0; i<20; i++) {
         al2.add(i);
         if (i % 5 == 0) {
             cout << "Added " << i << ", Size: " << al2.getSize() << ", Capacity: " << al2.getCapacity() << endl;
         }
     }
     cout << "Final Size: " << al2.getSize() << ", Capacity: " << al2.getCapacity() << endl;
    
     // ==================== BINARY SEARCH TREE ====================
     cout << "\n\n=== TESTING BINARY SEARCH TREE (BST) ===" << endl;
     BST bst;
     
     cout << "Is empty: " << (bst.isEmpty() ? "true" : "false") << endl;
     
     cout << "\n--- Inserting values ---" << endl;
     int bstValues[] = {50, 30, 70, 20, 40, 60, 80};
     for (int value : bstValues) {
         bst.insert(value);
         cout << "Inserted: " << value << " into the BST." << endl;
     }
     
     cout << "\nIs empty after insertions: " << (bst.isEmpty() ? "true" : "false") << endl;
     
     cout << "\n--- Traversals ---" << endl;
     cout << bst.preorder() << endl;
     cout << bst.inorder() << endl;
     cout << bst.postorder() << endl;
     
     cout << "\n--- Finding values ---" << endl;
     bool found = bst.find(60);
     cout << "Value 60 " << (found ? "found" : "not found") << " in the BST." << endl;
     found = bst.find(25);
     cout << "Value 25 " << (found ? "found" : "not found") << " in the BST." << endl;
     found = bst.find(50);
     cout << "Value 50 " << (found ? "found" : "not found") << " in the BST." << endl;
     
     cout << "\n--- Removing values ---" << endl;
     bst.remove(20);
     cout << "Removed: 20 from the BST." << endl;
     cout << bst.inorder() << endl;
     
     bst.remove(30);
     cout << "Removed: 30 from the BST." << endl;
     cout << bst.inorder() << endl;
     
     bst.remove(50);
     cout << "Removed: 50 from the BST." << endl;
     cout << bst.inorder() << endl;

     // Test BST clear
     cout << "\n--- Testing BST Clear ---" << endl;
     bst.clear();
     cout << "BST cleared." << endl;
     cout << "Is empty after clear: " << (bst.isEmpty() ? "true" : "false") << endl;
    
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