
/* Nathan Zhu  Monday July 20th, 2020 10:46 pm Stockton, CA.  Emailed Katie & Jaewon today.
*  Leetcode 1346 | easy | easy
*  Category: two sum
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

bool checkIfExist(vector<int>& arr) {
    unordered_map<int, int> table;
    int N(arr.size());
    
    for(int i = 0; i < N; ++i){
        int num = arr[i];
        if(num % 2 == 0 && table.count(num / 2) && table[num / 2] != i) return true;
        if(table.count(num * 2) && table[num * 2] != i) return true;
        table[num] = i;
    }
    return false;
}