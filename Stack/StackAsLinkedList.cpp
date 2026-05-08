#include "StackAsLinkedList.h"
#include <sstream>

/*
MADE BY: HA
This module implements the Stack (INT NUMBERS ONLY) DS using a linked list the class got 3 methods:
1. push: to add an element to the top of the stack.
2. pop: to remove the top element from the stack.
3. peek: to return the top element without removing it.
4. toString: to return a string representation of the stack (for TUI).
(LIFO)
*/

void StackAsLinkedList::push(int value){
    SNode* newnode = new SNode();
    if (head == nullptr){
        newnode->data = value;
        newnode->next = nullptr;
        head = newnode;
        top = value;
        stacksize++;
        return;
    }
    newnode->data = value;
    newnode->next = head;
    head = newnode;
    top = value;
    stacksize++;
    return;
}

void StackAsLinkedList::pop(){
    if (stacksize == 0){
        throw std::underflow_error("Cannot pop from empty stack");
    }
    SNode* ptr = head;
    head = head->next;
    delete (ptr);
    stacksize--;
    if (stacksize > 0)
        top = head->data;
    else
        top = -1;
    return;
}

int StackAsLinkedList::peek(){
    if (stacksize == 0)
        throw std::underflow_error("Cannot peek from empty stack");
    
    return top;
}

std::string StackAsLinkedList::toString(){
    if (head == nullptr){
        return "Stack: [empty]";
    }
    
    std::string result = "Stack: [";
    SNode* ptr = head;
    for (int i = 0;i < stacksize;++i){
        std::ostringstream oss;
        oss << ptr->data;
        result += oss.str();
        if (i < stacksize - 1){
            result += " -> ";
        }
        ptr = ptr->next;
    }
    result += "]";
    return result;
}