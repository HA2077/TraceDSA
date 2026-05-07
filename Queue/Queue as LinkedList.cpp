#include <iostream>
#include "QueueAsLinkedList.h"
#include <sstream>
using namespace std;

/*
MADE BY: HA
This module implements the Queue (INT NUMBERS ONLY) DS using a linked list the class got 3 methods:
1. Enqueue: to add the item in the queue.
2. Dequeue: to remove the first item enqueued in the queue.
3. toString: to return a string representation of the queue (for TUI).
(FIFO)
*/

QueueAsLinkedList::QueueAsLinkedList(){
    head = nullptr;
}

void QueueAsLinkedList::Enqueue(int value){
    LNode* newNode = new LNode();
    newNode->data = value;
    newNode->next = nullptr;

    if (head == nullptr){
        head = newNode;
        listSize++;
        cout << "Inserted: " << value << " at the end of the Queue." << endl;
        return;
    }
    LNode* ptr = head;
    while (ptr->next != nullptr)
        ptr = ptr->next;
    ptr->next = newNode;
    listSize++;
    cout << "Inserted: " << value << " at the end of the Queue." << endl;
}

void QueueAsLinkedList::Dequeue(){
    if (head == nullptr){
        throw std::underflow_error("Cannot dequeue from empty queue");
    }
    LNode* ptr = head;
    head = head->next;
    delete ptr;
    listSize--;
    cout << "Deleted the first element from the Queue." << endl;
}

std::string QueueAsLinkedList::toString(){
    if (head == nullptr){
        return "Queue: [empty]";
    }
    std::string result = "Queue: [";
    LNode* ptr = head;
    for (int i = 0;i < listSize;++i){
        std::ostringstream oss;
        oss << ptr->data;
        result += oss.str();
        if (i < listSize - 1){
            result += " -> ";
        }
        ptr = ptr->next;
    }
    result += "]";
    return result;
}