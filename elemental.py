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
            if Configuration.target.startswith(s.lower(), len(self.word_string())):
                successor_list.append(Configuration(self.word + [s]))
        return successor_list

    def word_string(self):
        """
        Converts internal word into a string
        """
        return "".join(self.word)

    def is_goal(self):
        """
        Returns true if the current configuration is the target
        """
        return Configuration.target == self.word_string().lower()

    def __repr__(self):
        """
        String representation of a configuration
        """
        return "{word_string} : ({target})".format(word_string=self.word_string(), target=Configuration.target)

def bfs(word):
    """
    Returns a goal configuration if the word can be represented as a
    collection of element symbols. None otherwise.
    """
    queue = []
    Configuration.target = word
    queue.append(Configuration([]))
    while len(queue) > 0:
        current_config = queue.pop(0)
        if current_config.is_goal():
            return current_config
        queue.extend(current_config.successors())
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find words that can be spelled using the symbols of elements.")
    parser.add_argument("word_list", help="the filename of the list of words to evaluate")
    parser.add_argument("symbol_file", help="the filename of the element symbols")
    parser.add_argument("-p", dest="percent", action="store_true", help="Show percentage analysis")
    args = parser.parse_args()
    
    # Load element symbols 
    symbols = [s.strip() for s in open(args.symbol_file)]
    Configuration.symbols = symbols

    # Solve
    count_successful = 0
    count_total = 0
    for w in open(args.word_list):
        word = w.strip().lower()
        config = bfs(word)
        if config != None:
            print(config.word_string())
            count_successful += 1
        count_total += 1

    if args.percent:
        print("{x}/{y} were successful = {p}".format(x=count_successful, y=count_total, p=(count_successful/count_total)))

