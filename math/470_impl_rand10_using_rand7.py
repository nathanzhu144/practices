# Nathan Zhu January 3rd, 2019
# Leetcode 470 | medium | medium
# Category: number theory
# 
# The question is given a uniform distribution 1 - 7, how do you generate a uniform 1 - 10?
# Note that adding the two won't work, subtracting won't work, multiplying won't work as there is 
# non-uniformity introduced.  For example, adding rand7() + rand7() can get us 10 with 5 + 5, 4 + 6, 3 + 7, whereas, 14 can only be achieved with 7 + 7
# 
# So, we do this:
# One way to fix this problem is to think of each dice roll as the row/col of a 7x7 matrix.

#   1  2  3  4  5  6  7
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# So position (1,1) maps to outcome 1.
# Position (1,2) maps to outcome 2.
# ...
# Position (1,7) maps to outcome 7.
# Position (2,1) maps to outcome 8.
# How do we get this number using math for a given (x,y) position?
# 7(x-1) + y
# 
# WE EXCLUDE 40 - 48 BECAUSE this would lead to non-uniformity after modding by 10.
def rand10(self):
    """
    :rtype: int
    """
    num = 50
    while num >= 40:
        num = (rand7() - 1) * 7 + (rand7() - 1)
    return num % 10 + 1
    
    # We only exlude 40 - 48
    # 0 1 2 3 4 5 6 7 8 9 | 10 11 ...    | 30 31 32 33 34 35 36 37 38 39 | 40 41 42 43 44 45 46 47 48
    # [interval 1]         [Interval 2]   [Interval 4]                    [Exclude]
    # 
    