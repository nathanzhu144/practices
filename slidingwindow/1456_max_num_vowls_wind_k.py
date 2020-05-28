# Nahan Zhu May 23rd, 2020 saturday, weekly contest
# Leetcode 1456 | mediu | easy
# Category: sliding window


def maxVowels(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    left, right = 0, 0
    N = len(s)
    ret, num_vow = 0, 0
    while right < N:
        if s[right] in "aeiou": num_vow += 1
        right += 1
        if right - left == k + 1:
            if s[left] in "aeiou": num_vow -= 1
            left += 1
        ret = max(num_vow, ret)
        
    return ret