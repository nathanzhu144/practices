# Nathan Zhu September 6th, 2019 10:33 pm At Neil and Conner's party on sofa.
# Leetcode 212 | hard | pretty hard
#
# Microsoft Phone interview - leetcode
# Your interview score of 5.38/10 beats 78% of all users.
# Time Spent: 1 hour 11 minutes 25 seconds
# Time Allotted: 1 hour 30 minutes
#
# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same letter 
# cell may not be used more than once in a word.

 

# Example:

# Input: 
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]

# Output: ["eat","oath"]

# Intution
# Save time with a Trie, and backtracking with a trienode.

import collections

class TrieNode(object):
    # self.table maps char -> trienode
    def __init__(self):
        self.endshere = False
        self.word = ""
        self.next = collections.defaultdict(TrieNode)
        self.prev = None

class Trie(object):
    def __init__(self, dictionary):
        self.root = TrieNode()
        
        for word in dictionary:
            self.add_word(word)
        
    def add_word(self, string):
        curr = self.root
        
        for character in string:
            curr = curr.next[character]            
        curr.endshere = True
        curr.word = string
    

class Solution(object):
    # DS 
    # Used positions. 
    # 
    # Functions
    # DFS 
    # 
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def valid(row, col, board):
            return row >= 0 and col >= 0 and row < len(board) and col < len(board[0])
        
        # If valid row, col
        def DFS(row, col, node, currstring, visited, t):
            # Return if...
            # Not on board position
            # Visited this square on this DFS
            # 
            currstring = currstring + board[row][col]
            if board[row][col] in node.next:
                node = node.next[board[row][col]]
            else: return
            
            # We find a word!
            if node.endshere:
                ret.append(node.word)
                node.endshere = False

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newr, newc = dr + row, dc + col
                if valid(newr, newc, board) and (newr, newc) not in visited:
                    visited.add((row, col))
                    DFS(newr, newc, node, currstring, visited, t)
                    visited.remove((row, col))
                
        t = Trie(words)
        ret = list()
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                DFS(row, col, t.root, "", set(), t)
                
        return ret