#  Nathan Zhu, Thuesday 10:46 am, Amex Tower, After work, been here since 5:30 am, a bit tired
#  Leetcode 53 | easy | so, kinda easy with Kadane's algo, but at least a medium with divide and conq
#  Runtime complexity is NlogN, N is size of arr.  
#
#  Analyzing the recurrence relation is a case of master's theorem, where we do O(n / 2) + N work
#  each time, basically same as merge sort.  Therefore, we get a NlogN runtime.
#
#  There is an optimization to this algo that can increase runtime, but I don't think it is feasible in an interview setting.
#  However, the best way to solve this problem is in O(N) time with Kadane's algorithm with DP.

def max_subarray_divide_conq(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # This calculates maximum subarray, crossing arr[mid] in arr
    # Does it in O(n) time.  The code is long, but the idea is super simple
    def max_crossing_sum(arr, mid):
        total_cross_sum = arr[mid]
        
        max_so_far, cumulative = 0, 0
        # this calculates max left of mid
        for i in range(mid - 1, -1, -1):
            cumulative += arr[i]
            max_so_far = max(cumulative, max_so_far)
            
        total_cross_sum += max_so_far
        max_so_far, cumulative = 0, 0
        
        # this calcualtes max right of mid
        for i in range(mid + 1, len(arr)):
            cumulative += arr[i]
            max_so_far = max(cumulative, max_so_far)
        
        # total_cross_sum = max left of mid + arr[mid] + max right of mid
        return total_cross_sum + max_so_far
    
    def max_subarray(nums):
        if len(nums) == 1: return nums[0]
        # if len(nums) == 0: return 0      // THIS CREATES BUGS, FOR NEG NUM ARRAYS
        mid = len(nums) / 2
        
        # Essentially, idea is max_subarray either includes middle element or it does not.  We want to find maximum of these 3:
        #   Includes middle element
        #          - 1. maximum contiguous subarray including min (O(n) operation) 
        #   Doesn't include middle element
        #          - 2. Calculate max contig subarray for left subarray, not including mid
        #          - 3. Calculate max contigu subarray for right subarray, not including mid
        #
        # So, one edge case is when array size == 2, we can potentially try to recursively call max_subarray with empty lists.
        # If we return 0, for empty lists, we create bugs, as sometimes maximum subarray is negative.
        # JUST THOUGHT OF IDEA - CAN RETURN -INF.
        # The bottom code doesn't implement above idea, but finds max of these 3 possibilties, only calculating max_subarray if a 
        # valid list is passed in.
        returned = max(max_subarray(nums[:mid]), max_crossing_sum(nums, mid)) if nums[:mid] else max_crossing_sum(nums, mid)
        returned = max(returned, max_subarray(nums[mid + 1: ])) if nums[mid + 1: ] else returned
        return returned
                        
    return max_subarray(nums)

if __name__ == "__main__":
    print(max_subarray_divide_conq([-2,1]))