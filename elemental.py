"""
elemental.py
Finds words that can be spelled using symbols of elements
"""

__author__ = "Nic Manoogian"

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find words that can be spelled using the symbols of elements.")
    parser.add_argument("word_list", help="the filename of the list of words to evaluate")
    parser.add_argument("symbol_file", help="the filename of the element symbols")
    args = parser.parse_args()
    
    # Load element symbols
    symbols = [s.strip().lower() for s in open(args.symbol_file)]

    for w in open(args.word_list):
        word = list(w.strip())
        for c in word:
            print(c)

