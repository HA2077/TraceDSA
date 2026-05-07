#ifndef QUEUEASLINKEDLIST_H
#define QUEUEASLINKEDLIST_H

#include <iostream>
#include <stdexcept>
#include <string>

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
    std::string toString();
};

#include "Queue as LinkedList.cpp"
#endif // QUEUEASLINKEDLIST_H