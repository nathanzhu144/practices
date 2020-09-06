
def maxSideLength(mat, threshold):
    """
    :type mat: List[List[int]]
    :type threshold: int
    :rtype: int
    """
    if not mat or not mat[0]: return 0
    R, C = len(mat), len(mat[0])
    
    prefix = [[mat[r][c] for c in range(C)] for r in range(R)] 
    
    for r in range(R):
        for c in range(C):
            if r > 0: prefix[r][c] += prefix[r - 1][c]
            if c > 0: prefix[r][c] += prefix[r][c - 1]
            if r > 0 and c > 0: prefix[r][c] -= prefix[r - 1][c - 1]
    
    # Is there a square of size k less than threshold?
    def test_size_k_sq(k):
        for r in range(R - k + 1):
            for c in range(C - k + 1):
                br = (r + k - 1, c + k - 1)
                tot = prefix[br[0]][br[1]]
                if r > 0: tot -= prefix[r - 1][br[1]]
                if c > 0: tot -= prefix[br[0]][c - 1]
                if r > 0 and c > 0: tot += prefix[r - 1][c - 1]
                if tot <= threshold: return True
                
        return False
    
    
    left, right = 1, min(R, C)
    ret = 0
    while left <= right:
        mid = (right - left) // 2 + left
        if test_size_k_sq(mid):
            ret = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return ret


if __name__ == "__main__":
    print(maxSideLength([[2, 2], [2, 2]], 0))