#include "DoublyLinkedList.h"
#include <iostream>
#include <sstream>
using namespace std;

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
    cout << "Inserted: " << value << " at the start of the list." << endl;
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
        cout << "Inserted: " << value << " at the end of the list." << endl;
        return;
    }
    
    tail->next = newNode;
    tail = newNode;
    listSize++;
    cout << "Inserted: " << value << " at the end of the list." << endl;
}

void DoublyLinkedList::deleteAtTheStart(){
    if (head == nullptr){
        cout << "The list is empty, Insert an element first!" << endl;
        return;
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
    cout << "Deleted the first element from the list." << endl;
}
void DoublyLinkedList::deleteAtTheEnd(){
    if (head == nullptr){
        cout << "The list is empty, Insert an element first!" << endl;
        return;
    }

    if (head == tail){
        delete head;
        head = nullptr;
        tail = nullptr;
        listSize--;
        cout << "Deleted the last element from the list." << endl;
        return;
    }

    DNode* ptr = tail;
    tail = tail->prev;
    tail->next = nullptr;
    delete ptr;
    listSize--;
    cout << "Deleted the last element from the list." << endl;
}
void DoublyLinkedList::deleteWithVal(int value){
    if (head == nullptr){
        cout << "The list is empty, Insert an element first!" << endl;
        return;
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
        cout << "Deleted: " << value << " from the list." << endl;
        return;
    }

    DNode* ptr = head;
    while (ptr != nullptr && ptr->data != value)
        ptr = ptr->next;

    if (ptr == nullptr){
        cout << "Value: " << value << " not found in the list." << endl;
        return;
    }

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
    cout << "Deleted: " << value << " from the list." << endl;
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