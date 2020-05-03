# Nathan Zhu April 19th, 2020. Stockton, CA Weekly contest 185, position 225 / 9206, a bit above top 2.5%.  First contest to get all 4 qs, also no WAs.
# Leetcode 1420 | hard | kinda hard? 
# Category:  3D Dynamic programming lol.  I wasn't sure how to do this iteratively.
# s

def numOfArrays(self, n, m, k):
    """
    :type n: int
    :type m: int
    :type k: int
    :rtype: int
    """
    table = dict()
    # represents length of array we have to build still
    def helper(n, m, k, max_so_far):
        #print(n, m, k, max_so_far)
        if n == 0:
            if k == 0: return 1
            else: return 0
        if k < 0: 
            return 0
        key = (n, k, max_so_far)
        if key in table: return table[key]
        ret = 0
        for i in range(1, m + 1):
            if i > max_so_far:
                ret = (ret + helper(n - 1, m, k - 1, i)) % (10 ** 9 + 7)
            else:
                ret = (ret + helper(n - 1, m, k, max_so_far)) % (10 ** 9 + 7)
        table[key] = ret
        return ret
    return helper(n, m, k, -1)
