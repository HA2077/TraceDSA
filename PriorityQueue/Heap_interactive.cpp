#include <iostream>
#include <string>
#include <sstream>
#include "Heap.h"
using namespace std;

int main() {
    Heap heap;
    cout << "READY" << endl;
    cout.flush();
    
    string line;
    while (getline(cin, line)) {
        istringstream iss(line);
        string cmd;
        iss >> cmd;
        
        if (cmd == "ENQUEUE_MIN") {
            int val;
            if (iss >> val) {
                heap.enqueue(val);
                cout << "OK " << heap.toStringMinHeap() << endl;
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "DEQUEUE_MIN") {
            try {
                heap.dequeueMin();
                cout << "OK " << heap.toStringMinHeap() << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "PEEK_MIN") {
            try {
                int val = heap.peekMin();
                cout << "OK Peek (min): " << val << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "ENQUEUE_MAX") {
            int val;
            if (iss >> val) {
                heap.enqueueMax(val);
                cout << "OK " << heap.toStringMaxHeap() << endl;
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "DEQUEUE_MAX") {
            try {
                heap.dequeueMax();
                cout << "OK " << heap.toStringMaxHeap() << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "PEEK_MAX") {
            try {
                int val = heap.peekMax();
                cout << "OK Peek (max): " << val << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "PRINT_MIN") {
            cout << "OK " << heap.toStringMinHeap() << endl;
            cout.flush();
        }
        else if (cmd == "PRINT_MAX") {
            cout << "OK " << heap.toStringMaxHeap() << endl;
            cout.flush();
        }
        else if (cmd == "ISEMPTY") {
            cout << "OK " << (heap.isEmpty() ? "true" : "false") << endl;
            cout.flush();
        }
        else if (cmd == "SIZE") {
            cout << "OK Size: " << heap.getSize() << endl;
            cout.flush();
        }
        else if (cmd == "CLEAR") {
            heap.clear();
            cout << "OK " << heap.toStringMinHeap() << endl;
            cout.flush();
        }
        else if (cmd == "PRINT") {
            // Default print min heap
            cout << "OK " << heap.toStringMinHeap() << endl;
            cout.flush();
        }
        else if (cmd == "EXIT") {
            cout << "BYE" << endl;
            cout.flush();
            break;
        }
        else {
            cout << "ERROR Unknown command: " << cmd << endl;
            cout.flush();
        }
    }
    return 0;
}