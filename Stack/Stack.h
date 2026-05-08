#ifndef STACK_H
#define STACK_H

#include <iostream>
#include <stdexcept>
#include "../ArrayList/ArrayList.h"
#include <string>

class Stack{
private:
    ArrayList<int> stack;
public:
    int top;
    int stacksize = 0;

    void push(int value);
    void pop();
    int peek();
    std::string toString();
};

#endif // STACK_H