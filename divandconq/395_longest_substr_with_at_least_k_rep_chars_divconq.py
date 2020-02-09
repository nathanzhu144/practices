# Nathan Zhu Feb 4th, 2020. Starbucks State Street 5:50 am  Have a phone call with ServiewNow today to see what happened in my interview.
# Leetcode 395 | medium | kinda hard?, simple but amazing to think of if possible.
# Category: Divide and conquer.


# Insight 1: A character with a frequency leess than k can never be part of the
#            final result.  So, we split on this character greedily when we encounter it.
# Insight 2: A string with all frequencies >= k is correct.
#
# This leads to an elegant (albeit slightly inefficient) divide and conq solution.

def longestSubstring(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    def helper(s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(helper(string, k) for string in s.split(c))
        return len(s)  # all chars have >= k freq
    
    return helper(s, k)