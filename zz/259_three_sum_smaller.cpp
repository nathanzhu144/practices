#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int threeSumSmaller(vector<int>& nums, int target) {
    if(nums.size() < 3) return 0;
    sort(nums.begin(), nums.end());
    int ret = 0;
    for(int first = 0; first < nums.size() - 2; ++first){
        int second = first + 1, third = nums.size() - 1;
        
        int curr_targ = target - nums[first];
        while(second < third){
            if(nums[second] + nums[third] < curr_targ){
                ++ret;
                while(second < third && nums[second] == nums[second + 1]) ++second;
                ++second;
            }
            else --third;
            
        }
    }
    return ret;
}

int main(){
    vector<int> v = {-2, 0, 1, 3};
    cout << threeSumSmaller(v, 2);
}