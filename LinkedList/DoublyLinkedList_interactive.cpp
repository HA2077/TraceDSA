#include <iostream>
#include <string>
#include <sstream>
#include "DoublyLinkedList.h"
using namespace std;

int main() {
    DoublyLinkedList dll;
    cout << "READY" << endl;
    cout.flush();
    
    string line;
    while (getline(cin, line)) {
        istringstream iss(line);
        string cmd;
        iss >> cmd;
        
        if (cmd == "INSERT_START") {
            int val;
            if (iss >> val) {
                dll.insertAtTheStart(val);
                cout << "OK " << dll.toString() << endl;
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "INSERT_END") {
            int val;
            if (iss >> val) {
                dll.insertAtTheEnd(val);
                cout << "OK " << dll.toString() << endl;
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "DELETE_START") {
            try {
                dll.deleteAtTheStart();
                cout << "OK " << dll.toString() << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "DELETE_END") {
            try {
                dll.deleteAtTheEnd();
                cout << "OK " << dll.toString() << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "DELETE_VAL") {
            int val;
            if (iss >> val) {
                try {
                    dll.deleteWithVal(val);
                    cout << "OK " << dll.toString() << endl;
                } catch (const exception& e) {
                    cout << "ERROR " << e.what() << endl;
                }
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "PRINT") {
            cout << "OK " << dll.toString() << endl;
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