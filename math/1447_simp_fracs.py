# Nathan Zhu May 16th, 2020 Stockton, CA During Biweekly contest
# Leetcode 1447 | medium | easy
# Category: math
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


def simplifiedFractions(n):
    """
    :type n: int
    :rtype: List[str]
    """
    def gcd(a, b):
        if a == 0: return b
        if b == 0: return a
        return gcd(b, a % b)
    ret = []
    
    for i in range(1, n + 1):
        for j in range(1, i):
            if gcd(j, i) == 1:
                ret.append(str(j) + "/" + str(i))
                
    return ret
            