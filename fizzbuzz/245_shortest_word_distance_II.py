# Nathan Zhu Tuesday September 10th, 2019 11:52 am
# Leetcode 245 | medium | kinda annoying but medium

# The special case here is that word1 can equal word2, but
# we shouldn't return 0 when that is the case.

def shortestWordDistance(words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    i1, i2, ret = -len(words), -len(words), float('inf')
    same = word1 == word2
    
    for i in range(len(words)):
        if words[i] == word1:
            i1 = i
            if i2 != -1: ret = min(ret, abs(i1 - i2))
            # We assign to i2, so next time i1 gets assigned, i1 - i2 will have correct result
            if same: i2 = i1
        elif not same and words[i] == word2:
            i2 = i
            if i1 != -1: ret = min(ret, abs(i1 - i2))
    return ret