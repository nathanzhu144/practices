# Nathan Zhu Jan 20th, 2019 12:40 pm Potbelly State Street
# Leetcode 1209 | medium | medium
# Category: Stack
# Damn this is smart, idea is stack has more than just the char, but also the count.

# dumb O(N^2) soln
def removeDuplicates(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    canremove = True
    while canremove:
        i = 0
        canremove = False
        #print(s)
        while i < len(s):
            start = i - 1
            ct = 1
            while i < len(s) and i >= 1 and s[i] == s[i - 1] and ct < k:
                ct += 1
                i += 1
            if ct == k:
                s = s[:start] + s[start + k:]
                canremove = True
                break
            i += 1
            
            
    return s

# smart stack sln
def removeDuplicates(s, k):
    stack = []             # stack of [num, num of occurrences of that num]
    for i, ch in enumerate(s):
        if stack and stack[-1][0] == ch:
            stack[-1][1] += 1
            if stack[-1][1] == k: stack.pop()
        else:
            stack.append([ch, 1])
            
    return "".join([c * cnt for c, cnt in stack])
        
    
if __name__ == "__main__":
    print(removeDuplicates("deeedd",3))