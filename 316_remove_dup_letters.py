# Nathan Zhu January 2nd, 2019 9:35 pm
# Leetcode 316 | hard | yeah hard
# Category: Stack
# Runtime: O(N)
# Kinda similar to leetcode 402, remove k digits to make smallest number.  Also uses a stack, and similar idea.

# Problem:
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears 
# once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
import collections

def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    c = collections.Counter(s)
    stack = list()
    visited = set()
    
    
    for i, charac in enumerate(s):
        c[charac] -= 1
        
        if charac in visited: continue
        visited.add(charac)
        
        # While the stack is not empty
        #       the next char in stack is bigger than curr char
        #       the next char can be deleted here (as in it appears in the future), 
        # we can pop top of stack and unvisit it.
        while len(stack) > 0 and c[stack[-1]] >= 1 and charac < stack[-1]:
            visited.remove(stack[-1])
            stack.pop()
            
        stack.append(charac)
            
            
    return "".join(stack)

if __name__ == "__main__":
    removeDuplicateLetters("bcabc")