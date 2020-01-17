# Nathan Zhu December 29th, 2019 Done in napa valley car
# Leetcode 1234 | medium | kinda hard
# Category: sliding window
import collections

def balancedString(s):
    """
    :type s: str
    :rtype: int
    """
    # If a string is un-balanced, there must be 1-2 characters that are over-represented. 
    # It is impossible to have more than 2, and also impossible to have fewer than 1.
    #
    # We can just take those characters with a count more than N/4, and subtract the number of
    # characters it would take to get to N/4.
    
    # QQWE
    # R
    # L
    c = collections.Counter(s)
    ret = float('inf')
    N = len(s)
    left = 0
    for right in range(N):
        c[right] -= 1
        
        # All statement checks whether if we properly changed all chars in our substring, we would get a balanced string.
        while left <= right + 1 and all(c[ch] <= N // 4 for ch in "QWER"):
            ret = min(ret, right - left + 1)
            c[left] += 1
            left += 1
    return ret

if __name__ == "__main__":
    print(balancedString("QQWWE"))