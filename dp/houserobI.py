#  Suppose that we are trying to find the maximum sum that can be derived from an array
#  However, no two consecutive items in the array can be taken.
# 
#  Formally, the idea is that we have a line of houses.  
#  https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
#
#  10:24 am, Sunday Nov 4th, Hilton Hotel in Chicago
#  6:52 am   Thursday June 6th, Amex Building New york (added C++ code)
#
#  Each of the houses has a profit, given in "arr".  
# 
#  The key insight is ... 
# 
#  We can either take or not take the last house.  
# 
#  1. If we take the last house
#  we cannot take the last house or second to last house, so the problem breaks down to
#  a smaller problem of all the houses except for the last 2.
#
#  2. If we do not take the last house, the problem breaks down to all the houses minus 1.
#
#  We take maximum of the two possibilities.
#
#  [1, 2, 3, ... P - 2, P - 2, P]
#                
#           to maximum of
#  [1, 2, 3, ... P - 2] + profit from last house 
#                  OR 
#  [1, 2, 3, ... P - 1] + no profit 
#
#  

def max_no_adjacent(arr):
    def helper(arr, i, mem):
        key = i
        if key in mem: return mem[key]
        
        if i < 0: return 0
        else: mem[i] = max(helper(arr, i - 1, mem), helper(arr, i - 2, mem) + arr[i])

        return mem[i]

    return helper(arr, len(arr) - 1, {})

if __name__ == "__main__":
    # should be 110
    print(max_no_adjacent([5, 5, 10, 100, 10, 5]))
    print(max_no_adjacent([1, 20, 3]))
    print(max_no_adjacent([1, 2, 3]))



int helper(vector<int> &nums, int index, unordered_map<int, int>& mem){
        
    if(mem.count(index) != 0){
        return mem[index];
    }
    
    if(index < 0){
        return 0;
    }
    
    mem[index] = std::max(helper(nums, index - 1, mem),
                            helper(nums, index - 2, mem) + nums[index]);
    
    return mem[index];
}

int rob(vector<int>& nums) {
    unordered_map<int, int> mem;
    
    return helper(nums, nums.size() - 1, mem);
}