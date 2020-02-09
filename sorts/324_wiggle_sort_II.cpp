/** Nathan Zhu Friday January 31st, 2020 9:27 am.  Duderstadt Library 2nd floor, higher table, damn this problem, studying with Julie & Zhongfu.  Apparently they were up till 4 to do their
 *                                                 Solloway presentation. Going to dinner with Peifu and Hershal and Nafeez tonight.  
 *  Leetcode 324 | medium | HARD
 *  Category: Sorts
 *  This question is probably one of the hardest on this platform that I've done.
 * 
 *  To do this in-place, you need to be able to:
 *     - Realize this can be done better than NLogN time by partitioning around the medium, as we only need some kind of partial sort (okay)
 *     - find a median in O(N) time (quickselect should be a hard, not obvious idea)
 *     - Come up with some virtual indexing scheme mapping indices to (2 * idx) + 1 % (n | 1), a bijection mapping
 *       all the odd indices to 
 * 
 *     Mapping: 
 *     arr [3, 5, 1, 1, 6, 4]
 *     idx  0  1  2  3  4  5
 *     vidx 1  3  5  0  2  4
 *    
 *     We want to map all things that are smaller than median to even indices
 *     We want to map all things bigger than median to odd indices
 * 
 *  
 */


#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int vidx(int i, int n){
    return ((i) * 2 + 1) % (n | 1);
}

void wiggleSort(vector<int>& nums) {
    int n = nums.size();

    // Find a median.
    auto midptr = nums.begin() + n / 2;
    nth_element(nums.begin(), midptr, nums.end());
    int median = *midptr;

    int left = 0, right = n - 1, mid = 0;

    while (mid <= right){
        if(nums[vidx(mid, n)] < median){
            swap(nums[vidx(mid, n)], nums[(vidx(right--, n))]);
        }
        else if(nums[vidx(mid, n)] > median){
            swap(nums[vidx(mid++, n)], nums[(vidx(left++, n))]);
        }
        else{
            mid++;
        }
    }
}

int main(){
    vector<int> nums = {13, 6, 5, 5, 4, 2};
    wiggleSort(nums);

}