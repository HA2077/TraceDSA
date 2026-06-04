#include "DoublyLinkedList.h"
#include <sstream>

DoublyLinkedList::DoublyLinkedList(){
    head = nullptr;
    tail = nullptr;
}

void DoublyLinkedList::insertAtTheStart(int value){
    DNode* newNode = new DNode();
    newNode->data = value;
    newNode->next = head;
    newNode->prev = nullptr;

    if (head != nullptr)
        head->prev = newNode;
    head = newNode;

    if (tail == nullptr)
        tail = newNode;

    listSize++;
}

void DoublyLinkedList::insertAtTheEnd(int value){
    DNode* newNode = new DNode();
    newNode->data = value;
    newNode->next = nullptr;
    newNode->prev = tail;

    if (head == nullptr){
        head = newNode;
        tail = newNode;
        listSize++;
        return;
    }
    
    tail->next = newNode;
    tail = newNode;
    listSize++;
}

void DoublyLinkedList::deleteAtTheStart(){
    if (head == nullptr){
        throw std::underflow_error("Cannot delete from empty list");
    }

    DNode* ptr = head;
    if (head == tail){
        head = nullptr;
        tail = nullptr;
    }

    else{
        head = head->next;
        head->prev = nullptr;
    }

    delete ptr;
    listSize--;
}
void DoublyLinkedList::deleteAtTheEnd(){
    if (head == nullptr){
        throw std::underflow_error("Cannot delete from empty list");
    }

    if (head == tail){
        delete head;
        head = nullptr;
        tail = nullptr;
        listSize--;
        return;
    }

    DNode* ptr = tail;
    tail = tail->prev;
    tail->next = nullptr;
    delete ptr;
    listSize--;
}
void DoublyLinkedList::deleteWithVal(int value){
    if (head == nullptr){
        throw std::underflow_error("Cannot delete from empty list");
    }

    if (head->data == value){
        if (head == tail){
            delete head;
            head = nullptr;
            tail = nullptr;
        }
        else{
            DNode* ptr = head;
            head = head->next;
            head->prev = nullptr;
            delete ptr;
        }
        listSize--;
        return;
    }

    DNode* ptr = head;
    while (ptr != nullptr && ptr->data != value)
        ptr = ptr->next;

    if (ptr == nullptr)
        throw std::runtime_error("Value not found in list");

    if (ptr == tail){
        tail = tail->prev;
        tail->next = nullptr;
        delete ptr;
    }
    else{
        ptr->prev->next = ptr->next;
        ptr->next->prev = ptr->prev;
        delete ptr;
    }
    listSize--;
}

void DoublyLinkedList::clear(){
    DNode* ptr = head;
    while (ptr != nullptr){
        DNode* temp = ptr;
        ptr = ptr->next;
        delete temp;
    }
    head = nullptr;
    tail = nullptr;
    listSize = 0;
}

std::string DoublyLinkedList::toString(){
    if (head == nullptr){
        return "Doubly Linked List: [empty]";
    }

    std::string result = "Doubly Linked List: Forward: [";
    DNode* ptr = head;
    for (int i = 0; i < listSize; ++i){
        std::ostringstream oss;
        oss << ptr->data;
        result += oss.str();
        if (i < listSize - 1){
            result += " <-> ";
        }
        ptr = ptr->next;
    }
    result += "]";

    result += " Backward: [";
    ptr = tail;
    for (int i = 0; i < listSize; ++i){
        std::ostringstream oss;
        oss << ptr->data;
        result += oss.str();
        if (i < listSize - 1){
            result += " <-> ";
        }
        ptr = ptr->prev;
    }
    result += "]";

    return result;
}