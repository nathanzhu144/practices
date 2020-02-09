
# Nathan Zhu January 26th, 2019 9:30 pm Foundry Loft 
# Leetcode 292 | easy | easy/med?
# Category: Minimax / DP / misc tricks
# 
# This was funny because Leetcode only lists the math soln. This one is actually
# in the induction section, and it can be proved easily that if you have anythng % 4 != 0, you can win,
# but if you have N % 4 == 0, you lose.  
#
# Soln 1 is more applicable to most cases, in many minimax solutions.
# 


# Top down, O(N) time, O(N) space
def canWinNim1(self, n):
    """
    :type n: int
    :rtype: bool
    """
    table = dict()
    def helper(n):
        if n <= 3: return True
        if n in table: return table[n]
        
        ret = False
        for i in range(1, 4):
            ret |= not helper(n - i)
        
        table[n] = ret
        return ret
    return helper(n)

# Bottom up, O(N) time, O(1) space
def canWinNim2(self, n):
    if n <= 3: return True
    
    arr = [False for i in range(n + 1)]  # Each idx represents whether it is possible to win at nim game with this num of stones.
    arr[1] = True
    arr[2] = True
    arr[3] = True
    
    for i in range(4, n + 1):
        arr[i] = (not arr[i - 1] or not arr[i - 2] or not arr[i - 3])
        
    return arr[-1]

# Bottom up, O(N) time, O(1) space
# We use a circular buffer like structure to save the last 4 terms, lol.
# A queue might be easier... or more clean
def canWinNim3(self, n):
    if n <= 3: return True
    
    arr = [False for i in range(4)]  # Each idx represents whether it is possible to win at nim game with this num of stones.
    arr[1] = True
    arr[2] = True
    arr[3] = True
    
    i = 4
    while i < n:
        arr[(i) % 4] = (not arr[(i - 1) % 4] or not arr[(i - 2) % 4] or not arr[(i - 3) % 4])
        i += 1
        
    return arr[i % 4]

# Tricky, O(1) solution.
# 
def canWinNim4(self, n):
    return not n % 4 == 0
    