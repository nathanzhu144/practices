
/** Nathan Zhu April 14th, 2020 Stockton, CA, Talked to Stanford guy today, and he told me to do more leetcode.  Good stuff man.
 *  Leetcode 1426 | easy | easy
 *  Category: Fizzbuzz
 * 
 *  No for loops, O(N) time, O(N) space 2 passes
 *  I thnk there's a one-pass way too with some thinking, but this is a nice three-liner.
 *  
*/
#include <vector>
#include <unordered_map>
#include <numeric>
#include <algorithm>

using namespace std;

int countElements(vector<int>& arr) {
    unordered_map<int, int> counts;
    
    for_each(begin(arr), end(arr), [&](int num){ counts[num]++; });
    return accumulate(begin(counts), 
                        end(counts), 
                        0, 
                        [&](int ret, const auto& p) { 
                            auto [num, count] = p;
                            return (counts.count(num + 1)) ? ret + count : ret;
                        });
}



