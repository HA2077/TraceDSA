#ifndef HEAP_H
#define HEAP_H

#include "../ArrayList/ArrayList.h"
#include <iostream>
#include <string>

class Heap{
private:
    ArrayList<int> heap;
    
    void swapValues(int index1, int index2);
    void heapifyUp(int index); 
    void heapifyDown(int index); // For Min-Heap
    void maxHeapifyUp(int index);  
    void maxHeapifyDown(int index); // For Max-Heap

public:
    Heap();
    void enqueue(int value);          
    int dequeueMin();                  
    int peekMin() const;             

    void enqueueMax(int value);       
    int dequeueMax();                  
    int peekMax() const;               
    
    // Utility methods - now return strings for TUI
    std::string toStringMinHeap() const;       // Display as Min-Heap
    std::string toStringMaxHeap() const;       // Display as Max-Heap
    bool isEmpty() const;
    int getSize() const;
    void clear();
};

#include "Heap.cpp"
#endif // HEAP_H