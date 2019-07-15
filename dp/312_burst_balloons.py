# Nathan Zhu 8:36 pm, Monday July 8th, 2019, Amex Building, 36th floor, New York
# Leetcode 312 | hard | yeah damn hard, been looking at this problem for 8 months
#
# This is EXACTLY same question as minimizing matrix multiplication size, except we are trying to
# MAXIMIZE the number of operations done, instead of MINIMIZE.
#
# My solution is similar to this.
# https://leetcode.com/problems/burst-balloons/discuss/76245/Easiest-Java-Solution
def max_coins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # We pad the array with a 1 in front and a 1 in the back.  This makes bounds checking easier.
    # We also pop all balloons with 0 value, as popping the balloon, will give us 0 coins.
    arr = [1] + [i for i in nums if i != 0] + [1]

    # For the helper function, we are calculating the balloon popping for left, right inclusive
    def helper(arr, left_i, right_i, mem):
        # base case, if left_i > right_i, that means that we have an empty interval, we can make a 0 coin profit with no balloons
        if left_i > right_i: return 0  
        
        key = (left_i, right_i)
        if key in mem: return mem[key]
        else:
            # we pick the last_ball_to_pop_index, and divide and conquer for everything else
            # Popping balloons index i -> index j can be solved by picking the balloon to be popped last.  This allows us to break it 
            # into two subproblems that are smaller
            temp = float('-inf')
            for last_ball_to_pop_ind in range(left_i, right_i + 1):
                temp = max(helper(arr, left_i, last_ball_to_pop_ind - 1, mem) +                                  \
                           arr[left_i - 1] * arr[last_ball_to_pop_ind] * arr[right_i + 1] +                      \
                           helper(arr, last_ball_to_pop_ind + 1, right_i, mem),                                  \
                           temp)
            # memoize
            mem[key] = temp
            return temp
    
    return helper(arr, 1, len(arr) - 2, {})

if __name__ == "__main__":
    print(maxCoins([3]))
            