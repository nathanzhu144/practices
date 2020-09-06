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
# Leetcode: 1525 | medium | hard
# Category: 4D DP
# Runtime:  O(N^2 * K)?
#
# When does a RLE length change?
#
# Adding a new character that's dfferent  is a +1 to RLE
#  A ->  AB  means RLE goes from A -> AB  
# 
# Adding a old character that's same, but count is increased to 2 is a +1 to RLE
# A  -> AA means RLE goes from A -> A2
#
# Adding a old characte that's same, but count is increased from 2 > x is USUALLY a +0 RLE
# AAAA -> AAAAA means RLE goes from A4 -> A5
#
# Adding an old character that's same, but count is increased from a smaller power to a greater power,
# for example from 9 to 10 or 99 to 100 increases RLE by 1.
# A ... AA ->  A ... AAA means RLE goes from A9 -> A10 or A99 -> A100
# 
# 
# How to design an algorithm based off of this?  
# The idea here is that if we are trying to build the shortest RLE, and we have K removals, for each
# character in the original string, we can either TAKE or REMOVE IT.  We can only remove up to K
# character, so each removal decreases k by 1.
#
# This is a really good setup for DP.
# Initially I was doing DP off of (index, k left), but I realized pretty quickly given the above factors
# that we have to also include last character & last character occurrences.
# 


def getLengthOfOptimalCompression(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    table = dict()

    def helper(i, k, prev, streak):
        if k < 0: return float('inf')
        if i == len(s):
            if k == 0: return 0
            else: return float('inf')

        key = (i, k, prev, streak)
        if key in table: return table[key]

        ret = helper(i + 1, k - 1, prev, streak)   # deleting this char

        # Keeping this char
        if prev == s[i]: streak += 1
        else: streak = 1

        inc = 0
        if streak == 1 or streak == 2: inc += 1
        if streak == 10 or streak == 100: inc += 1
        ret = min(ret, inc + helper(i + 1, k, s[i], streak))
        table[key] = ret
        return ret

    ret = helper(0, k, None, 0)
    return ret