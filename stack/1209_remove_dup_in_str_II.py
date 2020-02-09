# Nathan Zhu Jan 20th, 2019 12:40 pm Potbelly State Street
# Leetcode 1209 | medium | medium
# Category: Stack
# Damn this is smart, idea is stack has more than just the char, but also the count.

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