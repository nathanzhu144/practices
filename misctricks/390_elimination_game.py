
# Nathan Zhu January 15th, 2020 5:30 pm Wes Weimer is rating about some weird ass coding metrics, nearly got hit by candy earlier when I vowed to stop drinking coffee (for cancer)
# Leetcode 390 | medium | hard
# Category: Misc Tricks
# This problem a math problem, keep track of the head.
# 
# Example:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
# 2 4 6 8 10 12 14 16 18 20 22 24
# 2 6 10 14 18 22
# 6 14 22
# 14

# First, note that the gaps between the numbers starts out at 1,
# 1 -> 2 -> 4 -> 8 ...
# 
# If we lose the first number, we know where the next number is.
#
# 
# Second, we don't need to track all the numbers, as we just care about
# the final result.  At the very end, the last number is the head

def lastRemaining(n):
    """
    :type n: int
    :rtype: int
    """
    head, left = 1, True
    head_move = 1
    
    while n > 1:
        if left or n % 2 == 1:
            head += head_move
            
        left = not left
        n = n // 2
        head_move *= 2
        
    return head