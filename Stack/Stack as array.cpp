#include <iostream>
#include "../ArrayList/ArrayList.h"
#include "Stack.h"
using namespace std;

/*
MADE BY: HA
This module implements the Stack (INT NUMBERS ONLY) DS using a ArrayList the class got 3 methods:
1. push: to add an element to the top of the stack.
2. pop: to remove the top element from the stack.
3. peek: to return the top element without removing it.
4. printStack: to print the elements in the stack, the stack size and the top element.
(LIFO)
*/

void Stack::push(int value){
    stack.add(value);
    top = value;
    stacksize++;
    cout << "Pushed: " << value << " to the stack." << endl;
}

void Stack::pop(){
    if (stacksize == 0){
        cout << "The stack is empty, Push an element first!" << endl;
        return;
    }

    stack.remove(stacksize - 1);
    stacksize--;

    if(stacksize > 0){
        top = stack.get(stacksize - 1);
        cout << "Popped The Top Element From the stack." << endl;
        return;
    }
    else    top = -1;
}

int Stack::peek(){
    if (stacksize == 0){
        cout << "The stack is empty, Push an element first!" << endl;
        return -1;
    }
    return top;
}

void Stack::printStack(){
    cout << "Your Stack: " << endl;
    for (int i = 0;i < stacksize;++i)
        cout << stack.get(i) << " ";
    cout << endl;
    cout << "Stack size: " << stacksize << endl;
    cout << "Top element: " << top << endl;
    cout << endl;
}