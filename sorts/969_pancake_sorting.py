# Nathan Zhu May 4th, 2020 Got above median by a decent amount on 376 Final!! 
# Leetcode 969 | medium | medium
# Category: Sorting.
#
# Never done a pancake sort, but it is a N^2 sort.
# The idea is flip biggest number in arr to front, then to back, recurse on array excluding back element.
#
def pancakeSort(A):
    def is_sorted(A):
        return all(A[i] <= A[i + 1] for i in range(len(A) - 1))
    
    N = len(A)
    back = N - 1
    ret = []
    while not is_sorted(A):
        max_idx = A[:back + 1].index(max(A[:back + 1]))
        A[:max_idx + 1] = A[:max_idx + 1][::-1]
        ret.append(max_idx + 1)
        A[:back + 1] = A[:back + 1][::-1]
        ret.append(back + 1)
        back -= 1
    return ret