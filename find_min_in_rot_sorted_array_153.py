def findMin(arr):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(arr) - 1
    
    while left != right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[right]:
            left = mid + 1
        elif arr[mid] >= arr[right]:
            right = mid
            
    return left

if __name__ == "__main__":
    print(findMin([3,4,5,1,2]))