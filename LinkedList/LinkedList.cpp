#include "LinkedList.h"
#include <sstream>

/*
MADE BY: HA
This module implements the Linked List (INT NUMBERS ONLY) DS using a struct Node with 6 methods:
OPs:
1. insertAthestart: New node and head point to it.
2. insertAtTheEnd: New node and the pointer is null.
3. deleteAtTheStart: head poins to the next node and the first node is deleted.
4. deleteAtTheEnd: the past node points to null and the last node is deleted.
5. deletewithval: the past node points to the next node and the current node is deleted.
6. toString: to return a string representation of the list (for TUI).
*/

LinkedList::LinkedList(){
    head = nullptr;
}

void LinkedList::insertAthestart(int value){
    Node* newNode = new Node();
    newNode->data = value;
    newNode->next = head;
    head = newNode;
    listSize++;
}

void LinkedList::insertAtTheEnd(int value){
    Node* newNode = new Node();
    newNode->data = value;
    newNode->next = nullptr;

    if (head == nullptr){
        head = newNode;
        listSize++;
        return;
    }
    Node* ptr = head;
    while (ptr->next != nullptr)
        ptr = ptr->next;
    ptr->next = newNode;
    listSize++;
}

void LinkedList::deleteAtTheStart(){
    if (head == nullptr){
        throw std::underflow_error("Cannot delete from empty list");
    }
    Node* ptr = head;
    head = head->next;
    delete ptr;
    listSize--;
}

void LinkedList::deleteAtTheEnd(){
    if (head == nullptr){
        throw std::underflow_error("Cannot delete from empty list");
    }
    if (head->next == nullptr){
        delete head;
        head = nullptr;
        listSize--;
        return;
    }
    Node* ptr = head;
    while (ptr->next->next != nullptr){
        ptr = ptr->next;
    }
    delete ptr->next;
    ptr->next = nullptr;
    listSize--;
}

void LinkedList::deletewithval(int value){
    if (head == nullptr){
        throw std::underflow_error("Cannot delete from empty list");
    }
    Node* ptr = head;
    if (head->data == value){
        head = head->next;
        delete ptr;
        listSize--;
        return;
    }
    while (ptr->next != nullptr && ptr->next->data != value)
        ptr = ptr->next;

    if (ptr->next == nullptr)
        throw std::runtime_error("Value not found in list");

    Node* remove = ptr->next;
    ptr->next = remove->next;
    delete remove;
    listSize--;
}

void LinkedList::clear(){
    Node* ptr = head;
    while (ptr != nullptr){
        Node* temp = ptr;
        ptr = ptr->next;
        delete temp;
    }
    head = nullptr;
    listSize = 0;
}

std::string LinkedList::toString(){
    if (head == nullptr){
        return "List: [empty]";
    }
    
    std::string result = "List: [";
    Node* ptr = head;
    for (int i = 0;i < listSize;++i){
        std::ostringstream oss;
        oss << ptr->data;
        result += oss.str();
        if (i < listSize - 1){
            result += " -> ";
        }
        ptr = ptr->next;
    }
    result += "]";
    return result;
}