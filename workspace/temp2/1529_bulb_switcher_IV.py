# Nathan Zhu Saturday July 26th, 2020, Stockton CA.  GOT POSITION #36/14309 for top 0.25% in Weely Contest 199.
# I honestly never thought I'd get that high in the next year or next few years.  I only thought it would take
# a few years, and for me to start competitive programming in earnest to actually get that good.  I got 300 leetcode 
# points.  :)  
#
# There wasn't anything super special in Q1 - Q3.
# Q1 took 2 min cuz I was 1 minute late in starting                     (+2:26 min, total 2:26)
# Q2 was an O(N) greedy bit flip question, where it is easy to write the algorithm if you have the idea, but
#    hard to prove why it would work.                                   (+7:45 min, total 10:16)
#                                  ]
# Q3 probably had a really smart solution, probably binary lifting with LCA, the question was how many leaf pairs
# were k distance apart.  I did brute force BFS from each leaf, and then dividing by two for total.
#                                                                       (+20:03 min, total: 30:19)
# Q4 was why I did well.  I'm strongest on DP and graph problems, weak on probability, geometry, etc.   
# I knew I could finish all the problems when I saw this problem, but I think I was overconfident.
# Halfway through trying to memoize with 2D DP, I realized I needed another 2 variables in the 
# memoization for it to work out properly.  So, I ended up with a 4D DP problem.
# I was initially skeptical, but couldn't see a better way, so I kept at it. 
#
# Extremely lucky on Q4 not to have any wrong submissions.  Even william lin had like 2 submission failures. 
# I caught the case where we have to increase RLE by 1 if we go from 9->10 and 99->100
# 
# I initially saw the score, before me finishing Q4, and I was position #600 or so, and I was kinda sad that finishing all 4
# gave my such a low position, but it turned out that my Q4 submission didn't update yet, and I went from #600 -> #36.
#
# 10 minutes slower than William Lin.  I'm super happy w that, but I definitely have room for improvements.  
#                                                                       (+20:12 min, total: +50:31)
#
# Good finish this time, but need more work for future.
#
# Leetcode: 1529 | medium | medium
# Category: Greedy
# Runtime:  O(N)
# Intuition has three parts.
# 1. Starting from left to right if a bit is incorrect, we need at least one bit to flip it.
# 2. Flipping each bit that's correct leads to it having to be flipped back, by contradiction we can get
#    a shorter sequence by not flipping correct bits.
# 3. Each flip flips from index i to end of array, so each flip affects all bits in the back.
# 4. Flipping a bit twice makes it same.
# 5. If we keep track of all flips done so far, we can tell based off of original value and number of flips
#    what the current value is and whether we need to flip this bit.


def minFlips(self, target):
    """
    :type target: str
    :rtype: int
    """
    ret, flips, N = 0, 0, len(target)
    
    for i in range(N):
        if int(flips) != int(target[i]):
            flips = (flips + 1) % 2
            ret += 1
            
    return ret
        