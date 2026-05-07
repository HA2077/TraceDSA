#ifndef DOUBLYLINKEDLIST_H
#define DOUBLYLINKEDLIST_H

#include <iostream>

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
    void printList();
};

#include "DoublyLinkedList.cpp"
#endif // DOUBLYLINKEDLIST_H