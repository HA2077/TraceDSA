#include <iostream>
#include "Circular Queue.h"
using namespace std;

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
        cout << "The queue is full. dequeue an element." << endl;
        return;
    }
    int insertpos = (Front + Qsize) % 10;
    Queuearr[insertpos] = value;
    cout << "Added element " << value << " to the queue in pos " << insertpos << endl;
    Qsize++;
}

void CircularQueue::Dequeue(){
    if (Qsize == 0){
        cout << "The queue is empty. Enqueue an element." << endl;
        return;
    }
    int Relement = Queuearr[Front];
    Queuearr[Front] = -1;   // Removed
    cout << "Removed Element " << Relement << " From the queue." << endl;
    Front = (Front + 1) % 10;
    Qsize--;
}

std::string CircularQueue::tostring(){
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