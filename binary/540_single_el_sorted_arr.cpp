/* Nathan Zhu Jan 10th, 2020 8:21 pm Foundry Lofts
*  Leetcode 540 | medium | EZ
*  Category: bitshifting
*/

#include <vector>

using namespace std;

int singleNonDuplicate(vector<int>& nums) {
    int ret = 0;
    for(auto num : nums) ret ^= num;
    return ret;
}