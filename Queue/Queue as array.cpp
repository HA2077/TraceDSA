#include <iostream>
#include "../ArrayList/ArrayList.h"
#include "Queue.h"
using namespace std;

/*
MADE BY: HA
This module implements the Queue (INT NUMBERS ONLY) DS using ArrayList the class got 3 methods:
1. Enqueue: to add the item in the queue.
2. Dequeue: to remove the first item enqueued in the queue.
3. Display: to print the elements of the queue.
(FIFO)
*/

void Queue::Enqueue(int value){
    Queuearr.add(value);
    cout << "Added element " << value << " to the queue" << endl;
}

void Queue::Dequeue(){
    if (Queuearr.getSize() == 0){
        cout << "The queue is empty. Enqueue an element." << endl;
        return;
    }
    int Relement = Queuearr.get(0);
    Queuearr.remove(0);
    cout << "Removed Element " << Relement << " From the queue." << endl;
}

void Queue::Display(){
    if (Queuearr.getSize() == 0){
        cout << "The queue is empty. Enqueue an element." << endl;
        return;
    }
    cout << "The current queue: ";
    for(int i = 0;i < Queuearr.getSize();++i){
        cout << Queuearr.get(i) << " ";
    }
    cout << endl;
}