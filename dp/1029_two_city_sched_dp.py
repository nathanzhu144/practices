# Nathan Zhu Feb 4th, 2020 12:30 pm  SI 106, we have exam tomorrow, lol.
# Leetcode 1029 | easy | medium
# Category: DP
# I do dp on [a, b], where a is number of ppl left to send to A, and b in number of ppl left to send to B.
# We have a total of a * b subproblems, or N ^ 2 subproblems.
# 

def twoCitySchedCost(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    table = dict()
    N = len(costs)
    
    def helper(a, b):
        if a <= -1 or b <= -1: return float('inf')
        if a == 0 and b == 0: return 0
        
        key = (a, b)
        if key in table: return table[key]
        
        table[key] = min(helper(a - 1, b) + costs[a + b - 1][0], helper(a, b - 1) + costs[1][a + b - 1])
        return table[key]
    
    return helper(N // 2, N // 2)

if __name__ == "__main__":
    print(twoCitySchedCost([[10, 20], [30, 200]]))
