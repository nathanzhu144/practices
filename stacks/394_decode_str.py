# Nathan Zhu August 30th, 2019
# Leetcode 394 | medium | yeah medium
# Google- On-Site Interview
# Category: stack
#
# Your interview score of 6.36/10 beats 87% of all users.
# Time Spent: 1 hour 23 minutes 49 seconds
# Time Allotted: 2 hours
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    numstack = []
    stringstack = []
    currnum = 0
    currstr = ""

    
    for i in s:
        if i.isdigit(): currnum = currnum * 10 + int(i)
        elif i == "[":
            numstack.append(currnum)
            stringstack.append(currstr)
            currnum = 0
            currstr = ""
        elif i == "]":
            multiplier = numstack.pop()
            top = stringstack.pop()
            currstr = top + multiplier * currstr
        else:
            currstr = currstr + i
            
    return currstr