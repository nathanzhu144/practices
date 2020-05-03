# Nathan Zhu March 23rd, 2020.  
# Leetcode n/a | n/a | easy
# Category: Fizzbuzz
#
# What are the unique of pairs of numbers in an array adding up to k?
# (3, 7) amd (7, 3) count as one pair, as both add up to 10.
# Similar to two-sum.

import collections

# queesion 2
def Q2(arr, target):
    used = set()
    table = set()
    ret = 0

    for num in arr:
        if target - num in table:
            pair = tuple(sorted([num, target - num]))
            if pair in used: continue
            used.add(pair)
            ret += 1
        table.add(num)

    return ret