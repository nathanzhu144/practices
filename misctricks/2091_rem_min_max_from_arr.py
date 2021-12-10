# Nathan Zhu, 12/8/2021, 4:20 am, Stockton, CA.  Kinda sleepy.
# Leetcode 2091 | medium | easy and fun
# Category: Misc tricks
#

# Note all elements are distinct
# 3 cases overall
# [2, 10,7, 5, 4, 1 ,8, 6]
#  0  1  2  3  4  5  6  7
#     ^
#     firsti(min)
#                 ^secondi(max)
# Doesn't matter if firsti is min or max, we just need to know where
# the indexes are.  Smaller index is firsti.
#
# Then we have 3 possibilities.
# [* * * * * * * * * * * *]
#      ^         ^
# [               ]            remove [0:secondi + 1]
#     [                   ]    remove [firsti: N]
# [     ]        [        ]    remove [0:firsti + 1] and [secondi:N]
def minimumDeletions(nums):
    maxi, mini = -1, -1
    max_num, min_num = float('-inf'), float('inf')
    N = len(nums)
    
    for i, num in enumerate(nums):
        if num > max_num:
            maxi = i
            max_num = num
        if num < min_num:
            mini = i
            min_num = num
    
    first, second = sorted([maxi, mini])
    return min(second + 1, N - first, first + 1 + N - second)