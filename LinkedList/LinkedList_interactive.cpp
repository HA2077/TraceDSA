#include <iostream>
#include <string>
#include <sstream>
#include "LinkedList.h"
using namespace std;

int main() {
    LinkedList ll;
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
                ll.insertAthestart(val);
                cout << "OK " << ll.toString() << endl;
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "INSERT_END") {
            int val;
            if (iss >> val) {
                ll.insertAtTheEnd(val);
                cout << "OK " << ll.toString() << endl;
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "DELETE_START") {
            try {
                ll.deleteAtTheStart();
                cout << "OK " << ll.toString() << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "DELETE_END") {
            try {
                ll.deleteAtTheEnd();
                cout << "OK " << ll.toString() << endl;
            } catch (const exception& e) {
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "DELETE_VAL") {
            int val;
            if (iss >> val) {
                try {
                    ll.deletewithval(val);
                    cout << "OK " << ll.toString() << endl;
                } catch (const exception& e) {
                    cout << "ERROR " << e.what() << endl;
                }
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "PRINT") {
            cout << "OK " << ll.toString() << endl;
            cout.flush();
        }
        else if (cmd == "CLEAR") {
            ll.clear();
            cout << "OK " << ll.toString() << endl;
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