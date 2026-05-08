#include <iostream>
#include <string>
#include <sstream>
#include "Stack.h"
using namespace std;

int main(){
    Stack s;
    cout << "READY" << endl;
    cout.flush();
    
    string line;
    while (getline(cin, line)) {
        istringstream iss(line);
        string cmd;
        iss >> cmd;
        
        if (cmd == "PUSH") {
            int val;
            if (iss >> val) {
                s.push(val);
                cout << "OK " << s.toString() << endl;
            } 
            else
                cout << "ERROR Invalid value" << endl;
            cout.flush();
        }
        else if (cmd == "POP") {
            try {
                s.pop();
                cout << "OK " << s.toString() << endl;
            } 
            catch (const exception& e){
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "PEEK") {
            try {
                int val = s.peek();
                cout << "OK Peek: " << val << endl;
            } 
            catch (const exception& e){
                cout << "ERROR " << e.what() << endl;
            }
            cout.flush();
        }
        else if (cmd == "PRINT") {
            cout << "OK " << s.toString() << endl;
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