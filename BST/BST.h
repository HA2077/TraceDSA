#ifndef BST_H
#define BST_H

#include <iostream>
#include <stdexcept>
#include <string>

struct Tnode{
    int data;
    Tnode* left;
    Tnode* right;
};

class BST{
private:
    Tnode* root;
    
    // Private helper methods
    Tnode* insertHelper(Tnode* node, int value);
    Tnode* deleteHelper(Tnode* node, int value);
    Tnode* findHelper(Tnode* node, int value) const;
    Tnode* findMin(Tnode* node) const;
    void preorderHelper(Tnode* node, std::string& result) const;
    void postorderHelper(Tnode* node, std::string& result) const;
    void inorderHelper(Tnode* node, std::string& result) const;
    void freeTree(Tnode* node);

public:
    BST();
    ~BST();
    
    // Public methods
    void insert(int value);
    void remove(int value);
    bool find(int value) const;
    
    // Traversal methods returning strings for TUI
    std::string preorder() const;
    std::string postorder() const;
    std::string inorder() const;
    
    // Utility methods
    bool isEmpty() const;
    void clear();
};

#include "BST.cpp"
#endif // BST_H