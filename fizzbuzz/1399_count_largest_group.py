
# Nathan Zhu April 4th, 2020. Foundry Lofts, Final Week, COVID-19
# Leetcode 1399 | easy | easy
# Category: Fizzbuzz
# 
# 
import collections
def countLargestGroup(self, n):
    """
    :type n: int
    :rtype: int
    """
    def get_sum(num):
        ret = 0
        for n1 in str(num):
            ret += int(n1)
        return ret
    
    max_ct = 0
    table = collections.Counter()
    for i in range(1, n + 1):
        table[get_sum(i)] += 1
        max_ct = max(table[get_sum(i)], max_ct)
        
    ret = 0
    for key, val in table.items():
        if val == max_ct: ret += 1
    return ret