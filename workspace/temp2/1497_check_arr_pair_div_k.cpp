
/* Nathan Zhu  Thursday July 16th, 2020  Hershal cancelled movie night this week!!! D:  Had leetcode prep w Meera, Neha, Shazeen
*  Leetcode 1497 | medium | medium
*  Category: Similar to two-sum, misc tricks?
*/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


bool canArrange(vector<int>& arr, int k) {
    int num_pairs(0), N(arr.size());
    if(N & 1) return false;
    unordered_map<int, int> table;
    
    for(int i = 0; i < N; ++i){
        int num = arr[i];
        int second = k - (((num % k) + k) % k);
        if(table.count(second) && table[second] > 0){
            table[second]--;
            num_pairs++;
        }else{
            int first = ((num % k) + k) % k;
            if(first == 0) table[k]++;
            else table[first]++;
        }
    }
        
    return N / 2 == num_pairs;
}