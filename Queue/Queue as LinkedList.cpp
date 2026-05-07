#include <iostream>
#include "QueueAsLinkedList.h"
using namespace std;

/*
MADE BY: HA
This module implements the Queue (INT NUMBERS ONLY) DS using a linked list the class got 3 methods:
1. Enqueue: to add the item in the queue.
2. Dequeue: to remove the first item enqueued in the queue.
3. Display: to print the elements of the queue.
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
        cout << "The Queue is empty, Insert an element first!" << endl;
        return;
    }
    LNode* ptr = head;
    head = head->next;
    delete ptr;
    listSize--;
    cout << "Deleted the first element from the Queue." << endl;
}

void QueueAsLinkedList::printList(){
    if (head == nullptr){
        cout << "The Queue is empty." << endl;
        return;
    }
    cout << "Your Queue: " << endl;
    LNode* ptr = head;
    cout << "Head -> ";
    for (int i = 0;i < listSize;++i){
        cout << ptr->data << " -> ";
        ptr = ptr->next;
    }
    cout << "NULL" << endl;
    cout << "Queue size: " << listSize << endl;
    cout << endl;
}