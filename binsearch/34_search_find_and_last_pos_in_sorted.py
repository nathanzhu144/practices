#  Nathan Zhu, Flying in air from Chicago to New York.  Sunday June 30th, 2019
#  Leetcode 34 | medium | deadly if not good at binary search
#  Knowing how to find lower_bound and upper_bound of a number is vital.

# NOTE: our find_smallest or find_largest returns -1 

def search_range(arr, target):
    # standard lower bound search
    def find_smallest(arr, target):
        left, right = 0, len(arr) - 1
        ret = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid - 1
                ret = mid
            else:
                left = mid + 1
        return ret
    # standard upper bound search
    def find_largest(arr, target):
        left, right = 0, len(arr) - 1
        ret = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
                ret = mid
            else:
                right = mid - 1
        return ret

    start = find_smallest(arr, target)
    end = find_largest(arr, target)
    # Note, if start == -1, end == -1, means target is "outside" range of array
    #       if arr[start] != target, means target is "inside" range of array, but not in array
    #       range is (smallest, biggest), inclusive.
    return [start, end] if start != -1  and arr[start] == target else [-1, -1]