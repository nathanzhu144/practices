# Nathan Zhu, 12/12/2021, 3:08 pm Studying with ZF & J in Milpitas.  We had szechuan food today! 
# Leetcode 2105 | medium | easy/med
# Category: Fizzbuzz

# Important edge case question:
# do any plants have a bigger number than either of the capacities?
def minimumRefill(plants, capacityA, capacityB):
    """
    :type plants: List[int]
    :type capacityA: int
    :type capacityB: int
    :rtype: int
    """
    ret = 0
    N = len(plants)
    lefti, righti, leftamt, rightamt = 0, N - 1, capacityA, capacityB
    
    while lefti <= righti:
        if lefti == righti:
            ret += 1 if max(leftamt, rightamt) < plants[lefti] else 0
            break
            
        else:
            if leftamt < plants[lefti]:
                leftamt = capacityA
                ret += 1
            leftamt -= plants[lefti]
            
            if rightamt < plants[righti]:
                rightamt = capacityB
                ret += 1
            rightamt -= plants[righti]
            
            lefti += 1
            righti -= 1
    return ret