/*  Nathan Zhu Saturday June 7th, 2020
*   Leetode 1470 | easy | easy
*   Category: fizzbuzz
*/

#include <vector>
using namespace std;

vector<int> shuffle(vector<int>& nums, int n) {
    int N(nums.size()), i1(0), i2(n);
    vector<int> ret;
    while(i2 < N && i1 < n){
        ret.push_back(nums[i1++]);
        ret.push_back(nums[i2++]);
    }
    return ret;
}