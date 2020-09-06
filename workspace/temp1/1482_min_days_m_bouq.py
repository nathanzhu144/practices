# /* Nathan Zhu June 14th, 2020  
# *  Leetcode 1482 | medium | medium
# *  Category: sliding window + binary search
# */

        


def minDays(self, arr, num_boq, k):
    """
    :type bloomDay: List[int]
    :type m: int
    :type k: int
    :rtype: int
    """
    N = len(arr)
    
    def find_ones(day):
        i = 0
        ret = 0
        while i < N:
            # moving until next blooming flower
            while i < N and arr[i] > day: i += 1  
                
            # j is curr blooming flower
            j = i
            num_flow_left = k
            while j < N and arr[j] <= day and num_flow_left != 0: 
                j += 1
                num_flow_left -= 1

            if num_flow_left == 0: ret += 1
            i = j
        
        return ret
    
    left, right, ret = min(arr), max(arr), -1
    while left <= right:
        mid = (right - left) // 2 + left
        if find_ones(mid) >= num_boq:
            ret = mid
            right = mid - 1
        else: left = mid + 1
    return ret
    