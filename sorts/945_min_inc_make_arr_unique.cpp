/** Nathan Zhu Tuesday, April 14th, 2020.  3:18 pm, Stockton, CA Covid-19
 *  Leetcode 945 | medium | medium ?  not too easy
 *  Category: Sorting
 * 
 *  Runtime: NLogN
 *  
*/
#include <algorithm>
#include <vector>
using namespace std;


int minIncrementForUnique(vector<int>& A) {
    if(!A.size()) return 0;
    sort(A.begin(), A.end());
    int ret = 0, need = A[0];
    
    for(auto num : A){
        ret += max(0, need - num);
        need = max(num + 1, need + 1);
    }
    
    return ret;
}