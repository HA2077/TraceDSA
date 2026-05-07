#include <iostream>
using namespace std;

struct LNode{
    int data;
    LNode* next;
};

class QueueAsLinkedList{
    private:
        LNode* head;
        int listSize = 0;
    public:
        QueueAsLinkedList(){
            head = nullptr;
        }
        void Enqueue(int value){
            LNode* newNode = new LNode();
            newNode->data = value;
            newNode->next = nullptr;

            if (head == nullptr){
                head = newNode;
                listSize++;
                cout << "Inserted: " << value << " at the end of the Queue." << endl;
                return;
            }
            LNode* ptr = head;
            while (ptr->next != nullptr)
                ptr = ptr->next;
            ptr->next = newNode;
            listSize++;
            cout << "Inserted: " << value << " at the end of the Queue." << endl;
        }
        void Dequeue(){
            if (head == nullptr){
                cout << "The Queue is empty, Insert an element first!" << endl;
                return;
            }
            LNode* ptr = head;
            head = head->next;
            delete ptr;
            listSize--;
            cout << "Deleted the first element from the Queue." << endl;
        }
        void printList(){
            if (head == nullptr){
                cout << "The Queue is empty." << endl;
                return;
            }
            cout << "Your Queue: " << endl;
            LNode* ptr = head;
            cout << "Head -> ";
            for (int i = 0;i < listSize;++i){
                cout << ptr->data << " -> ";
                ptr = ptr->next;
            }
            cout << "NULL" << endl;
            cout << "Queue size: " << listSize << endl;
            cout << endl;
        }
};