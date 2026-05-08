#include "Heap.h"
#include <sstream>
using namespace std;

/*
MADE BY: HA
This module implements the Priority Queue (Heap) DS with both Min-Heap and Max-Heap functionality:
1. Enqueue/EnqueueMax: inserting a value in the heap (Min-Heap or Max-Heap)
2. DequeueMin/DequeueMax: removing the highest priority value from the heap
3. PeekMin/PeekMax: Getting the highest priority value without removing it
4. toStringMinHeap/toStringMaxHeap: returning a string representation of the heap (for TUI)
*/

// Helper method to swap values in the heap array
void Heap::swapValues(int index1, int index2){
    int temp = heap.get(index1);
    heap.set(index1, heap.get(index2));
    heap.set(index2, temp);
}

void Heap::heapifyUp(int index){
    while (index > 0){
        int parentIndex = (index - 1) / 2;
        if (heap.get(index) < heap.get(parentIndex)){
            swapValues(index, parentIndex);
            index = parentIndex;
        } 
        else
            break; 
    }
}

void Heap::heapifyDown(int index){
    int size = heap.getSize();
    while (true) {
        int leftChild = 2 * index + 1;
        int rightChild = 2 * index + 2;
        int smallest = index;

        if (leftChild < size && heap.get(leftChild) < heap.get(smallest))
            smallest = leftChild;
        if (rightChild < size && heap.get(rightChild) < heap.get(smallest))
            smallest = rightChild;
        if (smallest != index) {
            swapValues(index, smallest);
            index = smallest;
        } 
        else
            break;
    }
}

void Heap::maxHeapifyUp(int index) {
    while (index > 0) {
        int parentIndex = (index - 1) / 2;
        if (heap.get(index) > heap.get(parentIndex)) {
            swapValues(index, parentIndex);
            index = parentIndex;
        } 
        else
            break;
    }
}

void Heap::maxHeapifyDown(int index) {
    int size = heap.getSize();
    while (true) {
        int leftChild = 2 * index + 1;
        int rightChild = 2 * index + 2;
        int largest = index;

        if (leftChild < size && heap.get(leftChild) > heap.get(largest))
            largest = leftChild;
        if (rightChild < size && heap.get(rightChild) > heap.get(largest))
            largest = rightChild;
        if (largest != index) {
            swapValues(index, largest);
            index = largest;
        } 
        else
            break;
    }
}

Heap::Heap() {}

void Heap::enqueue(int value){
    heap.add(value);
    heapifyUp(heap.getSize() - 1);
}

int Heap::dequeueMin(){
    if (heap.getSize() == 0) {
        throw std::underflow_error("Cannot dequeue from empty heap");
    }

    int minValue = heap.get(0);
    heap.set(0, heap.get(heap.getSize() - 1));
    heap.remove(heap.getSize() - 1);

    if (heap.getSize() > 0)
        heapifyDown(0);

    return minValue;
}

int Heap::peekMin() const {
    if (heap.getSize() == 0){
        throw std::underflow_error("Cannot peek from empty heap");
    }
    return heap.get(0);
}

void Heap::enqueueMax(int value){
    heap.add(value);
    maxHeapifyUp(heap.getSize() - 1);
}

int Heap::dequeueMax() {
    if (heap.getSize() == 0){
        throw std::underflow_error("Cannot dequeue from empty heap");
    }

    int maxValue = heap.get(0);
    heap.set(0, heap.get(heap.getSize() - 1));
    heap.remove(heap.getSize() - 1);

    if (heap.getSize() > 0)
        maxHeapifyDown(0);

    return maxValue;
}

int Heap::peekMax() const {
    if (heap.getSize() == 0){
        throw std::underflow_error("Cannot peek from empty heap");
    }
    return heap.get(0);
}

// Utility Methods
string Heap::toStringMinHeap() const{
    if (heap.getSize() == 0) {
        return "Min-Heap: [empty]";
    }
    string result = "Min-Heap: [";
    for (int i = 0; i < heap.getSize(); ++i){
        std::ostringstream oss;
        oss << heap.get(i);
        result += oss.str();
        if (i < heap.getSize() - 1)
            result += " ";
    }
    result += "]";
    return result;
}

string Heap::toStringMaxHeap() const {
    if (heap.getSize() == 0) {
        return "Max-Heap: [empty]";
    }
    string result = "Max-Heap: [";
    for (int i = 0; i < heap.getSize(); ++i){
        std::ostringstream oss;
        oss << heap.get(i);
        result += oss.str();
        if (i < heap.getSize() - 1)
            result += " ";
    }
    result += "]";
    return result;
}

bool Heap::isEmpty() const {
    return heap.getSize() == 0;
}

int Heap::getSize() const {
    return heap.getSize();
}

void Heap::clear() {
    heap.clear();
}