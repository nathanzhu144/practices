# Nathan Zhu, Chicago O'Hare Airport, 6:15 pm, Friday June 28th, 2019 aboutta miss the flight, soez gonna dip. 
# Leetcode 887 | hard | yes
# Jesus, I've legitimately spent at least 4 hours on this problem.
# 
# Before I was familiar with binary search, I struggled through naive DP approach.  It was TLE.
# Then, I made my two-way binary search, still TLE
# Then, I thought about it, did a one-way binary search, passed in 10 min.
#
def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
    def helper(eggs, floors, mem):
        
        key  = (eggs, floors)
        if key in mem: return mem[key]
        
        if eggs == 1 or floors == 0 or floors == 1: return floors
        
        # Note that helper(eggs - 1, floor - 1, mem) is a function increasing as "floor" increases
        # Note that helper(eggs, floors - floor, mem) is a function decreasing as "floor" increases
        # We use "med" as our proxy for "floor" in this case.
        #
        # We don't need to do a O(n) search thru all floors. and can instead do a binary search, as 
        # the minimum of the max(helper(eggs - 1, floor - 1, mem), helper(eggs, floors - floor, mem))
        # comes close to the intersection point.
        #
        # Suppose:
        # Let increasing be at index "med" be increasing = helper(eggs - 1, med - 1, mem)
        # Let decreasing be  at index "med" be decreasing = helper(eggs, floors - med, mem)
        # 
        # It is obvious that if increasing == decreasing, that means that this is the point where
        # the worst case for egg drop is minimized, as the worst case is same as the best case.
        # Since we calculate worst case as max of best case and worst case, this is optimal point
        #
        # It is intuitive that if increasing > decreasing, we are at a value of med that is simply too large.
        #    if increasing > decreasing: high = med - 1
        #
        # It is also intuitive that if decreasing > increasing, we are at a value of med that is too small.
        #    if increasing < decreasing: low = med + 1
        #
        # So, how do we know that we won't prune a valid minimum med value?  This is troubling
        # as it definitely possible that there is no integer point where increasing == decreasing.3
        # It is possible that there exists a value med s.t.
        #
        #        increasing at med < decreasing at med + 1
        #
        # Working out an example where there are 3 values to do a binary search in wil lsee that the
        # condition high - low > 1 won't allow pruning of any valid numbers. If there is no singular value
        # where increasing == decreasing, left and right will always be 1 apart.  If there is a singular
        # value where increasing == decreasing, left and right will be the same.
        # 
        
        low, high = 1, floors
        # finding "M"
        while high - low > 1:
            med = (high - low) // 2 + low
            increasing = helper(eggs - 1, med - 1, mem)
            decreasing = helper(eggs, floors - med, mem)
            
            # We found the single position
            if increasing == decreasing:
                low = high = med
            elif increasing > decreasing:
                high = med - 1
            elif increasing < decreasing:
                low = med + 1
        
        # We iterate through at most 3 positions now, to get the right floor.
        curr = float('inf')
        for floor in range(low, high + 1):
            curr = min(curr, 1 + max(helper(eggs - 1, floor - 1, mem), helper(eggs, floors - floor, mem)))
            
        mem[key] = curr
        return curr
        
    return helper(K, N, dict())  