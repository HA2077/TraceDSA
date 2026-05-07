#ifndef QUEUEASLINKEDLIST_H
#define QUEUEASLINKEDLIST_H

#include <iostream>

struct LNode{
    int data;
    LNode* next;
};

class QueueAsLinkedList{
private:
    LNode* head;
    int listSize = 0;
public:
    QueueAsLinkedList();
    void Enqueue(int value);
    void Dequeue();
    void printList();
};

#include "Queue as LinkedList.cpp"
#endif // QUEUEASLINKEDLIST_H