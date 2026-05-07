#ifndef BST_H
#define BST_H

#include <iostream>

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
    void preorderHelper(Tnode* node) const;
    void postorderHelper(Tnode* node) const;
    void inorderHelper(Tnode* node) const;
    void freeTree(Tnode* node);

public:
    BST();
    ~BST();
    
    // Public methods
    void insert(int value);
    void remove(int value);
    bool find(int value) const;
    
    // Traversal methods
    void preorder() const;
    void postorder() const;
    void inorder() const;
    
    // Utility methods
    bool isEmpty() const;
    void clear();
};

#include "BST.cpp"
#endif 