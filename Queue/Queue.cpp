#include "../ArrayList/ArrayList.h"
#include "Queue.h"

/*
MADE BY: HA
This module implements the Queue (INT NUMBERS ONLY) DS using ArrayList the class got 3 methods:
1. Enqueue: to add the item in the queue.
2. Dequeue: to remove the first item enqueued in the queue.
3. toString: to return a string representation of the queue (for TUI).
(FIFO)
*/

void Queue::Enqueue(int value){
    Queuearr.add(value);
}

void Queue::Dequeue(){
    if (Queuearr.getSize() == 0)
        throw std::underflow_error("Cannot dequeue from empty queue");
    Queuearr.remove(0);
}

std::string Queue::toString(){
    if (Queuearr.getSize() == 0){
        return "Queue: [empty]";
    }
    std::string result = "Queue: [";
    for(int i = 0;i < Queuearr.getSize();++i){
        result += std::to_string(Queuearr.get(i));
        if (i < Queuearr.getSize() - 1){
            result += " ";
        }
    }
    result += "]";
    return result;
}