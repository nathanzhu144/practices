/* Nathan Zhu
*  Leetcode 978 | medium | medium
*  This is the exact question on the DRW hackerrank.
*/
#include <vector>
using namespace std;

int difference(int a, int b){
    if (a == b) return 0;
    if (a < b) return -1;
    else return 1;
    
}

int maxTurbulenceSize(vector<int>& A) {
    A.push_back(A.back());

    int longest = 0;
    int currdelta = 0;
    int prevdelta = 0;
    int curr_len = 0;

    for(unsigned int i = 1; i < A.size(); ++i){
        currdelta = difference(A[i - 1], A[i]);

        if(currdelta == 0){
            curr_len = 1;
        }
        else if(currdelta * prevdelta == -1){
            curr_len += 1;
        }
        else{
            curr_len = 2;
        }

        prevdelta = currdelta;
        longest = max(curr_len, longest);
    }

    return longest;
}
