/** May 10th, 2020, Stockton, CA.  First day at work, 7:21 pm.  We did mostly orientations today, but first day at work!!
 *  Leetcode 53 |  easy | easy
 *  Category: divide and oncq
 *  Runtime O(NlogN), 
 *  Honestly, it feels like everything is coming full-circle.  It was more or less two weeks to the day that I start work in New York.  It was three days ago when
 *  we had our trip in california with Hershal and crew.  It was before work on that first day at Amex that I really started doing leetcode.  I think I started from
 *  maybe 30 questions done or something?  I was laughably bad, but at some point since I always did leetcode at lunch, everyone came to think I was pretty good.  
 * 
 *  I haven't comped the latest couple days, but I'm definitely within hitting range of doing 1000 questions total this year.  My counter says 939 not including the work of the last 
 *  3 days, and there was one day where I did at least 10 questions.  If I can do 50 questions in the next two weeks, I can hit 1000 qs done.  That's damn doable, and 
 *  I can get that done.
 */


#include <vector>
#include <climits>
using namespace std;

int helper(vector<int>& nums, int l, int r){
    if(l > r) return INT_MIN;
    if(l == r) return nums[l];
    
    int mid = (r - l) / 2 + l;
    
    int left_max(0), prefix(0);
    for(int i = mid - 1; i >= l; --i){
        prefix += nums[i];
        left_max = max(prefix, left_max);
    }
    
    int right_max(0);
    prefix = 0;
    for(int i = mid + 1; i <= r; ++i){
        prefix += nums[i];
        right_max = max(prefix, right_max);
    }
    
    int mid_sum = left_max + right_max + nums[mid];
    int ret = max(mid_sum, helper(nums, l, mid - 1));
    return max(ret, helper(nums, mid + 1, r));
}

int maxSubArray(vector<int>& nums) {
    return helper(nums, 0, nums.size() - 1);
}