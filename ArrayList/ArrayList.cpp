#include "ArrayList.h"

/*
MADE BY: HA
Array List implemention with dynamic resizing, the class got 10 methods:
1. add(element): to add an element to the end of the list.
2. add(index, element): to add an element at a specific index in the list.
3. get(index): to retrieve the element at a specific index.
4. set(index, element): to update the element at a specific index.
5. remove(index): to remove the element at a specific index and return it.
6. getSize(): to return the number of elements in the list.
7. getCapacity(): to return the current capacity of the list.
8. isEmpty(): to check if the list is empty.
9. clear(): to remove all elements from the list.
10. toString(): to return a string representation of the list (for TUI).
*/

template <typename T>
ArrayList<T>::ArrayList() : data(nullptr), size(0), capacity(0){
    resize(1); // Start with capacity of 1
}

// Check the initial capacity constructor for negative values and handle it
template <typename T>
ArrayList<T>::ArrayList(int initialCapacity) : data(nullptr), size(0), capacity(initialCapacity) {
    if (initialCapacity < 0)
        throw std::invalid_argument("Initial capacity cannot be negative");
    if (initialCapacity > 0)
        data = new T[initialCapacity];
    else
        data = nullptr;
}

template <typename T>
ArrayList<T>::~ArrayList(){
    delete[] data;
}

template <typename T>
void ArrayList<T>::resize(int newCapacity){
    if (newCapacity < 0)
        throw std::invalid_argument("New capacity cannot be negative");
    
    if (newCapacity == capacity)
        return; // No change needed
    
    T* newData = new T[newCapacity];
    
    // Copy elements (only up to the minimum of old and new capacity)
    int elementsToCopy = (size < newCapacity) ? size : newCapacity;
    for (int i = 0; i < elementsToCopy; i++)
        newData[i] = data[i];
    
    delete[] data;
    data = newData;
    capacity = newCapacity;
    
    // If we reduced capacity and size is now larger than capacity, adjust size
    if (size > capacity)
        size = capacity;
}

template <typename T>
void ArrayList<T>::add(const T& element) {
    // Resize if needed (when size equals capacity)
    if (size >= capacity){
        int newCapacity = (capacity == 0) ? 1 : capacity * 2;
        resize(newCapacity);
    }
    
    data[size] = element;
    size++;
}

template <typename T>
void ArrayList<T>::add(int index, const T& element){
    if (index < 0 || index > size)
        throw std::out_of_range("Index out of range");
    
    // Resize if needed
    if (size >= capacity){
        int newCapacity = (capacity == 0) ? 1 : capacity * 2;
        resize(newCapacity);
    }
    
    // Shift elements to the right
    for (int i = size; i > index;--i)
        data[i] = data[i-1];
    
    data[index] = element;
    size++;
}

template <typename T>
T ArrayList<T>::get(int index) const {
    if (index < 0 || index >= size)
        throw std::out_of_range("Index out of range");
    return data[index];
}

template <typename T>
void ArrayList<T>::set(int index, const T& element) {
    if (index < 0 || index >= size)
        throw std::out_of_range("Index out of range");
    data[index] = element;
}

template <typename T>
T ArrayList<T>::remove(int index) {
    if (index < 0 || index >= size)
        throw std::out_of_range("Index out of range");
    
    T removedElement = data[index];
    
    // Shift elements to the left
    for (int i = index; i < size - 1;++i)
        data[i] = data[i+1];
    
    size--;
    
    // Optional: shrink capacity if it's too large (e.g., less than 25% full)
    // For simplicity in this implementation, we won't shrink automatically
    // but we could add: if (size > 0 && size <= capacity/4) resize(capacity/2);
    
    return removedElement;
}

template <typename T>
int ArrayList<T>::getSize() const {
    return size;
}

template <typename T>
int ArrayList<T>::getCapacity() const {
    return capacity;
}

template <typename T>
bool ArrayList<T>::isEmpty() const {
    return size == 0;
}

template <typename T>
void ArrayList<T>::clear(){
    size = 0;
    // Optional: reset to initial capacity or keep current capacity
    // For simplicity, we keep the current capacity but reset size to 0
}

template <typename T>
std::string ArrayList<T>::toString() const {
    if (size == 0){
        return "[]";
    }
    
    std::string result = "[";
    for (int i = 0; i < size; i++) {
        std::ostringstream oss;
        oss << data[i];
        result += oss.str();
        if (i < size - 1) {
            result += ", ";
        }
    }
    result += "]";
    return result;
}

// Explicit instantiation for common types if needed
// template class ArrayList<int>;
// template class ArrayList<double>;
// template class ArrayList<std::string>;