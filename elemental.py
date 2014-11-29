"""
elemental.py
Finds words that can be spelled using symbols of elements
"""

__author__ = "Nic Manoogian"

import argparse

class Node:
    """
    A generic linked-list node
    """
    def __init__(self, data)
        """
        Creates an empty node with data
        """
        self.data = data
        self.nextNode = None
    def setNext(self, nextNode)
        """
        Sets the next node
        """
        self.nextNode = nextNode

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find words that can be spelled using the symbols of elements.")
    parser.add_argument("word_list", help="the filename of the list of words to evaluate")
    parser.add_argument("symbol_file", help="the filename of the element symbols")
    args = parser.parse_args()
    
    # Load element symbols into the tree
    symbols = []
    for s in open(args.symbol_file):
        symbol = list(s.strip().lower())
        rootNode = None
        currentNode = None
        for c in symbol:
            if rootNode == None:
                rootNode = Node(c)
                currentNode = rootNode
            else:
                
                


    for w in open(args.word_list):
        word = list(w.strip())
        for c in word:
            print(c)

