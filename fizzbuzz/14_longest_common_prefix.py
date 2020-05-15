# Nathan Zhu April 4th, 2020, Stockton, CA, COVID-19, just finished 376 final
# Leetcode 14 | Easy | easy
# Category: Fizzbuzz

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    def two_common(a, b):
        N = min(len(a), len(b))
        for i in range(N):
            if a[i] != b[i]: return a[:i]
        return a[:N]
    
    def helper(arr):
        if len(arr) == 1: return arr[0]
        N = len(arr) // 2
        return two_common(helper(arr[:N]), helper(arr[N:]))
    if not strs: return ""
    return helper(strs)