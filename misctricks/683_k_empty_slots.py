# Nathan Zhu January 27th, 2019 10:03 pm Foundry Lofts, Winter career fair tomorrow.
# Leetcode 683 | hard | goddamn hard
# Runtime O(N)
# Category: Misc tricks
#
# Each bulb should only care about bulb to its left and right.
# At the very end, each bulb is one away from its neighbors.
#
# Insight:
# We start with the very end result:
# [[None, 1], [0, 2], [1, 3], [2, 4], [3, None]]
# All flowers are 1 apart
#
# Now, take flowers out from the back...
# 
# 1. Everytime we take a flower out, we measure 
# how far that flower is from its left and right
# 2. We mark the left and right, "removing" that flower.
# Run the code to see...

def kEmptySlots(bulbs, K):
    """
    :type bulbs: List[int]
    :type K: int
    :rtype: int
    """

    N = len(bulbs)
    garden = [[i - 1, i + 1] for i in range(N)]
    garden[0][0] = None
    garden[-1][1] = None
    
    ret = -1
    
    for i in range(N - 1, -1, -1):
        curr = bulbs[i] - 1
        left, right = garden[curr]
        
        if left != None and curr - left == K + 1: ret = i + 1
        if right != None and right - curr == K + 1: ret = i + 1
        if left != None: garden[left][1] = right
        if right != None: garden[right][0] = left
            
    return ret
    
if __name__ == "__main__":
    print(kEmptySlots([1,3,2], 1))