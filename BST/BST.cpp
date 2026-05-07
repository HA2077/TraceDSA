#include "BST.h"
#include <iostream>
using namespace std;

/*
MADE BY: HA
This module implements the Binary Search Tree (INT NUMBERS ONLY) DS with the following functionality:
1. Insert: inserting a node in the tree
2. Delete: removing a node with a value from the tree
3. Find: Searching for a node with a value
4. Pre-order Traversal: Going through the tree from the left side of the root first
5. Post-order Traversal: Going through the tree printing the last nodes of the tree and upwards
6. In-order Traversal: Going through the tree printing the left nodes first then the root and then the right nodes (Sorted order)
*/

Tnode* BST::insertHelper(Tnode* node, int value){
    if (node == nullptr){
        Tnode* newNode = new Tnode();
        newNode->data = value;
        newNode->left = nullptr;
        newNode->right = nullptr;
        return newNode;
    }
    
    if (value < node->data)
        node->left = insertHelper(node->left, value);
    else if (value > node->data)
        node->right = insertHelper(node->right, value);
    
    return node;
}

Tnode* BST::deleteHelper(Tnode* node, int value){
    if (node == nullptr) 
        return nullptr;
    
    if (value < node->data)
        node->left = deleteHelper(node->left, value);
    else if (value > node->data)
        node->right = deleteHelper(node->right, value);
    else{
        if (node->left == nullptr){
            Tnode* temp = node->right;
            delete node;
            return temp;
        } 
        else if (node->right == nullptr){
            Tnode* temp = node->left;
            delete node;
            return temp;
        }
        Tnode* temp = findMin(node->right);
        node->data = temp->data;
        node->right = deleteHelper(node->right, temp->data);
    }
    return node;
}

Tnode* BST::findHelper(Tnode* node, int value) const{
    if (node == nullptr)
        return nullptr;
    
    if (value < node->data)
        return findHelper(node->left, value);
    else if (value > node->data)
        return findHelper(node->right, value);
    else
        return node;
}

Tnode* BST::findMin(Tnode* node) const {
    while (node && node->left != nullptr) {
        node = node->left;
    }
    return node;
}

void BST::preorderHelper(Tnode* node, string& result) const {
    if (node != nullptr) {
        result += to_string(node->data);
        result += " ";
        preorderHelper(node->left, result);
        preorderHelper(node->right, result);
    }
}

void BST::postorderHelper(Tnode* node, string& result) const{
    if (node != nullptr) {
        postorderHelper(node->left, result);
        postorderHelper(node->right, result);
        result += to_string(node->data);
        result += " ";
    }
}

void BST::inorderHelper(Tnode* node, string& result) const {
    if (node != nullptr){
        inorderHelper(node->left, result);
        result += to_string(node->data);
        result += " ";
        inorderHelper(node->right, result);
    }
}

void BST::freeTree(Tnode* node){
    if (node != nullptr) {
        freeTree(node->left);
        freeTree(node->right);
        delete node;
    }
}


BST::BST() : root(nullptr) {}
BST::~BST(){
    freeTree(root);
}

void BST::insert(int value){
    root = insertHelper(root, value);
    cout << "Inserted: " << value << " into the BST." << endl;
}

void BST::remove(int value){
    if (!find(value)) {
        cout << "Value " << value << " not found in the BST. Cannot delete." << endl;
        return;
    }
    root = deleteHelper(root, value);
    cout << "Removed: " << value << " from the BST." << endl;
}

bool BST::find(int value) const {
    Tnode* result = findHelper(root, value);
    if (result != nullptr){
        cout << "Value " << value << " found in the BST." << endl;
        return true;
    } 
    else{
        cout << "Value " << value << " not found in the BST." << endl;
        return false;
    }
}

string BST::preorder() const {
    if (isEmpty()) {
        return "Pre-order: [empty]";
    }
    string result = "Pre-order: [";
    preorderHelper(root, result);
    result += "]";
    return result;
}

string BST::postorder() const {
    if (isEmpty()) {
        return "Post-order: [empty]";
    }
    string result = "Post-order: [";
    postorderHelper(root, result);
    result += "]";
    return result;
}

string BST::inorder() const {
    if (isEmpty()) {
        return "In-order: [empty]";
    }
    string result = "In-order: [";
    inorderHelper(root, result);
    result += "]";
    return result;
}

bool BST::isEmpty() const{
    return root == nullptr;
}

void BST::clear(){
    freeTree(root);
    root = nullptr;
    cout << "BST cleared." << endl;
}