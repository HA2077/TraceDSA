#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdexcept>
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
    void clear();
    std::string toString();
};

#endif // LINKEDLIST_H