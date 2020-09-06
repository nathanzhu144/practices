/* Nathan Zhu Tuesday, Stockton, CA. 7:02 pm, June 16th, 2020 Called Sophie from Amex today.
*  Leetcode 974 | medium | EZ
*  Category: presum counting, same as number subarrays eq k
*/

#include <vector>
#include <unordered_map>
using namespace std;

int subarraysDivByK(vector<int>& A, int K) {
    unordered_map<int, int> counts;
    int ret(0), curr(0);
    counts[0] = 1;
    
    for(auto n : A){
        curr = (((curr + n) % K) + K) % K;
        ret += counts[curr];
        counts[curr]++;
    }
    return ret;
}