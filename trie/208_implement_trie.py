# Nathan Zhu August 6th, 2019, 9:49 pm
# Leetcode 208 | medium | medium
# Category: DS
# Implementing a Trie isn't as bad as I thought.
# 
# Why use a Trie vs Hash table?
# A Trie allows us to easily access things with same prefix, 
# for things like autocomplete, that is very useful.
#
# A trie allows us to easily provide an alphabetical order of the entries
# by key. We just do a preorder traversal.  Note NOT inorder traversal.
# This is cause suppose we have the words "HI" and "HIGH".  A preorder traversal
# would print "HIGH" before "HI".
#
# Looking up data in a Trie is O(M) where M is length of string.
# Hash table worst case is O(N) time + O(M) for evaluating hash
#
# No collisions in a Trie.
#
# 
# 
# Trie Disadvantage:
# Some keys, like floating point numbers, have long chains an prefixes that aren't 
# very useful.
# 
# Some tries can require more space than a hash table cause we need memory for
# each character in a string.


import collections

class TrieNode:
    # Initialize your data structure here.
    # self.children maps  letter ->  TrieNode obj
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Returns: Nothing
    # Insert a word into our trie
    # Returns nothing
    def insert(self, word):
        current = self.root

        # Upon indexing into current, we have 2 cases:
        # 1. If the TrieNode exists, there has been a word with same prefix so far
        #    no new TrieNode is created
        #    hash table returns the old TrieNode obj
        # 2. If the TrieNode doesn't exist, no word with same prefix so far
        #    new TrieNode is created
        #    hash table returns a new TrieNode obj
        #
        # Either way, current will point to the next TrieNode object down from the current character
        for c in word:
            # This line took me 20 min to understand lmao, in interview
            # pls replace this line with 3 easily readable lines.
            current = current.children[c]
        
        current.is_word = True

    # Returns: boolean
    # checks if a word is in our Trie
    # We go through the chain of TrieNodes and we check to see if a TrieNode exists for every char in word
    # For the last TrieNode we visit, we check to see if the is_word field is True.
    def search(self, word):
        current = self.root

        for c in word:
            if current.children.get(c) is None: return False
            else: current = current.children.get(c)
        
        return current.is_word == True

    # Returns: boolean
    # Same as search, EXCEPT If we reach end of the word, return true always.
    def startsWith(self, prefix):
        current = self.root

        for c in prefix:
            if current.children.get(c) is None: return False
            else: current = current.children.get(c)
        
        return True


if __name__ == "__main__":
    obj = Trie()
    obj.insert("app")
    obj.insert("ag")
    obj.insert("a")