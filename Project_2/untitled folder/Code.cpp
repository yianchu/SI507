Code:

main.cpp

#include
#include
#include
#include "binary_tree.h"

Binary_tree read(istream& in)
{
// Note the stream is called in
//
// declare data as string
// declare level as integer
// get level from stream
// get line from stream and assign it to data
// if level == -1
// return Binary_tree();
//
// declare left as a Binary_tree and assign it read(in)
// Note: it is a recursive call
//
// declare right as a Binary_tree and assign it to read(in)
// Note: it is a recursive call
//
// return Binary_tree(data, left, right)
}

void write(ostream& out, const Binary_tree& tree, int level)
{
// if tree.empty()
// output -1 + \n to out
// return
// output level + ' ' + tree.data() + \n to out
// call write (out, tree.left(), level + 1)
// call write (out, tree.right(), level + 1)
}

/*
* helper function that will help with definite or indefinite
* articles in a string
*/
std::string article(const std::string& entry)
{
std::string article = "a";
if (std::string("aeiou").find(entry[0]) != std::string::npos)
{
article = "an";
}
return article;
}

int main(int argc,char **argv)
{
Binary_tree root;
// Strategy
// get the filename from the command line arguments
// open the file stream
// initialize the root Binary_tree variable with data from the
// file stream to initialize the decision tree root by calling
// the read function
//

// declare a Binary_tree question_tree and set it to root
// while not done
// declare a string called response
// declare a Binary_tree called left and set it to
// question_tree.left()
//
// declare a Binary_tree called right and set it to
// question_tree.right()
//
// if left.empty() and right.empty()
// Add code here that will carry on something like the
// following dialog:
//
// Is it a mammal? Y
// Does it have stripes? N
// Is it a pig? N

// get the response from the user and
// if it is correct,
// print "I guessed it!"
// else
// print "I give up. What is it?"
// if user enters A hamster
// then
// print "Please give me a question that is true
// for a hamster and false for a pig."
// get the response from the user
// example user response: Is it small and cuddly?
//
// Insert a node into question_tree so that this
// question is used in future dialogs:
//
// One strategy to consider is to implement a set method
// in the Binary_tree called root
// the set method will set the data and the left and right
// subtrees for the given root
//
// Future dialog:
// print "May I try again? "
// get response
// if response is yes
// done = true
// else
// question_tree = root
// else
// do
// print Is it a question_tree.data() (y/n):
// get response
// while (response != y and response != n)

// if response is y
// question_tree = left;
// else
// question_tree = right;

// When done, write the decision tree to the data file by calling
// the write function so that the new
// question and answer is added to the data file
}

binary_tree.cpp

//SOLUTION
#include
#include "binary_tree.h"

using namespace std;

Binary_tree::Binary_tree()
{
root = nullptr;
}

Binary_tree::Binary_tree(string root_data)
{
root = new Node;
root->data = root_data;
root->left = nullptr;
root->right = nullptr;
}

Binary_tree::Binary_tree(string root_data, Binary_tree left, Binary_tree right)
{
root = new Node;
root->data = root_data;
root->left = left.root;
root->right = right.root;
}

int Binary_tree::height(const Node* n) const
{
if (n == nullptr)
{
return 0;
}
else
{
return 1 + max(height(n->left), height(n->right));
}
}

int Binary_tree::height() const
{
return height(root);
}

bool Binary_tree::empty() const
{
return root == nullptr;
}

string Binary_tree::data() const
{
return root->data;
}

Binary_tree Binary_tree::left() const
{
Binary_tree result;
result.root = root->left;
return result;
}

Binary_tree Binary_tree::right() const
{
Binary_tree result;
result.root = root->right;
return result;
}

binary_tree.h

#ifndef BINARY_TREE_H
#define BINARY_TREE_H

#include

using namespace std;

class Node
{
private:
string data;
Node* left;
Node* right;
friend class Binary_tree;
};

/*
A binary tree in which each node has two children.
*/
class Binary_tree
{
public:
/**
Constructs an empty tree.
*/
Binary_tree();

/**
Constructs a tree with one node and no children.
@param root_data the data for the root
*/
Binary_tree(string root_data);

/**
Constructs a binary tree.
@param root_data the data for the root
@param left the left subtree
@param right the right subtree
*/
Binary_tree(string root_data, Binary_tree left, Binary_tree right);


/**
Returns the height of this tree.
@return the height
*/
int height() const;

/**
Checks whether this tree is empty.
@return true if this tree is empty
*/
bool empty() const;

/**
Gets the data at the root of this tree.
@return the root data
*/
string data() const;

/**
Gets the left subtree of this tree.
@return the left child of the root
*/
Binary_tree left() const;

/**
Gets the right subtree of this tree.
@return the right child of the root
*/
Binary_tree right() const;

private:
/**
Returns the height of the subtree whose root is the given node.
@param n a node or nullptr
@return the height of the subtree, or 0 if n is nullptr
*/
int height(const Node* n) const;

Node* root;
};