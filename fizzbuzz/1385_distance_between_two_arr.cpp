/*  Nathan Zhu
*   Leetcode 1385 | easy | easy
*   One-line!
**/

#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;


int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
    return accumulate(begin(arr1), 
                        end(arr1), 
                        0, 
                        [&](int prev, int n1){
                            return (none_of(begin(arr2),
                                            end(arr2),
                                            [&](int n2){
                                                return abs(n1 - n2) <= d;
                                            }
                                            )) ? prev + 1 : prev;
                        });
}
