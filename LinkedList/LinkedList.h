#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <iostream>
#include <string>

struct Node{
    int data;
    Node* next;
};

class LinkedList{
private:
    Node* head;
    int listSize = 0;
public:
    LinkedList();
    void insertAthestart(int value);
    void insertAtTheEnd(int value);
    void deleteAtTheStart();
    void deleteAtTheEnd();
    void deletewithval(int value);
    std::string toString();
};

#include "LinkedList.cpp"
#endif // LINKEDLIST_H