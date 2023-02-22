#
# Name: Yi-An Chu
# Unique name: yianchu
#

from ast import While
import ast
from re import A
from tkinter import Y
from tracemalloc import stop
from Proj2_tree import printTree

#
# The following two trees are useful for testing.
#


class Tree:
    def __init__(self, data=None):
        self.data = data
        self.question = None
        self.yes = None
        self.no = None  # may leaf

    def unit_tree(self, tree):
        # unit_tree = Tree(tree)
        self.question = tree[0]
        self.yes = tree[1]
        self.no = tree[2]
        # return unit_tree

    def new_tuple(self):
        self.data = (self.question, self.yes, self.no)


smallTree = \
    ("Is it bigger than a breadbox?",
        ("an elephant", None, None),
        ("a mouse", None, None))
smallTree = ('Is it bigger than a breadbox?', ('Is it gray?', ('Does it have wheels?', ('Does it only have four wheels?', ('a car', None, None), ('an airplane', None, None)), ('an elephant', None, None)),
             ('Is it yellow?', ('a tiger', None, None), ('a bear', None, None))), ('Is it gray?', ('Does it have two big ears?', ('a mouse', None, None), ('a rabbit', None, None)), ('an ant', None, None)))


def isLeaf(tree):
    if tree.yes == None and tree.no == None:  # not leaf
        return True
    else:
        return False


def yes_no(ans):
    right = ['yes', 'y', 'yup', 'sure']
    if ans in right:
        return True
    else:
        return False


def change_question(unit_tree):
    # newtree =
    true_object = input('Drats! What was it?')
    distinguish = input(
        f'What is a question that distinguishs between {true_object} and {unit_tree.question} ?')
    ans = input(f'And what is the answer for {true_object} ?')
    if yes_no(ans):
        # print(f'("{distinguish}", {true_object, None, None}, {unit_tree.data})')
        return distinguish, (true_object, None, None), unit_tree.data
    else:
        # print(f'("{distinguish}", {unit_tree.data}, {true_object, None, None})')
        return distinguish, unit_tree.data, (true_object, None, None)


def simplePlay(tree):
    """DOCSTRING!"""
    if isLeaf(tree):  # is leaf
        ans = input('What is it?')
        if ans in tree:
            a = 'True'
        else:
            a = 'False'
        return a  # return to below function yes_no
    else:
        # tree = unit_tree(tree)
        ans = input(tree[0])
        if yes_no(ans):
            a = simplePlay(tree[1])
        else:
            a = simplePlay(tree[2])
        return a  # final return


def playLeaf(leaf):
    newtree = leaf
    ans = input(f'Is it {leaf.question} ?  ')
    if yes_no(ans):
        print('I got it')
    else:
        a, b, c = change_question(leaf)
        newtree.question = a
        newtree.yes = b
        newtree.no = c
        newtree.data = (a, b, c)
    return newtree.data


def play(tree):
    """DOCSTRING!"""
    # a = tree
    t = Tree(tree)
    t.unit_tree(tree)
    if isLeaf(t):  # is leaf
        a = playLeaf(t)
        return a
    else:
        ans = input(t.question)
        if yes_no(ans):
            t.yes = play(t.yes)
            t.new_tuple()
        else:
            t.no = play(t.no)
            t.new_tuple()
        return t.data


def saveTree(tree, files):
    t = Tree(tree)
    t.unit_tree(tree)
    if isLeaf(t):  # is leaf
        print('Leaf', file=files)
        print(t.question, file=files)
    else:
        print('Internal node', file=files)
        print(t.question, file=files)
        saveTree(t.yes, files)
        saveTree(t.no, files)


def loadTree(treeFile):
    line = treeFile.readline()
    if line == '':
        return t.new_tuple()
    line = line.strip()
    # print(line)
    if line == 'Internal node':
        line = treeFile.readline()
        line = line.strip()
        t = Tree()
        t.question = line
        t.yes = loadTree(treeFile)
        t.no = loadTree(treeFile)
        t.new_tuple()
        # print(t.data)
        return t.data

    else:
        line = treeFile.readline()
        line = line.strip()
        leaf = (line, None, None)
        # print(leaf)
        return leaf


def main():
    """DOCSTRING!"""
    # Write the "main" function for 20 Questions here.  Although
    # main() is traditionally placed at the top of a file, it is the
    # last function you will write.
    print('Welcome to 20 Questions!')
    load_or_not = input('Would you like to load a tree from a file?')
    if yes_no(load_or_not):
        file_name = input('What is the name of the file?')
        treeFile = open(file_name, 'r')
        tree1 = loadTree(treeFile)
        treeFile.close()
    else:
        tree1 = smallTree

    newTree = play(tree1)
    while True:
        print(newTree)
        play_or_not = input('Would you like to play again?')
        if not yes_no(play_or_not):
            save_or_not = input('Would you like to save this tree for later?')
            if yes_no(save_or_not):
                file_name = input('Please enter a file name: ')
                treeFile = open(file_name, 'w')
                saveTree(newTree, treeFile)
                treeFile.close()
                break
        newTree = play(newTree)

    print('Thank you! The file has been saved.')
    print('Bye!')

    """simple_play"""
    # simple_smalltree = simplePlay(smallTree)
    # print(f'simplePlay(smallTree): {simple_smalltree}')
    # simple_mediumtree = simplePlay(mediumTree)
    # print(f'simplePlay(mediumTree) {simple_mediumtree}')
    """play(Hint1-4)"""
    # newTree = play(smallTree)
    # print(newTree)
    # newTree = play(mediumTree)
    # print(newTree)
    """saveTree(Hint5)"""
    # treeFile = open('tree1.txt', 'w')
    # saveTree(smallTree, treeFile)
    # treeFile.close()
    # newTree = ('Is it bigger than a breadbox?', ('Does it have wheels?',
    #            ('a car', None, None), ('an elephant', None, None)), ('a mouse', None, None))
    # treeFile = open('tree2.txt', 'w')
    # saveTree(newTree, treeFile)
    # treeFile.close()
    """loadTree(Hint6-7)"""
    # treeFile = open('tree1.txt', 'r')
    # tree1 = loadTree(treeFile)
    # treeFile.close()
    # print(tree1)
    # treeFile = open('tree2.txt', 'r')
    # tree2 = loadTree(treeFile)
    # treeFile.close()
    # print(tree2)


#
# The following two-line "magic sequence" must be the last thing in
# your file.  After you write the main() function, this line it will
# cause the program to automatically play 20 Questions when you run
# it.
#
if __name__ == '__main__':
    main()
