# Nathan Zhu 200 Vessey Street, New Yotk, June 26th, 6:00 pm
# Leetcode_230 | medium | idea is easy, implementation may not be as easy, without using recursion.
#
# Unlike 4 sum I, which is nontrivial, 4 sum II has 4 separate arrays, and we need to do all combinations of 
# sums for them.
#
# Idea is to see how many in A and B sum up to a sum like 15.
#
# Then, idea is how many in C and D sum up to a sum like -15
# 
# we can do in N^2 time instead of N^4 assuming we know all arrays have same size.
#
# This code was super intuitive, and easy, AFTER seeing the soln, LOL.  Very cool
# NOTE: PRO USE OF GET IN HASH TABLE, DIDN'T KNOW IT EXISTED
def fourSumCount(self, A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    sums = dict()
    
    for i in A:
        for j in B:
            # increment occurrences of i + j by 1, init 
            # to 1 if i + j doesn't exist in sums yet
            sums[i + j] = sums.get(i + j, 0) + 1
    
    ret = 0
    for i in C:
        for j in D:
            # increment ret if we get a sum of 0
            ret += sums.get(-i -j, 0)
    
    return ret