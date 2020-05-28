# Nathan Zhu May 16th, 2020 8:00 am Stockton, CA During Biweekly contest
# Leetcode 1449 | hard | medium cuz I figured it out in <8 min during the contest
# Category: DP
#
# First, I'm damn proud of how I did this during the contest.  I finished in 37 min!!
#
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

def largestNumber(self, cost, target):
    """
    :type cost: List[int]
    :type target: int
    :rtype: str
    """
    table = dict()

    def helper(target):
        if target < 0: return float('-inf')
        if target == 0: return 0
        if target in table: return table[target]

        next_curr = float('-inf')
        for i in range(9):
            next_curr = max(next_curr, 10 * helper(target - cost[i]) + (i + 1))
        table[target] = next_curr
        return next_curr

    ret = helper(target)
    return str(ret) if ret >= 0 else "0"
