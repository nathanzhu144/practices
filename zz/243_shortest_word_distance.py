# Nathan Zhu August 9th, 2019 5:40 pm 3 days before microsoft interview
# Leetcode 243 | easy | not so easy
# This is a non-trivial algorithm if you haven't thought about it before.
# 
# If you're trying to find the shortest distance between two words in an array,
# it can be done in O(N) time.
#
# Everytime you meet word1 or word2, you update its respective index, and try to figure out
# if the current difference in indices is shorter than the smallest one seen so far.



def shortestDistance(self, words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    idx1, idx2 = -1, -1
    ret = float('inf')
    
    for i in range(len(words)):
        if words[i] == word1:
            idx1 = i
            if idx2 != -1: ret = min(ret, abs(idx1 - idx2))
        if words[i] == word2:
            idx2 = i
            if idx1 != -1: ret = min(ret, abs(idx1 - idx2))
                
    return ret
                