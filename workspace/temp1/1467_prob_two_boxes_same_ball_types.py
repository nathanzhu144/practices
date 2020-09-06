# Nathan Zhu, Stockton, CA, June 1st, 2020 8:01 am
# Leetcode 1467 | hard | hard
# Category: Math (probability)
import collections
import math
import random
def getProbability(balls):
    """
    :type balls: List[int]
    :rtype: float
    """
    def helper(n, sum1, sum2):
        if abs(sum1 - sum2) > totsum - sum1 - sum2: return   #prune if difference > half
        if n == N:
            if sum1 != sum2: return  # diff # balls in each bucket

            prod1 = math.factorial(sum1)
            for item in set1.values(): prod1 /= math.factorial(item)

            prod2 = math.factorial(sum2)
            for item in set2.values(): prod2 /= math.factorial(item)

            denom[0] += prod1 * prod2
            if len(set1) == len(set2): ret[0] += prod1 * prod2  # If same number of keys
        else:
            # (0, 3), (1, 2), (2, 1), (3, 0), try all ways of spliting each ball pile
            set1[n] = balls[n]
            for i in range(balls[n] + 1):
                helper(n + 1, sum1 + balls[n] - i, sum2 + i)
                set2[n] += 1
                set1[n] -= 1
                if set1[n] == 0: del set1[n]                
            del set2[n]
    
    totsum = sum(balls)
    set1, set2 = collections.Counter(), collections.Counter()
    N = len(balls)
    ret = [0]
    denom = [0]
    helper(0, 0, 0)

    return ret[0] * 1.0 / denom[0]
print(getProbability([3, 2, 1]))
