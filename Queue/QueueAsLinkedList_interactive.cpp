#include <iostream>
#include <string>
#include <sstream>
#include "QueueAsLinkedList.h"
using namespace std;

int main() {
    QueueAsLinkedList q;
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
                q.Enqueue(val);
                cout << "OK " << q.toString() << endl;
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "DEQUEUE") {
            try {
                q.Dequeue();
                cout << "OK " << q.toString() << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "PEEK") {
            if (q.toString() == "Queue: [empty]") {
                cout << "ERROR Cannot peek from empty queue" << endl;
            } else {
                // Extract first element from toString for display
                string str = q.toString();
                // Format is "Queue: [elem1 -> elem2 -> ...]" or "Queue: [empty]"
                if (str.length() > 10) { // Not empty
                    string elements = str.substr(9, str.length() - 10); // Remove "Queue: [" and "]"
                    size_t arrowPos = elements.find(" -> ");
                    string firstElem = (arrowPos == string::npos) ? elements : elements.substr(0, arrowPos);
                    cout << "OK Peek: " << firstElem << endl;
                } else {
                    cout << "ERROR Cannot peek from empty queue" << endl;
                }
            }
            cout.flush();
        }
        else if (cmd == "CLEAR") {
            q.clear();
            cout << "OK " << q.toString() << endl;
            cout.flush();
        }
        else if (cmd == "PRINT") {
            cout << "OK " << q.toString() << endl;
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