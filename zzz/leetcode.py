import collections

def wateringPlants(arr, capacity):
    """
    :type plants: List[int]
    :type capacity: int
    :rtype: int
    """
    N, ret, curr = len(arr), len(arr), capacity
    
    for i in range(N):
        while arr[i] > 0:
            if arr[i] > curr:
                arr[i] -= curr
                ret += (i * 1) + 2
                curr = capacity
            else:
                curr -= arr[i]
                arr[i] = 0
    return ret

if __name__ == "__main__":
    print(wateringPlants([1,1,1,4,2,3], 4))
    print('hi')