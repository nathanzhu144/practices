/** May 4th, 2020 Stockton, CA.  No meeting thursday today at SF!
 *  Leetcode 1313 | easy | easy
 *  Category: fizzbuzz
 */

#include <vector>

using namespace std;

vector<int> decompressRLElist(vector<int>& nums) {
    vector<int> ret;
    for(int i = 0; i < nums.size(); i += 2){
        int num(nums[i + 1]), times(nums[i]);
        for(int j = 0; j < times; ++j) ret.push_back(num);
    }
    return ret;
}