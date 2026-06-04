#ifndef DOUBLYLINKEDLIST_H
#define DOUBLYLINKEDLIST_H

#include <stdexcept>
#include <string>

struct DNode {
    int data;
    DNode* next;
    DNode* prev;
};

class DoublyLinkedList{
private:
    DNode* head;
    DNode* tail;
    int listSize = 0;
public:
    DoublyLinkedList();
    void insertAtTheStart(int value);
    void insertAtTheEnd(int value);
    void deleteAtTheStart();
    void deleteAtTheEnd();
    void deleteWithVal(int value);
    void clear();
    std::string toString();
};

#endif // DOUBLYLINKEDLIST_H