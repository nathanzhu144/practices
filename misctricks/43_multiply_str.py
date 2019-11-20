# Nathan Zhu September 5, 2019 8:54 PM
# Category: Misc tricks
# Leetcode 43 | medium | medium
# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.

# Microsoft- Phone Interview (leetcode)
# Your interview score of 6.73/10 beats 82% of all users.
# Time Spent: 30 minutes 41 seconds
# Time Allotted: 1 hour 30 minute

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"

def multiply(number1, number2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    num1, num2 = number1[::-1], number2[::-1]
    ret = [0] * (len(num1) + len(num2))
    
    for i in range(len(num1)):
        for j in range(len(num2)):
            curr = int(num1[i]) * int(num2[j])
            pos1, pos2 = i + j, i + j + 1
            
            prod = ret[pos1] + curr
            
            ret[pos1] = prod % 10
            ret[pos2] += prod // 10
            
    while len(ret) > 1 and ret[-1] == 0: ret.pop()
        
    return  "".join([str(s) for s in ret])[::-1]