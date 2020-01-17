# Nathan Zhu 11:44 pm Santa Cruz December 29th, 2019
# Leetcode 1048 | medium | medium
# Category: DP
# 
# We can use a bottom-up dp in a really easy way by observing that a string chain from word A 
# is simply the longest string chain of any word that is 1 character away from being A.
#
# If we first sort all the strings by increasing length, this is pretty easy.

def longestStrChain(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    words.sort(key=len)
    table = dict()   # Maps string -> longest chain
    
    ret = 0  
    for word in words:
        best = 0
        for i in range(len(word)):
            best = max(best, table.get(word[:i] + word[i + 1:], 0) + 1)
            
        table[word] = best
        ret = max(best, ret)
        
    return ret
            