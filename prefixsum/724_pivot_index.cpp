/* Nathan Zhu May 19th, 2020. 1:05 am, starting 2nd day at Salesforce toomorrow.  Or today
*  Leetcode 724 | easy | easy
*  Category: Prefix sum
*/

#include <vector>

using namespace std;


int pivotIndex(vector<int>& nums) {
    int N = nums.size();
    vector<int> pre = nums, post = nums;
    
    for(int i = 1; i < N; ++i) pre[i] += pre[i - 1];
    for(int i = N - 2; i >= 0; i--) post[i] += post[i + 1];
    
    for(int i = 0; i < N; ++i){
        if(pre[i] == post[i]) return i;
    }
    return -1;
}