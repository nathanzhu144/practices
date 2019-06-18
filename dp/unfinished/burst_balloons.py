def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr = [1] + [i for i in nums if i != 0] + [1]
    
    def helper(arr, left_i, right_i, mem):
        if right_i - left_i == 1: return 0  # base case, we are out of balloons to pop
        
        key = (left_i, right_i)
        if key in mem: return mem[key]
        else: mem[key] = float('-inf')
        
        for last_ball_to_pop_ind in range(left_i + 1, right_i):
            mem[key] = max(helper(arr, left_i, last_ball_to_pop_ind, mem) +                      \
                        arr[left_i] * arr[last_ball_to_pop_ind] * arr[right_i] +              \
                        helper(arr, last_ball_to_pop_ind, right_i, mem),                      \
                        mem[key])
        
        return mem[key]
    
    return helper(arr, 0, len(arr) - 2, {})


if __name__ == "__main__":
    print(maxCoins([3,1,5,8]))
