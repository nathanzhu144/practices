# Nathan Zhu May 1st, 2020
# Leetcode 211 | medium | medium
# Category: Trie

import collections
class TrieNode:
    def __init__(self):
        self.ends_here = False
        self.word = ""
        self.table = collections.defaultdict(TrieNode)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        curr = self.root
        
        for ch in word:
            curr = curr.table[ch]
            
        curr.word = word
        curr.ends_here = True
        
        
    def search_word(self, word):       
        def helper(curr, i):
            if curr.ends_here : return True
            if i >= len(word): return False
            
            if word[i] == ".":
                for key, val in curr.table.items():
                    if helper(val, i + 1): return True
            else:
                if word[i] in curr.table and helper(curr.table[word[i]], i + 1): return True
            return False
        
        return helper(self.root, 0)
                    

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.trie.add_word(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.search_word(word)

if __name__ == "__main__":
    t = WordDictionary()
    t.addWord("s")
    t.search(".")
