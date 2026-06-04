#ifndef QUEUEASLINKEDLIST_H
#define QUEUEASLINKEDLIST_H

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
    void clear();
    std::string toString();
};

#endif // QUEUEASLINKEDLIST_H