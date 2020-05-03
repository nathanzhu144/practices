# Nathan Zhu April 28th, 2020  Done in weekly contest 181. 
# Leetcode 1422 | easy | easy
# Category: fizzbuzz

def maxScore(self, s):
    """
    :type s: str
    :rtype: int
    """

    N = len(s)
    ones = [0] * N
    zeroes = [0] * N

    z_ct = 0
    for i in range(N):
        if s[i] == "0": z_ct += 1
        zeroes[i] = z_ct

    o_ct = 0
    for i in range(N - 1, -1, -1):
        if s[i] == "1": o_ct += 1
        ones[i] = o_ct

    ret = 0
    for i in range(N - 1):
        ret = max(ret, zeroes[i] + ones[i + 1])
    return ret