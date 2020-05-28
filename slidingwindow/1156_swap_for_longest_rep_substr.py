# Nathan Zhu Wednesday, May 28th, 2020, 11:05 pm Stockton, CA
# Leetcode 1156 | medium | kinda hard tbh
# Category: Sliding window.
# This is prob the trickiest sliding window I've seen a long time.
# General idea: Have two Counter objects, one for substr inside sliding window, one for outside.
#               Sliding window valid when there are exactly two chars, and one of them has a count of 1, with 
#               the other character having a count of at least one outside the substr
#
#               aefaaaaaed
#                  ^    ^
#               "aaaaae" vaid because we can swap an "a" in.
#
#               OR if there are <2 unique chars, it is definitely valid
#

import collections

def maxRepOpt1(text):
    """
    :type text: str
    :rtype: int
    """
    outside, inside = collections.Counter(text), collections.Counter()
    left, right, ret, N = 0, 0, 0, len(text)
    curr = set()
    
    # O(1) time
    # Only call when curr is a set of size 2
    # Checks if we have two chars in our sliding window, one with a count of one.
    # Returns true if that item has additional chars outside window.
    def check():
        fir, sec = curr.pop(), curr.pop()
        curr.add(fir), curr.add(sec)
        return (inside[fir] == 1 and outside[sec] >= 1) or (inside[sec] == 1 and outside[fir] >= 1)
    
    while right < N:
        inside[text[right]] += 1
        if inside[text[right]] == 1: curr.add(text[right])
        outside[text[right]] -= 1
        right += 1
        
        while not (len(curr) < 2 or (len(curr) == 2 and check())):
            inside[text[left]] -= 1
            outside[text[left]] += 1
            if inside[text[left]] == 0: curr.remove(text[left])
            left += 1
        ret = max(right - left, ret)
        
    return ret