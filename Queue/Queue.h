#ifndef QUEUE_H
#define QUEUE_H

#include <stdexcept>
#include "../ArrayList/ArrayList.h"
#include <string>

class Queue{
private:
    ArrayList<int> Queuearr;
public:
    void Enqueue(int value);
    void Dequeue();
    void clear();
    std::string toString();
};

#endif // QUEUE_H