# Nathan Zhu
# 

def isValid(self, s):
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