#  Nathan Zhu, Friday June 28th, 1:31 am
#  Leetcode 209 | medium | I think medium/easy
#
#  The O(n) solution is a simple sliding window problem.  There's apparently a NlogN binary search solution, but it is harder.
#  I haven't figured that out yet.
#  
#
# [1, 2, 2, 10, 5], s == 6
#  L = 0
#  R = 1
# [1, 2, 2, 10, 5], s == 6
#  L = 0
#     R = 2
# [1, 2, 2, 10, 5], s == 6    
#  L = 0
#        R = 3
# [1, 2, 2, 10, 5], s == 6  (target reached)
#  L = 0
#            R = 4          
# [1, 2, 2, 10, 5], s == 6  move left
#     L = 1
#            R = 4
# [1, 2, 2, 10, 5], s == 6  move left
#        L = 2
#            R = 4
# [1, 2, 2, 10, 5], s == 6  move left
#            L = 3
#            R = 4
# [1, 2, 2, 10, 5], s == 6  move left (curr_sum < s)
#               L = 4
#            R = 4
# [1, 2, 2, 10, 5], s == 6
#               L = 4
#               R = 5
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        
        left, right = 0, 0          # right is right index of sliding window, inclusive
                                    # left is left index of sliding window, inclusive
        curr_sum =  0
        min_len = float('inf')
        
        while right < len(nums):
            # We advance right pointer
            curr_sum += nums[right]
            right += 1
            
            # If when we get to desired sum, we see how far right we can move left pointer
            while curr_sum >= s:
                min_len = min(right - left, min_len)
                curr_sum -= nums[left]
                left += 1
                
        return min_len if (min_len != float('inf')) else 0