/* Nathan Zhu June 13th, 2020  
*  Leetcode 901 | medium | medium
*  Category: monotoni stack
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


class StockSpanner {
private:
    stack<pair<int, int>> st;    // (num, idx)
    int i = 0;
public:
    StockSpanner() {
        st.push(pair(INT_MAX, -1));
    }
    
    int next(int price) {
        while(price >= st.top().first){
            st.pop();
        }
        int ret = i - st.top().second;
        st.push(pair(price, i));
        ++i;
        return ret;
    }
};