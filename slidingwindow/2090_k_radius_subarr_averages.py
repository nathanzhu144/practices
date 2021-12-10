# Nathan Zhu, 3:53 pm, Stockton, CA.  
# Leetcode 2090 | medium | fun one
# Category: Sliding window
# Runtime O(N)

def getAverages(arr, k):
    if k == 0: return arr
    N, tot = len(arr), 0
    l = 0
    ret = [-1] * N
    
    for r in range(N):
        tot += arr[r]
        if r - l > k * 2:
            # r - l + 1 is 1 greater than k at this point
            tot -= arr[l]
            l += 1

        if r - l == k * 2:
            ret[r - k] = tot // (k * 2 + 1)
        
    return ret