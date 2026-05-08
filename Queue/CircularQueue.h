#ifndef CIRCULAR_QUEUE_H
#define CIRCULAR_QUEUE_H

#include <iostream>
#include <string>

class CircularQueue{
private:
    int Qsize = 0, Front = 0;
    int Queuearr[10];
public:
    void Enqueue(int value);
    void Dequeue();
    std::string tostring();
};

#endif