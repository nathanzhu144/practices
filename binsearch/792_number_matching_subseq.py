# Nathan Zhu January 31st, 2020 Buffalo wild wings with Hershal and Nafeez, but not Letao, and also peifu.
#                               Talking about Hershal's relationship suitors and certain problems.
# Leetcode 792 | medium | kinda hard?
# I thought the idea was non-trivial.
# Category: Binary search / string
# SIMILAR PROBLEMS: 392 is subseq, 1055 shortest way form string

import collections

def numMatchingSubseq(self, S, words):
    """
    :type S: str
    :type words: List[str]
    :rtype: int
    """
    table = collections.defaultdict(list)
    for i, ch in enumerate(S):
        table[ch].append(i)
    
    # find smallest greater or eq to target, returns idx of that el
    def search(arr, target):
        ret = len(arr)
        left, right = 0, ret - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if arr[mid] >= target:
                ret = mid 
                right = mid - 1
            else:
                left = mid + 1
        return ret
    
    # Returns true if string s is a subseq of S.
    def is_subseq(s):
        i = 0
        for ch in s:
            if ch not in table: return False
            
            newidx = search(table[ch], i)
            if newidx == len(table[ch]): return False
            i = table[ch][newidx] + 1
        return True
    
    ret = 0
    for word in words:
        if is_subseq(word): ret += 1
    return ret