# Nathan Zhu  Septeber 5th, 2019 4:06 pm
# Leetcode 151 | medium | easy if you use python library functions
# Given an input string, reverse the string word by word.

# Example 1:
# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:


# Microsoft- On-Site Interview
# CompletedSeptember 5, 2019 4:06 PM
# 80%
# Your interview score of 6.19/10 beats 80% of all users.
# Time Spent: 1 hour 5 seconds
# Time Allotted: 2 hours

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    ret = s.split()[::-1]
    ret2 = " ".join(ret)
    return ret2