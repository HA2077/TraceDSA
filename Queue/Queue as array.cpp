#include <iostream>
#include "../ArrayList/ArrayList.h"
using namespace std;

class Queue{
    private:
        ArrayList<int> Queuearr;
    public:
        void Enqueue(int value){
            Queuearr.add(value);
            cout << "Added element " << value << " to the queue" << endl;
        }
        void Dequeue(){
            if (Queuearr.getSize() == 0){
                cout << "The queue is empty. Enqueue an element." << endl;
                return;
            }
            int Relement = Queuearr.get(0);
            Queuearr.remove(0);
            cout << "Removed Element " << Relement << " From the queue." << endl;
        }
        void Display(){
            if (Queuearr.getSize() == 0){
                cout << "The queue is empty. Enqueue an element." << endl;
                return;
            }
            cout << "The current queue: ";
            for(int i = 0;i < Queuearr.getSize();++i){
                cout << Queuearr.get(i) << " ";
            }
            cout << endl;
        }
};