def arraysIntersection(arr1, arr2, arr3):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :type arr3: List[int]
    :rtype: List[int]
    """
    # [1, 3, 4]
    # [4, 4, 7]
    # [3, 3, 4]
    
    ret = []
    N1, N2, N3 = len(arr1), len(arr2), len(arr3)
    i1, i2, i3 = 0, 0, 0
    while i1 < N1 and i2 < N2 and i3 < N3:
        min_e = min(arr1[i1], arr2[i2], arr3[i3])
        
        if arr1[i1] == arr2[i2] and arr2[i2] == arr3[i3]: ret.append(arr1[i1])
        if arr1[i1] == min_e: i1 += 1
        if arr2[i2] == min_e: i2 += 1
        if arr3[i3] == min_e: i3 += 1
            
    return ret