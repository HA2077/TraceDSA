#ifndef STACKASLINKEDLIST_H
#define STACKASLINKEDLIST_H

#include <stdexcept>
#include <string>

struct SNode{
    int data;
    SNode* next;
};

class StackAsLinkedList{
private:
    SNode* head = nullptr;
    int top = -1;
    int stacksize = 0;
public:
    void push(int value);
    void pop();
    int peek();
    std::string toString();
};

#endif // STACKASLINKEDLIST_H