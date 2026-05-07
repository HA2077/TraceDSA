#ifndef STACK_H
#define STACK_H

#include <iostream>
#include "../ArrayList/ArrayList.h"

class Stack{
private:
    ArrayList<int> stack;
public:
    int top;
    int stacksize = 0;

    void push(int value);
    void pop();
    int peek();
    void printStack();
};

#include "Stack as array.cpp"
#endif // STACK_H