# Nathan Zhu Sunday Sept 5th, 2019 9:30 pm
# Leetcode 402 | medium | ehhh
# Category: Stack O(N), think an be done in DP with O(N^2)
# 
# Your interview score of 5.74/10 beats 82% of all users.
# Time Spent: 38 minutes 37 seconds
# Time Allotted: 1 hour
#
# Given a non-negative integer num represented as a string, remove k
# digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.



def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    stack = list()
    for n in num:
        while stack and stack[-1] > n and k > 0:
            stack.pop()
            k -= 1
            
        stack.append(n)
    #return stack
    return "".join(stack[:-k or None]).lstrip("0") or "0"