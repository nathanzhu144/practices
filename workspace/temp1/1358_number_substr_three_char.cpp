
/* Nathan Zhu June 13th, 2020  
*  Leetcode 1358 | medium | medium
*  Category: sliding window
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
#include <climits>
using namespace std;



// a a b c 
int numberOfSubstrings(string s) {
    unordered_map<int, int> table;
    
    int left(0), right(0), N(s.size()), uniq(0), ret(0);
    while(right < N){
        table[s[right]]++;
        if(table[s[right]] == 1) uniq++;
        right++;
        while(uniq == 3){
            ret += (N - right + 1);
            table[s[left]]--;
            if(table[s[left]] == 0) uniq--;
            left++;
        }
    }
    
    return ret;
}