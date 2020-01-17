def minCostII(costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    mem = dict()
    
    # The idea behind this one is that we can break the problem space down to 
    # n * k subproblems.
    
    # We structure the problem like this:
    # Given that the ith house has one of the k colors banned, 
    # what is the minimum painting cost for this house and rest of houses?
    #
    # we only have n * k problems to solve in total, giving the runtime O(n * k)
    
    def helper(costs, idx, banned):
        key = (idx, banned)
        
        if key in mem: return mem[key]
        
        # Base case, out of houses so no cost
        if idx == len(costs): return 0
    
        # for this house, we can choose any of the non-banned colors to paint this house with.
        ret = float('inf')
        for color in range(len(costs[0])):
            if color != banned:
                ret = min(ret, costs[idx][color] + helper(costs, idx + 1, color))
                
        mem[key] = ret
        
        return ret
    
    return helper(costs, 0, None)

if __name__ == "__main__":
    minCostII([[1,5,3],[2,9,4]])