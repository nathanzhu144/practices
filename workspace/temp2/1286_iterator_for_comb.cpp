
/* Nathan Zhu Monday July 27rd, 2020 5:34 am Stockton, CA.  Preparing for final presentations
*  Leetcode 1286 | medium | tricky
*  Category: Design
*
*  Use a bit mask to get all combinations iteratively.
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

class CombinationIterator {
private:
    string str;
    int num;
    int k;
public:
    CombinationIterator(string characters, int combinationLength) {
        str = characters;
        num = (1 << characters.size()) - 1;  
        k = combinationLength;       
    }
    
    string next() {
        hasNext();
        string ret;
        int N(str.size());
        cout << num << " ";
        for(int i = N - 1; i >= 0; --i){
            if((num & (1 << i)) >> i){
                ret += str[N - 1 - i];
            }
        }
        num--;
        return ret;
    }
    
    bool hasNext() {
        while(num >= 0 && __builtin_popcount(num) != k){
            num -= 1;
        }
        if(num < 0) return false;
        return true;
    }
};

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator* obj = new CombinationIterator(characters, combinationLength);
 * string param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */