# Nathan Zhu Jan 30th, 2020 Doing the work at the dude saw a turkey outside on the grass, well Julie saw it.
# Leetcode 541 | easy | not bad
# Category: Fizzbuzz
# 
def reverseStr(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    N = len(s)
    ret = list(s)
    for i in range(0, N, k * 2):
        l, r = i, min(N - 1, i + k - 1)
        while l <= r:
            ret[l], ret[r] = ret[r], ret[l]
            l += 1; r -= 1
    return "".join(ret)