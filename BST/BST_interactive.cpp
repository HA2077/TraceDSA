#include <iostream>
#include <string>
#include <sstream>
#include "BST.h"
using namespace std;

int main() {
    BST bst;
    cout << "READY" << endl;
    cout.flush();
    
    string line;
    while (getline(cin, line)) {
        istringstream iss(line);
        string cmd;
        iss >> cmd;
        
        if (cmd == "INSERT") {
            int val;
            if (iss >> val) {
                bst.insert(val);
                cout << "OK " << bst.inorder() << endl; // Show inorder after insert
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "REMOVE") {
            int val;
            if (iss >> val) {
                try {
                    bst.remove(val);
                    cout << "OK " << bst.inorder() << endl;
                } catch (const exception& e) {
                    cout << "ERROR " << e.what() << endl;
                }
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "FIND") {
            int val;
            if (iss >> val) {
                bool found = bst.find(val);
                cout << "OK " << (found ? "true" : "false") << endl;
            } else {
                cout << "ERROR Invalid value" << endl;
            }
            cout.flush();
        }
        else if (cmd == "PREORDER") {
            cout << "OK " << bst.preorder() << endl;
            cout.flush();
        }
        else if (cmd == "INORDER") {
            cout << "OK " << bst.inorder() << endl;
            cout.flush();
        }
        else if (cmd == "POSTORDER") {
            cout << "OK " << bst.postorder() << endl;
            cout.flush();
        }
        else if (cmd == "ISEMPTY") {
            cout << "OK " << (bst.isEmpty() ? "true" : "false") << endl;
            cout.flush();
        }
        else if (cmd == "CLEAR") {
            bst.clear();
            cout << "OK " << bst.inorder() << endl;
            cout.flush();
        }
        else if (cmd == "PRINT") {
            cout << "OK " << bst.inorder() << endl;
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