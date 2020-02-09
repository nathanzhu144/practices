# Nathan Zhu Feb 4th, 2020.  6:00 am Was just outside Brugel's bagels  A good day.
# Leetcode 1081 | medium | kinda hard to see an O(N) soln
# Category: Stack


def smallestSubsequence(text):
    """
    :type text: str
    :rtype: str
    """
    table = dict()
    for i, ch in enumerate(text):
        table[ch] = i
    
    stack = []
    for i, ch in enumerate(text):
        if ch in stack: continue # ch used already
            
        # We need to check 3 conditions:
        # 1. stack is not empty.
        # 2. character is more optimal than whatever is on the stack rn.
        # 3. the character we are about to pop hasn't had its last occurrence in text.ArithmeticError
        while stack and ch < stack[-1] and i < table[stack[-1]]: stack.pop()
        stack.append(ch)
        
    return "".join(stack)