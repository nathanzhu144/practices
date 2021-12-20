# Nathan Zhu, 10:19 pm, 12/19/2021.  Stockton, CA.  Played Valorant w George, Chau, Hershal today.
# Leetcode 1200 | easy | easy
# Category: super basic algorithm.

def minimumAbsDifference(arr):
    """
    :type arr: List[int]
    :rtype: List[List[int]]
    """
    arr.sort()
    smallest_delta = float('inf')
    ret = []
    
    for a, b in zip(arr, arr[1:]):
        if abs(b - a) < smallest_delta:
            smallest_delta = abs(b - a)
            ret = []
        if abs(b - a) == smallest_delta:
            ret.append([a, b])
            
    return ret