/* Nathan Zhu Thursday, June 4th, 2020. Stockton, CA, 8:05 pm, called Kareen today. 
*  Leetcode 1317 | easy | easy
*  Category: Fizzbuzz
*/
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;



vector<int> getNoZeroIntegers(int n) {
    auto func = [](auto&& x){ return none_of(begin(x), end(x), [](char c){ return c == '0'; }); };
    
    for(int i = 1; i < n; ++i){
        if(func(to_string(i)) && func(to_string(n - i))) return {i, n - i};
    }
    return {};
}