#ifndef QUEUE_H
#define QUEUE_H

#include <iostream>
#include "../ArrayList/ArrayList.h"
#include <string>

class Queue{
private:
    ArrayList<int> Queuearr;
public:
    void Enqueue(int value);
    void Dequeue();
    std::string toString();
};

#include "Queue as array.cpp"
#endif // QUEUE_H