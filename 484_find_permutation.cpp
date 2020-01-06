/* Nathan Zhu January 2nd, 2019 6:53 pm Just came back from Santa Cruz yesterday at point lobos, just finished trimming the plants.
*  Leetcode 484 | medium | medium
*  Category: Misc tricks
*  Runtime: O(N)
*  Very tricky, and may not think of at first.
*  
*  
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

/** The lowest lexicographical permutation can be easily found by starting at
*  [1, 2, 3, 4, 5, 6, 7]   (an increasing list)
*   I  I  D  D  D  I
*
*  Then, finding all substrings with Ds, and reversing them, like
# 
#  [1, 2, 6, 5, 4, 3 7]
*
*  Because of how an increasing sequence is defined, we reverse 1 letter after the D, not
*  just up to the last D.
*  
*/ 
vector<int> findPermutation(string s) {
    int N = s.size();
    vector<int> ret;
    
    for(int i = 1; i <= N + 1; ++i) ret.push_back(i);
    
    for(int i = 0; i < N; ++i){
        if(s[i] == 'D'){
            int left = i;
            while(i + 1 < N and s[i + 1] == 'D') ++i;
            int right = i + 1;
            
            while(left < right){
                swap(ret[left], ret[right]);
                left++; right--;
            }
        }
    }
    return ret;

}