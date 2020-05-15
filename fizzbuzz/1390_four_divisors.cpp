/* Nathan Zhu May 11th, 2020, Stockton, CA
*  Leetcode 1390 | medium | not bad
*  Category: Fizzbuzz
*/

using namespace std;
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <cmath>
#include <functional>
#include <numeric>

unordered_map<int, int> table;
unordered_map<int, int> int_to_factors_sum;

int get_divisors(int num){
    if(num == 1 or num == 0) return 1;               // This algo fails for num == 1 cuz, sqrt 1 is 1, we would return 2
    if(table.count(num)) return table[num];
    
    int ret = 0;                          
    int fac_sum = 0;                        // for num itself.
    for(int i = 1; i <= int(sqrt(num)); ++i){
        if(num % i == 0){
            int leftdiv(i), rightdiv(num / i);
            ret += (leftdiv == rightdiv) ? 1 : 2;
            fac_sum += (leftdiv + rightdiv);
        }
    }
    
    table[num] = ret;
    int_to_factors_sum[num] = fac_sum;
    return ret;
}

int sumFourDivisors(vector<int>& nums) {
    vector<int> all_fours;
    vector<int> tot_fac_sum;
    copy_if(nums.begin(), nums.end(), back_inserter(all_fours), [&](int num){ return get_divisors(num) == 4; } );
    transform(all_fours.begin(), all_fours.end(), back_inserter(tot_fac_sum), [&](int num) { return int_to_factors_sum[num]; });
    return accumulate(tot_fac_sum.begin(), tot_fac_sum.end(), 0);
}