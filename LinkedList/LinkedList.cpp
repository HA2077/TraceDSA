#include "LinkedList.h"
#include <iostream>
using namespace std;

/*
MADE BY: HA
This module implements the Linked List (INT NUMBERS ONLY) DS using a struct Node with 6 methods:
OPs:
1. insertAthestart: New node and head point to it.
2. insertAtTheEnd: New node and the pointer is null.
3. deleteAtTheStart: head poins to the next node and the first node is deleted.
4. deleteAtTheEnd: the past node points to null and the last node is deleted.
5. deletewithval: the past node points to the next node and the current node is deleted.
6. printList: to print the elements in the list and the list size.
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
    cout << "Inserted: " << value << " at the start of the list." << endl;
}

void LinkedList::insertAtTheEnd(int value){
    Node* newNode = new Node();
    newNode->data = value;
    newNode->next = nullptr;

    if (head == nullptr){
        head = newNode;
        listSize++;
        cout << "Inserted: " << value << " at the end of the list." << endl;
        return;
    }
    Node* ptr = head;
    while (ptr->next != nullptr)
        ptr = ptr->next;
    ptr->next = newNode;
    listSize++;
    cout << "Inserted: " << value << " at the end of the list." << endl;
}

void LinkedList::deleteAtTheStart(){
    if (head == nullptr){
        cout << "The list is empty, Insert an element first!" << endl;
        return;
    }
    Node* ptr = head;
    head = head->next;
    delete ptr;
    listSize--;
    cout << "Deleted the first element from the list." << endl;
}

void LinkedList::deleteAtTheEnd(){
    if (head == nullptr){
        cout << "The list is empty, Insert an element first!" << endl;
        return;
    }
    if (head->next == nullptr){
        delete head;
        head = nullptr;
        listSize--;
        cout << "Deleted the last element from the list." << endl;
        return;
    }
    Node* ptr = head;
    while (ptr->next->next != nullptr){
        ptr = ptr->next;
    }
    delete ptr->next;
    ptr->next = nullptr;
    listSize--;
    cout << "Deleted the last element from the list." << endl;
}

void LinkedList::deletewithval(int value){
    if (head == nullptr){
        cout << "The list is empty, Insert an element first!" << endl;
        return;
    }
    Node* ptr = head;
    if (head->data == value){
        head = head->next;
        delete ptr;
        listSize--;
        cout << "Deleted: " << value << " from the list." << endl;
        return;
    }
    while (ptr->next != nullptr && ptr->next->data != value)
        ptr = ptr->next;

    if (ptr->next == nullptr){
        cout << "Value: " << value << " not found in the list." << endl;
        return;
    }

    Node* remove = ptr->next;
    ptr->next = remove->next;
    delete remove;
    listSize--;
    cout << "Deleted: " << value << " from the list." << endl;
}

void LinkedList::printList(){
    if (head == nullptr){
        cout << "The list is empty." << endl;
        return;
    }
    cout << "Your List: " << endl;
    Node* ptr = head;
    cout << "Head -> ";
    for (int i = 0;i < listSize;++i){
        cout << ptr->data << " -> ";
        ptr = ptr->next;
    }
    cout << "NULL" << endl;
    cout << "List size: " << listSize << endl;
    cout << endl;
}