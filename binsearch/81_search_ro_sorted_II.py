# Nathan Zhu Apri l5th, 2020 Abotuta meeting with Meera and Shazeen for leetcode prep
# Leetcode 81 | medium | kinda hard
# Category: Binary search


# The idea behind this is actually pretty simple.
# Consider the case with arr = [5, 6, 7, -1, 2, 4]
# We call first ascending array the LEFT SIDE, and second THE RIGHT SIDE.
# 
# If arr[mid] < arr[left], we know that we are on the right side.
# We don't know where the left side stops, but we do know that the left side stops
# somewhere before or at mid.  Hwever, we know the chunk from arr[left:right + 1] is valid incresing
# array.
#
# If our target is in the range arr[mid + 1] <= target <= arr[right], we can search on that side.
# Otherwise, we search on the left side of mid.
# Note, we can do the +1s and -1s in our mid assignment because we first check mid.
#
# 
# Overall, with this logic there are 3 cases
# 1. arr[mid] < arr[left]
# 2. arr[mid] > arr[left]
# 3. arr[mid] == arr[left]
def search(arr, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    N = len(arr)
    left, right = 0, N - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if(arr[mid] == target): return True
        elif(arr[mid] < arr[left]):
            if(arr[mid + 1] <= target <= arr[right]):
                left = mid + 1
            else:
                right = mid - 1
        elif(arr[mid] > arr[left]):
            if(arr[left] <= target <= arr[mid - 1]):
                right = mid - 1
            else:
                left = mid + 1
        # This handles 2 edge cases:
        # 1. With no duplicates, we can get a case like arr = [1, 3], target 3
        #    In this case, arr[mid] == arr[left] amd we have to handle this by incrementing by 1
        #
        # 2. With duplicates: 
        #    [1, 1, 2, 1, 1, 1, 1, 1]
        #    [1, 1, 1, 1, 1, 1, 1, 2]
        #   Both are valid rotations, and if arr[mid] == arr[left], we can't really divide and conquer
        #   because our target can be on the left or right of it.  We just increment left by 1
        elif arr[mid] == arr[left]: left += 1
                
    return False