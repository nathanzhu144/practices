#  American express tower, New York, 200 Vessey Street 36th floor, got rained on way to work.
#  Nathan Zhu
#  Leetcode 20 | easy | I think easy
#  June 25th, 2019 7:29 am
#
#  It feels kinda full-circle with this question.  I struggled
#  with this question a year ago, as this was a 281 lab.  Now, it is ...
#  easy.  My code is so much cleaner, too.


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    def matching(char):
        if char == "{": return "}"
        if char == "[": return "]"
        if char == "(": return ")"
        
    stack = list()
    for i in s:
        if i == "{" or i == "(" or i == "[":
            stack.append(i)
        else:
            if not stack or matching(stack[-1]) != i:
                return False
            stack.pop()
            
    return False if stack else True