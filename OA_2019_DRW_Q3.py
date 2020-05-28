# Nathan Zhu May 18th, 2020
# Leetcode n/a | n/a | medium?
# Category: Math
# Had this on the DRW OA back in 2019.

import collections
import heapq

def stupid_elevens(power):
    curr = 11 ** power
    return str(curr).count("1")

# Idea 1:
# 11 ^ (n + 1) == 11 ^ n * 10 + 11 ^ n
#
# Why?
#    121 
#  *  11
# ---------
#    121
#   121
# --------
#   1331
#
#   
#    11
#  * 11
# -------
#    11
#   11
# --------
#   121
#
# Algorithm:
# Assume we have a function which can add two lists of integers together and give us a new list in O(N) time.
# We can call this function with [1, 1] and [1, 1, 0], then with [1, 2, 1] and [1, 2, 1, 0], etc.
#
# Runs in O(NLogN) time, as length of number scales with Log10 of number.  We also call this once for each N.
# 
#  
def smart_elevens(power):
    if power == 0: return 1
    def add_strs(a, b):
        rev_a = a[::-1]
        rev_b = b[::-1]
        aidx, bidx, carry, ret = 0, 0, 0, []

        while aidx < len(a) or bidx < len(b) or carry != 0:
            val1, val2 = 0, 0
            if aidx < len(a): val1 = int(rev_a[aidx])
            if bidx < len(b): val2 = int(rev_b[bidx])
            tot = carry + val1 + val2
            ret.append(tot % 10)
            carry = tot // 10
            aidx += 1
            bidx += 1
        return ret[::-1]

    curr = [1, 1]
    for i in range(power - 1):
        other = curr + [0]
        curr = add_strs(curr, other)

    return "".join(map(str, curr)).count("1")

    

    


if __name__ == "__main__":
    # this definitely seems to work - doesn't fail on anything up to 11^800
    for i in range(1000):
        print("power", i)
        print("multi is ", 11 ** i)
        smart = smart_elevens(i)
        dumb = stupid_elevens(i)
        assert(smart == dumb)



