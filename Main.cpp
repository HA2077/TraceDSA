#include <iostream>
#include "Stack/Stack as array.cpp"
#include "Queue/Queue as array.cpp"
#include "LinkedList/DoublyLinkedList.cpp"
#include "ArrayList/ArrayList.h"
using namespace std;

int main(){
    cout << "=== Testing Stack ===" << endl;
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
    
    cout << "\n=== Testing Queue ===" << endl;
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
    
    // Test adding more elements to verify dynamic resizing
    cout << "\n=== Testing Queue Resizing ===" << endl;
    for(int i = 0; i < 15; i++)
        q.Enqueue(i * 10);
    q.Display();
    
    return 0;
}