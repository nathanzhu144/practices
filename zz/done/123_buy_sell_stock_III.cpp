
#include <iostream>
#include <vector>

using namespace std;


// 3, 3, 5, 0, 0
// Idea is that we have an array for MAX profit from 0 -> i
//                         array for MAX profit from i -> n
int maxProfit(vector<int> prices) {
    if(prices.empty()) return 0;

    int n = prices.size();
    vector<int> left(n, 0);   // left indicates max profit from ending on day i or before
    vector<int> right(n, 0);  // right indicates max profit from starting on day i or after

    int min_so_far = prices[0];
    for(int i = 1; i < n; ++i){
        left[i] = max(left[i - 1], prices[i] - min_so_far);
        min_so_far = min(prices[i], min_so_far);
    }

    int max_so_far = prices.back();
    for(int i = n - 2; i >= 0; --i){
        right[i] = max(right[i + 1], max_so_far - prices[i]);
        max_so_far = max(prices[i], max_so_far);
    }

    int ret = 0;
    for(int i = 0; i < n; ++i){
        ret = max(ret, left[i] + right[i]);
    }

    return ret;
}

int main(){
    cout << maxProfit({2, 1, 2, 0, 1});
}