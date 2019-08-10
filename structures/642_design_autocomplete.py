# Nathan Zhu Wednesday August 7th, 2019
# Leetcode 642 | hard | not too bad mechanically if you know trie
# Category: Trie
#
# Question: 
# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character "#".
# For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence
# already typed.

# Here are the specific rules:

# The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
# 1. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have 
#    the same degree of hot, you need to use ASCII-code order (smaller one appears first).
#
# 2. If less than 3 hot sentences exist, then just return as many as you can.
#
# 3. When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
# 


import collections
import heapq

class TrieNode():
    def __init__(self):
        # Data Structures & Vars #
        
        # self.children maps   char ->  TrieNode representing next char
        # self.is_word         is seq ending here a word
        # self.word_count      if is_word, how many times have we seen this sentence?
        # self.data            stores the whole sentence ending here
        
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        self.word_count = 0
        self.data = ""

class AutocompleteSystem(object):

    # Effects: Initializes trie with sentences, times
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.word_so_far = ""
        
        for i in range(len(sentences)):
            self.insertsentence(sentences[i], times[i])         
        
    # If input is "#", we insert the sentence from this and previous inputs into Trie.
    # Then, resets self.word_so_far
    # 
    # If input is anything else, returns up to 3 of the most used strings with
    # the prefix entered so far in a list.
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.insertsentence(self.word_so_far, 1)
            self.word_so_far = ""
            return []
        else:
            self.word_so_far = self.word_so_far + c
            return self.gettopthree(self.word_so_far)
    
    # Helper function #
    # Effects: Inserts a string into trie in, increments by word_count_in
    #          Initializes self.word_count to word_count_in if no word was there before
    # Returns: Nothing
    def insertsentence(self, string, word_count_in):
        curr = self.root
        
        for s in string:
            curr = curr.children[s]
        
        curr.is_word = True
        curr.word_count += word_count_in
        curr.data = string
    
    # Helper function #
    # Effects: None
    # Returns: Returns up to 3 most used strings.
    def gettopthree(self, string):
        curr = self.root
        temp = []
        
        # Iterating to parent of all sentences w prefixes we want
        for s in string: curr = curr.children[s]
            
        # curr should now be pointing to parent of all sentences with prefixes we want.
        stack = [curr]
        while stack:
            top = stack.pop()
            if top.is_word:
                temp.append((-top.word_count, top.data))
            for key, nextnode in top.children.items():
                stack.append(nextnode)
        
        return [string for count, string in sorted(temp)[:3]]

if __name__ == "__main__":
    a = AutocompleteSystem(["i love you","island","iroman","i love leetcode"], [5,3,2,2])
    print(a.input("i"))
    print(a.input(" "))
    print(a.input("a"))
    print(a.input("#"))
    print(a.input("i"))
    print(a.input(" "))
    print(a.input("a"))
    print(a.input("#"))
    print(a.input("i"))
    print(a.input(" "))
    print(a.input("a"))
    print(a.input("#"))