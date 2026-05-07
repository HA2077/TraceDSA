#include <iostream>
#include "Stack/Stack.h"
#include "Stack/StackAsLinkedList.h"
#include "Queue/Queue.h"
#include "Queue/QueueAsLinkedList.h"
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
    s.printStack();
    cout << "Peek: " << s.peek() << endl;
    s.pop();
    s.printStack();
    s.pop();
    s.printStack();
    s.pop();
    s.printStack(); // Should be empty
    
    // ==================== STACK AS LINKED LIST ====================
    cout << "\n\n=== TESTING STACK (LINKED LIST IMPLEMENTATION) ===" << endl;
    StackAsLinkedList sll;
    sll.push(100);
    sll.push(200);
    sll.push(300);
    sll.printStack();
    cout << "Peek: " << sll.peek() << endl;
    sll.pop();
    sll.printStack();
    sll.pop();
    sll.printStack();
    sll.pop();
    sll.printStack(); // Should be empty
    
    // ==================== QUEUE AS ARRAY ====================
    cout << "\n\n=== TESTING QUEUE (ARRAY IMPLEMENTATION) ===" << endl;
    Queue q;
    q.Enqueue(5);
    q.Enqueue(15);
    q.Enqueue(25);
    q.Display();
    q.Dequeue();
    q.Display();
    q.Dequeue();
    q.Display();
    q.Dequeue();
    q.Display(); // Should be empty
    
    cout << "\n--- Testing Queue Array Resizing ---" << endl;
    for(int i = 0; i < 12; i++)
        q.Enqueue(i * 10);
    q.Display();
    
    // ==================== QUEUE AS LINKED LIST ====================
    cout << "\n\n=== TESTING QUEUE (LINKED LIST IMPLEMENTATION) ===" << endl;
    QueueAsLinkedList qll;
    qll.Enqueue(7);
    qll.Enqueue(14);
    qll.Enqueue(21);
    qll.printList();
    qll.Dequeue();
    qll.printList();
    qll.Dequeue();
    qll.printList();
    qll.Dequeue();
    qll.printList(); // Should be empty
    
    
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
    ll.printList();
    cout << "Deleting at start..." << endl;
    ll.deleteAtTheStart();
    ll.printList();
    cout << "Deleting at end..." << endl;
    ll.deleteAtTheEnd();
    ll.printList();
    cout << "Deleting element with value 50..." << endl;
    ll.deletewithval(50);
    ll.printList();
    
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
    dll.printList();
    cout << "Deleting at start..." << endl;
    dll.deleteAtTheStart();
    dll.printList();
    cout << "Deleting at end..." << endl;
    dll.deleteAtTheEnd();
    dll.printList();
    
    // ==================== ARRAY LIST ====================
    cout << "\n\n=== TESTING ARRAY LIST (DYNAMIC) ===" << endl;
    ArrayList<int> al;
    cout << "Adding elements..." << endl;
    al.add(1);
    al.add(2);
    al.add(3);
    al.add(4);
    al.add(5);
    al.print();
    
    cout << "Getting element at index 2: " << al.get(2) << endl;
    cout << "Setting element at index 2 to 99..." << endl;
    al.set(2, 99);
    al.print();
    
    cout << "Adding element 10 at index 1..." << endl;
    al.add(1, 10);
    al.print();
    
    cout << "Removing element at index 3..." << endl;
    al.remove(3);
    al.print();
    
    cout << "Size: " << al.getSize() << ", Capacity: " << al.getCapacity() << endl;
    
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
    
    pq.displayMinHeap();
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
    
    pq.displayMaxHeap();
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
    pq.displayMinHeap();
    pq.clear();
    cout << "Is empty after clear: " << (pq.isEmpty() ? "true" : "false") << endl;
    
    cout << "\n\n===============================================" << endl;
    cout << "       ALL TESTS COMPLETED SUCCESSFULLY      " << endl;
    cout << "===============================================" << endl;
    
    return 0;
}