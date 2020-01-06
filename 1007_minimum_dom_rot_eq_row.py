# Nathan Zhu Dec 26tth, 2019 8:23 pm, Napa Valley, California  
# Leetcode 1007 | medium | medium
# Category: Misc tricks

def minDominoRotations(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    # Insights 
    # Count the occurrence of all numbeSrs in A and B,
    # and also the number of domino with two same numbers.S
    # Try all possibilities from 1 to 6.
    # If we can make number i in a whole row,
    # it should satisfy that countA[i] + countB[i] - same[i] = N, where N is len(A)
    #
    
    # DS 
    # top counts numbers in top of dominoes
    # bottom counts number in bottom of dominoes
    # same counts number of times when a domino has the same top and bottom
    
    top = [0] * 7
    bottom = [0] * 7
    same = [0] * 7
    N = len(A)
    
    for i in range(len(A)):
        top[A[i]] += 1
        bottom[B[i]] += 1
        if A[i] == B[i]: same[A[i]] += 1
    
    for i in range(1, 7):
        # this is a valid swap
        if top[i] + bottom[i] - same[i] == N:
            return min(N - top[i], N - bottom[i])
            
    return -1