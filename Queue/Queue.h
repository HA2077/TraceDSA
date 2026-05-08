#ifndef QUEUE_H
#define QUEUE_H

#include <iostream>
#include <stdexcept>
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

#endif // QUEUE_H