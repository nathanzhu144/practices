/* Nathan Zhu May 19th, 2020 2nd day of work at SF
*  Leetcode 949 | easy | ehh
*  Category: Backtracking
*
*  Ok, the use of prev permutation is actually really cool, so there are so many edge caess 
*  with time, but the search space is small, and in c++ there isa function where you can get the
*  previous permutation of something.
*/
#include <string>

#include <algorithm>
#include <vector>
using namespace std;

string largestTimeFromDigits(vector<int>& A) {
    sort(begin(A), end(A), std::greater<int>());
    
    do{
        if((A[0] <= 1 || (A[0] == 2 && A[1] < 4)) && A[2] < 6)
            return to_string(A[0]) + to_string(A[1]) + ":" + to_string(A[2]) + to_string(A[3]);
    }while(prev_permutation(begin(A), end(A)));
    return "";
}