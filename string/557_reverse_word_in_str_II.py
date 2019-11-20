# Nathan Zhu September 6th, 2019 10:33 pm At Neil and Conner's party on sofa.
# Leetcode 557 | easy | EZ
# Category: Fizzbuzz
#
# Microsoft Phone interview - leetcode
# Your interview score of 5.38/10 beats 78% of all users.
# Time Spent: 1 hour 11 minutes 25 seconds
# Time Allotted: 1 hour 30 minutes
# 
# 
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    temp = s.split()
    ret = []
    
    for s in temp: ret.append(s[::-1])
        
    return " ".join(ret)