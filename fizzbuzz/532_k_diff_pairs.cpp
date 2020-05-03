/* Nathan Zhu 4/29/2020.  10:57 pm.  Finished 376 final today.  Boom.
*  Leetcode 532 | easy | easy
*  Category: Fizzbuzz
*/
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

int findPairs(vector<int>& nums, int k) {
    unordered_set<string> visited;
    unordered_set<int> table;
    if(k < 0) return 0;
    
    for(auto num: nums){
        if(table.count(num + k)) visited.insert(to_string(num) + " " + to_string(num + k));
        if(table.count(num - k)) visited.insert(to_string(num - k) + " " + to_string(num));
        table.insert(num);
    }
    
    return visited.size();
}