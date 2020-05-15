/* Nathan Zhu April 14th, 2020 Talked to stanford guy at citadel today, he told me to do more leetcode.  Good gig.
*  Leetcode 15 | medium | easy
*  Category: misc tricks
*/

#include <vector>
#include <algorithm>
using namespace std;
vector<vector<int>> threeSum(vector<int>& arr) {
    int N = arr.size();
    vector<vector<int>> ret;
    
    sort(arr.begin(), arr.end());
    
    for(int i = 0; i < N; ){
        int j(i + 1), k(N - 1);
        
        while(j < k){
            int tot = arr[i] + arr[j] + arr[k];
            if(tot == 0){
                ret.push_back({arr[i], arr[j], arr[k]});
                while(j < k and arr[j] == arr[j + 1]) j++;
                j++;
                while(j < k and arr[k] == arr[k - 1]) k--;
                k--;
            }
            else if(tot > 0) k--;
            else j++;
        }
        
        while(i < N - 2 && arr[i] == arr[i + 1]) i++;
        i++;
    }
    
    return ret;
}