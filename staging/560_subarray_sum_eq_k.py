# class Solution {
# public:
#   int subarraySum(vector<int>& nums, int k) {
#     if (nums.empty()) return 0;
#     unordered_map<int, int> counts{{0,1}};
#     int cur_sum = 0;
#     int ans = 0;
#     for (const int num : nums) {
#       cur_sum += num;      
#       ans += counts[cur_sum - k];
#       ++counts[cur_sum];
#     }
#     return ans;
#   }
# };
 

def subarray_sum_eq_k(nums, k):
    if not nums: return 0
    counts = dict()
    counts[0] = 1

    curr_sum = 0
    ans = 0

    for num in nums:
        curr_sum += num
        ans += counts[curr_sum - k] if curr_sum - k in counts else 0
        counts[curr_sum] = 0 if curr_sum not in counts else counts[curr_sum] + 1
        
    
    return ans

if __name__ == "__main__":
    print(subarray_sum_eq_k([1, 1, 1], 2))