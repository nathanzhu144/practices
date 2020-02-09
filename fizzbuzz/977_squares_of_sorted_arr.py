# Nathan Zhu Tuesday Jan 21st, 2019 3:00 pm Foundry lofts
# Leetcode 977 | easy | easy
# Category: fizzbuzz

def sortedSquares(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    
    #  [-4, -2, 0, 7, 9, 12]
    #    0   1  2  3  4  5
    #          ^posidx
    #        ^negidx
    # Basically, I find the first positive/zero, and last negative
    # and I combine both in a merge-like fashion (as in mergesort)
    N = len(A)
    posidx, negidx = 0, 0
    while posidx < N:
        if A[posidx] >= 0: break
        posidx += 1


    negidx = posidx - 1
    if negidx < 0: return [n ** 2 for n in A]

    ret = []
    while negidx >= 0 and posidx < N:
        if A[negidx] ** 2 < A[posidx] ** 2:
            ret.append(A[negidx] ** 2)
            negidx -= 1
        else:
            ret.append(A[posidx] ** 2)
            posidx += 1

    while negidx >= 0:
        ret.append(A[negidx] ** 2)
        negidx -= 1
    while posidx < N:
        ret.append(A[posidx] ** 2)
        posidx += 1

    return ret

if __name__ == "__main__":
    print(sortedSquares([-4,-1,0,3,10]))