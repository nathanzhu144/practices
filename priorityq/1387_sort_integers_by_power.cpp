/** Nathan Zhu May 17th, 2020 Starting at Salesforce tomorrow!
 *  Leetcode 1387 | mediumm | medium
 *  Similar to kth largest element in an array combined with the CTC OA hailstone problem.
 *  There are two optimizations. 
 *   1. You can do dp on hailstone length
 *   2. You can use either quickselect with nth_element to do a partial sort 
 *      OR
 *   3. Do a priority queue soln where pq is of size k.
 * 
 *   Both would result in the same runtimes.  I only did DP in this solution.
 * 
*/

#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int helper(int k, unordered_map<int,int>& table){
    if(table.count(k)) return table[k];
    if(k == 1) return 1;
    if((k & 1) == 0) table[k] = helper(k / 2, table) + 1;
    else table[k] = helper(k * 3 + 1, table) + 1;
    return table[k];
}


int getKth(int lo, int hi, int k) {
    int N = hi - lo + 1;
    vector<int> numbers(N);
    unordered_map<int, int> table;
    
    generate(begin(numbers), 
                end(numbers), 
                [i = int(lo)]() mutable 
                { 
                    return i++; 
                });
    
    // the & in the capture block ensure this doesn't time out beause we want to capture table by ref.
    // otherwise we will recalculate everytime we call helper.
    sort(begin(numbers), 
            end(numbers), 
            [&](auto a, auto b) {
                int p1(helper(a, table)), p2(helper(b, table));
                if(p1 == p2) return a < b;
                else return p1 < p2;
            });
    
    return numbers[k - 1];
}