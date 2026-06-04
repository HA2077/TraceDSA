#include "CircularQueue.h"
#include <stdexcept>

/*
MADE BY: HA
This module implements the Queue (INT NUMBERS ONLY) DS using a arrays (array of 10 numbers) the class got 3 methods:
1. Enqueue: to add the item in the queue.
2. Dequeue: to remove the first item enqueued in the queue.
3. Display: to print the elements of the queue.
(FIFO)
*/

void CircularQueue::Enqueue(int value){
    if (Qsize == 10){
        return;
    }
    int insertpos = (Front + Qsize) % 10;
    Queuearr[insertpos] = value;
    Qsize++;
}

void CircularQueue::Dequeue(){
    if (Qsize == 0)
        throw std::underflow_error("Cannot dequeue from empty queue");
    Queuearr[Front] = -1;   // Removed 
    Front = (Front + 1) % 10;
    Qsize--;
}

void CircularQueue::clear(){
    Qsize = 0;
    Front = 0;
    for (int i = 0; i < 10;++i){
        Queuearr[i] = -1;
    }
}

std::string CircularQueue::toString(){
    if (Qsize == 0){
        return "Queue: [empty]";
    }
    int checker = Front;
    std::string result = "Queue: [";
    for(int i = 0;i < Qsize;++i){
        if (checker == 10)
                checker = 0;
            result += std::to_string(Queuearr[checker]) + " ";
            checker++;
        }
        result += "]";
        return result;
    }