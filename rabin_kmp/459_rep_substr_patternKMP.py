# Nathan Zhu April 30th, 2020, Foundry Lofts, COVID-19
# Leetcode 459 | easy | not easy with KMP, also other trick isn't easy
# Category: KMP / misc-tricks

def repeatedSubstringPattern(self, s):
    """
    :type s: str
    :rtype: bool
    """
    return s in (s * 2)[1:-1]


def repeatedSubstringPattern(self, string):
    """
    :type s: str
    :rtype: bool
    """
    N = len(string)
    dp = [0] * N
    i, j = 1, 0

    while i < N:
        if string[i] == string[j]:
            dp[i] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = dp[j - 1]
            else:
                i += 1

    return dp[-1] and N % (N - dp[-1]) == 0