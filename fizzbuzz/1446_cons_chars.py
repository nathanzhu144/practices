# Nathan Zhu May 16th, 2020 Stockton, CA During Biweekly contest
# Leetcode 1446 | easy | damn annoying
# Category: fizzbuzz
# Did this during the contest.  I did damn well, and messed up so damn bad on this contest.  I had two wrong answers on this trash problem lol bc I Was 
# being silly with out-of-bounds checking.  I also had 2 TLEs for the 4th DP problem, the first because I didn't memoize (even after making the table lol), and the second because I
# didn't see why the first one TLEd.  
# 
# Also, I finished the contest in 37 min.  I was so proud of myself.  
#
# I hit position 181 just as I finished, but it went down to 450.  I feel that I'm getting better.  I guess today I just realized how good I was getting.
# For a game like Starcraft, top 200 is rougly the beginning of GM.  Now, obviously my performance isn't consistently in top 400, but my lowest ranking is usually
# ~2000, which is still top 5%.  Anyway, I am getting there.
#

def maxPower(self, arr):
    """
    :type s: str
    :rtype: int
    """
    if not arr: return 0
    ret, i = 1, 1
    N = len(arr)
    
    while i < N:
        if arr[i] == arr[i - 1]:
            curr = 1
            while i < N and arr[i] == arr[i - 1]:
                curr += 1
                i += 1
            ret = max(ret, curr)
        else:
            i += 1
            
    return ret