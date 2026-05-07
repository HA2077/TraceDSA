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
4. toString: to return a string representation of the stack (for TUI).
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

std::string Stack::toString(){
    if (stacksize == 0){
        return "Stack: [empty]";
    }
    
    std::string result = "Stack: [";
    for (int i = 0;i < stacksize;++i){
        result += std::to_string(stack.get(i));
        if (i < stacksize - 1){
            result += " ";
        }
    }
    result += "]";
    return result;
}