"""
elemental.py
Finds words that can be spelled using symbols of elements
"""

__author__ = "Nic Manoogian"

import argparse

class Configuration:
    """
    A word configuration
    """
    symbols = []
    target = ""
    def __init__(self, word):
        """
        Creates a configuration
        """
        self.word = word
    def successors(self):
        """
        Generates a list of successors from the current configuration
        """
        successor_list = []
        for s in symbols:
            if Configuration.target.startswith(s.lower(), len(self.word)):
                successor_list.append(Configuration(self.word + s.lower()))
        return successor_list
    def is_goal(self):
        """
        Returns true if the current configuration is the target
        """
        return Configuration.target == self.word

def bfs(word):
    """
    Returns true if the word can be represented as a
    collection of element symbols
    """
    queue = []
    Configuration.target = word
    queue.append(Configuration(""))
    while len(queue) > 0:
        current_config = queue.pop(0)
        if current_config.is_goal():
            return True
        queue.extend(current_config.successors())
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find words that can be spelled using the symbols of elements.")
    parser.add_argument("word_list", help="the filename of the list of words to evaluate")
    parser.add_argument("symbol_file", help="the filename of the element symbols")
    args = parser.parse_args()
    
    # Load element symbols 
    symbols = [s.strip() for s in open(args.symbol_file)]
    Configuration.symbols = symbols

    # Solve
    for w in open(args.word_list):
        word = w.strip().lower()
        if bfs(word):
            print(word)

