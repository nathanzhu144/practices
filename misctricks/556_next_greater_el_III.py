# Nathan Zhu 10/16/2021 Chicago Bucktown 1:43 pm, about to play stardew valley
# Leetcode 556 | medium |  a bit rough
# Category: Misc tricks 
# same as next permutation.
# In C++ there is a next perm function; I implemented it manually.
# Need to do some additional bounds checking.
# 

def nextGreaterElement(self, n):
    """
    :type n: int
    :rtype: int
    """
    def rev_to_end(num, l):
        N = len(num)
        left, right = l, N - 1
        
        while left < right:
            num[left], num[right] = num[right], num[left]
            left += 1
            right -= 1
            
    
    arr = list(str(n))
    N = len(arr)
    leftmost_exhaust = -1
    i = N - 1
    
    while i - 1 >= 0:
        if int(arr[i - 1]) < int(arr[i]):
            leftmost_exhaust = i
            break
        i -= 1
    
    # no valid answer
    if leftmost_exhaust == -1:
        return -1
    
    leftswap, rightswap = leftmost_exhaust - 1, 0
    i = N - 1
    while i >= 0:
        if int(arr[i]) > int(arr[leftswap]):
            rightswap = i
            break
        i -= 1
        
    arr[leftswap], arr[rightswap] = arr[rightswap], arr[leftswap]
    rev_to_end(arr, leftmost_exhaust)
    ret = int("".join(arr))
    return ret if ret <= 2 ** 31 - 1 else -1
    