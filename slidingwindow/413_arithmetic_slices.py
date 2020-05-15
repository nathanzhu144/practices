# Nathan Zhu May 7th, 2020. Stockton, CA, saw Amber today on a walk
# Leetcode 413 | medium | not bad
# Category: Math, sliding window
# Can do it with dp, not done w dp here


def numberOfArithmeticSlices(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    def calc_sub(N):
        ret = 0
        t = N
        while t >= 3:
            ret += (N - t + 1)
            t -= 1
        return ret 
    
    
    if len(A) < 3: return 0
    N, i = len(A), 2
    ret = 0
    while i < N:
        if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
            cnt = 2
            diff = A[i] - A[i - 1]
            while i < N and A[i] == A[i - 1] + diff:
                i += 1
                cnt += 1
            
            ret += calc_sub(cnt)
        else:
            i += 1
            
    return ret