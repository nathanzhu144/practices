# /* Nathan Zhu June 27th, 2020, Weekly contest crashed this week lol
# *  Leetcode 1492 | medium | easy
# *  Category: math
# */
# This is an O(N) soln, but there's a smart logn soln. 
# Just don't double count N^2.
# 
# Go up to sqrt(N).
# Then go up to sqrt(N), and take the opposite divisor, but not double counting N^2.
# 

def kthFactor(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    for i in range(1, n + 1):
        # found a factor
        if n % i == 0:
            k -= 1
            if k == 0: return i
            
    return -1