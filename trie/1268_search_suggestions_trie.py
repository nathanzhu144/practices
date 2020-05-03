# Nathan Zhu April 22nd, 2020. COVID-19, Stockton, CA, 376 exam in a week.
# Leetcode 1268 | medium | medium
# Category: Structures / Trie
# 
# I use a trie instead of binary search here.


import string
import collections

class Node:
    def __init__(self):
        self.table = collections.defaultdict(Node)
        self.word = ""
        self.valid = False


class Trie():
    def __init__(self):
        self.root = Node()
        
    def insert_word(self, word):
        curr = self.root
        
        for ch in word:
            curr = curr.table[ch]
            
        curr.word = word
        curr.valid = True
        
    def dfs(self, node):
        ret = []
        def helper(node):
            if len(ret) == 3: return
            if node.valid: ret.append(node.word)
                
            for ch in string.ascii_lowercase:
                if ch in node.table: helper(node.table[ch])
        helper(node)
        return ret
                
                
            

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        ret = []
        t = Trie()
        for p in products: 
            t.insert_word(p)
        
        curr = t.root
        for ch in searchWord:
            curr = curr.table[ch]
            ret.append(t.dfs(curr))
            
        return ret
            