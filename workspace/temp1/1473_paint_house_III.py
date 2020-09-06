
# /* Nathan Zhu June 7th, 2020  
# *  Leetcode 1473 | hard | hard
# *  Category: 3d DP
# */

def minCost(houses, cost, R, C, target):
    """
    :type houses: List[int]
    :type cost: List[List[int]]
    :type m: int
    :type n: int
    :type target: int
    :rtype: int
    """
    
    table = dict()

    def helper(i, num_hoods, last_h):
        if i == len(houses):
            if num_hoods == target: 
                return 0
            else: return float('inf')
        key = (i, num_hoods, last_h)
        if key in table: return table[key]

        ret = float('inf')
        if houses[i] == 0: 
            for c in range(C):
                ret = min(ret, cost[i][c] + helper(i + 1, num_hoods + int(last_h != c + 1), c + 1))
        else: ret = min(ret, helper(i + 1, num_hoods + int(houses[i] != last_h), houses[i]))

        table[key] = ret
        return ret

    ret = helper(0, 0, -1)
    return -1 if (ret == float('inf')) else ret