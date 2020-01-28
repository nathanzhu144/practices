# Nathan Zhu 10:30 am Dudertadt Library, 3rd floor on south side.  Zhongfu and Julie are sitting behind me.
# Man I've been struggling on this question for probably at least 5 hours.
# I got this question on an Amazon phone screen, LOL, and couldn't do it, so did it today.
# There have been 3 separate occasions when I came back to this question.
# Leetcode 1000 | hard | effing hard
# Category: DP

# Runtime, N^3 apparently?
def mergeStones(stones, K):
    N = len(stones)
    if (N - 1) % (K - 1) != 0: return -1
    
    table = dict()
    presum = stones[:]
    for i in range(N):
        if i > 0: presum[i] += presum[i - 1]
    
    # i, j are indices in array that represent inclusive ranges in array
    # piles is number of piles we want to make
    def helper(i, j, piles):
        key = (i, j, piles)
        if key in table: return table[key]
        #print(key)
        if i == j:
            return 0 if piles == 1 else float('inf')
        
        # If we have 1 pile for this range, it is equivalent to:
        # 1. Cost of getting this range to k piles (recursive call)
        # 2. Cost of merging these k piles to 1 pile (sum of everything from stones[i] to stones[j])
        #    No matter how we combine things to get to k piles, the final merge step of k piles still 
        #    must cost the sum of everything in the range.
        elif piles == 1:
            cost = presum[j]
            if i > 0: cost -= presum[i - 1]
            table[key] = cost + helper(i, j, K)
        # We test all ways to combine the piles 
        # Suppose k = 3
        # stones [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # idx     0  1  2  3  4  5  6  7  8
        # Ways to partition:
        # [0] to 1 piles,  [1, 2, 3, 4, 5, 6, 7, 8] to k - 1 piles
        # [0, 1, 2] to 1 pile, [3, 4, 5, 6, 7, 8] to k - 1 piles
        # [0, 1, 2, 3, 4] to 1 pile, [5, 6, 7, 8] to k - 1 piles
        #  ...
        # [0, 1, 2, 3, 4, 5, 6, 7, 8] to 1 pile, [] to k - 1 piles
        # Note: We step by K - 1 every time.
        #       Sometimes we cannot split an array into k - 1 piles, 
        #       return inf in these cases (handled in "if i == j" where we check if m == 1)
        else:
            mini = float('inf')
            for split in range(i, j, K - 1):
                mini = min(mini, helper(i, split, 1) + helper(split + 1, j, piles - 1))
            table[key] = mini
            
        return table[key]
    
    return helper(0, N - 1, 1)

if __name__ == "__main__":
    print(mergeStones([3,2,4,1,2,6], 3))