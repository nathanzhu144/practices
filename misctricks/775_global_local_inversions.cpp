/* Nathan Zhu
*  July 9th, 2021.  Friday 7:41 pm.  Fasting today and am hungry.
*  Leetcode 775 | medium | medium
*  
*/

// All local inversions are global inversions.
// Local & global inversions are same iff there are no global inversions
// that are not local inversions.  

#include <vector>
#include <limits>

using namespace std;


bool isIdealPermutation(vector<int>& nums) {
    int maxnum = numeric_limits<int>::min();
    int N = nums.size();
    
    for(int i = 0; i < N; ++i){
        if(i > 1) { 
            maxnum = max(maxnuds[i - 2]);
        }
        
        if(maxnum > nums[i]) return false;
    }
    
    return true;
}