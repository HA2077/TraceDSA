CXX = g++
CXXFLAGS = -std=c++23 -Wall

SRCS = Main.cpp \
       Stack/Stack.cpp \
       Stack/StackAsLinkedList.cpp \
       Queue/Queue.cpp \
       Queue/QueueAsLinkedList.cpp \
       Queue/CircularQueue.cpp \
       LinkedList/LinkedList.cpp \
       LinkedList/DoublyLinkedList.cpp \
       BST/BST.cpp \
       PriorityQueue/Heap.cpp

all: build run clean

build:
	$(CXX) $(CXXFLAGS) $(SRCS) -o main

run:
	./main

clean:
	rm -f main