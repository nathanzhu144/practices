# Nathan Zhu Christmas Day 8:35 pm, 
# Leetcode 472 | hard | ehh kinda hard?
# Category: Trie / Word break DP
# 
# The question asks:

#Given a list of words (without duplicates), please write a program that returns all 
# concatenated words in the given list of words. A concatenated word is defined as a 
#string that is comprised entirely of at least two shorter words in the given array.

# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
#
# Intuition:
# A small word cannot go into a bigger word, so we sort all the words by size from
# smallest to largest.
#
# Then, we can insert them one at a time.  To see if this word is a concatentated word,
# we use a modified backtracking algorithm on a trie.
#
# Alternative approach:
# Do sorting the same from smallest to largest, but use a word break mechanism instead.
#
import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, string):
        n = self.root
        for c in string:
            n = n.children[c]

        n.is_word = True
        n.word = string
    # this is main logic
    # target is concat word
    # idx is which idx of target we are on
    # num_word is number of concat words we have seen so far
    def find_concat(self, target, idx, num_words):
        node = self.root
        for i in range(idx, len(target)):
            c = target[i]

            if c not in node.children: return False

            node = node.children[c]
            if node.is_word:
                if i == len(target) - 1 and node.is_word and num_words >= 1: return True
                if self.find_concat(target, i + 1, num_words + 1): return True

        return False
        

def findAllConcatenatedWordsInADict(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    
    words.sort(key=len)
    t = Trie()
    ret = list()
    
    for word in words:
        t.add_word(word)
        if t.find_concat(word, 0, 0):
            ret.append(word)
            
    return ret

if __name__ == "__main__":
    print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))