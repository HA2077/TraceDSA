#include <iostream>
#include <string>
#include <sstream>
#include "CircularQueue.h"
using namespace std;

int main() {
    CircularQueue cq;
    cout << "READY" << endl;
    cout.flush();
    
    string line;
    while (getline(cin, line)) {
        istringstream iss(line);
        string cmd;
        iss >> cmd;
        
        if (cmd == "ENQUEUE") {
            int val;
            if (iss >> val) {
                // Check if full before enqueueing
                // Since we can't access private members directly, we'll try and see
                cq.Enqueue(val);
                cout << "OK " << cq.toString() << endl;
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "DEQUEUE") {
            try {
                cq.Dequeue();
                cout << "OK " << cq.toString() << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "PEEK") {
            if (cq.toString() == "Queue: [empty]") {
                cout << "ERROR Cannot peek from empty queue" << endl;
            } else {
                // Extract first element from toString for display
                string str = cq.toString();
                // Format is "Queue: [elem1 elem2 ...]" or "Queue: [empty]"
                if (str.length() > 10) { // Not empty
                    string elements = str.substr(8, str.length() - 9); // Remove "Queue: [" and "]"
                    size_t spacePos = elements.find(' ');
                    string firstElem = (spacePos == string::npos) ? elements : elements.substr(0, spacePos);
                    cout << "OK Peek: " << firstElem << endl;
                } else {
                    cout << "ERROR Cannot peek from empty queue" << endl;
                }
            }
            cout.flush();
        }
        else if (cmd == "PRINT") {
            cout << "OK " << cq.toString() << endl;
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