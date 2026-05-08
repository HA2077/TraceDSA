#ifndef ARRAYLIST_H
#define ARRAYLIST_H

#include <stdexcept>
#include <string>
#include <sstream>

template <typename T>
class ArrayList {
private:
    T* data;
    int size;
    int capacity;
    
    void resize(int newCapacity);

public:
    ArrayList();
    ArrayList(int initialCapacity);
    ~ArrayList();
    
    // Core methods
    void add(const T& element);
    void add(int index, const T& element);
    T get(int index) const;
    void set(int index, const T& element);
    T remove(int index);
    int getSize() const;
    int getCapacity() const;
    bool isEmpty() const;
    void clear();
    
    // Utility methods
    std::string toString() const;
};

#include "ArrayList.cpp"
#endif // ARRAYLIST_H