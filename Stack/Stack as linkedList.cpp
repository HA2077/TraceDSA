#include <iostream>
using namespace std;

/*
MADE BY: HA
This module implements the Stack (INT NUMBERS ONLY) DS using a linked list the class got 3 methods:
1. push: to add an element to the top of the stack.
2. pop: to remove the top element from the stack.
3. peek: to return the top element without removing it.
4. printStack: to print the elements in the stack, the stack size and the top element.
(LIFO)
*/

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
        void push(int value){
            SNode* newnode = new SNode();
            if (head == nullptr){
                newnode->data = value;
                newnode->next = nullptr;
                head = newnode;
                top = value;
                stacksize++;
                cout << "Pushed: " << value << " to the stack." << endl;
                return;
            }
            newnode->data = value;
            newnode->next = head;
            head = newnode;
            top = value;
            stacksize++;
            cout << "Pushed: " << value << " to the stack." << endl;
            return;
        }
        void pop(){
            if (stacksize == 0){
            cout << "The stack is empty, Push an element first!" << endl;
            return;
            }
            SNode* ptr = head;
            head = head->next;
            delete (ptr);
            stacksize--;
            if (stacksize > 0)
                top = head->data;
            else
                top = -1;
            cout << "Popped The Top Element From the stack." << endl;
            return;
        }
        int peek(){
            return top;
        }
        void printStack(){
            if (head == nullptr){
                cout << "The Stack is empty." << endl;
                return;
            }
            cout << "Your Stack: " << endl;
            SNode* ptr = head;
            cout << "Head -> ";
            for (int i = 0;i < stacksize;++i){
                cout << ptr->data << " -> ";
                ptr = ptr->next;
            }
            cout << "NULL" << endl;
            cout << "Stack size: " << stacksize << endl;
            cout << endl;
        }
};