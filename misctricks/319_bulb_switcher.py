# Nathan Zhu September 4th, 2019 3:22 pm
# Leetcode 319 | medium | medium
# 
# Facebook- Phone Interview
# CompletedSeptember 4, 2019 3:22 PM
# Time Spent: 41 minutes 47 seconds
# Time Allotted: 1 hour 30 minutes

# Observations:
# This is a cool one.
# 
# The state of a bulb depends on odd or even number of flips on that bulb.
#
# The idea is that the ith switch gets flipped once for every factor if i.
# For example, Bulb 6 gets flipped with 1, 2, 3, 6
#
# Only non-square numbers have a an odd number of factors.
# Take 16: 1, 2, 4, 8, 16  
#
# Therefore, only square numbers can get flipped an odd number of times...
#
# number of squares under N is bounded by floor(sqrt(N))
# 

def bulbSwitch(n):
    """
    :type n: int
    :rtype: int
    """
    return int(n ** 0.5)

def naive_bulb_switch(n):
    ret = [0] * n

    def flip(i): return 0 if i == 1 else 1

    for k in range(1, n + 1):
        for i in range(len(ret)):
            if (i + 1) % k == 0: ret[i] = flip(ret[i])

    return ret