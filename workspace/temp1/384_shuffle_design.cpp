/* Nathan Zhu Sunday Stockton, CA. 11:05 pm June 19th, 2020.  I watched a william lin video of him doing 150 questions in 12 hours lol.  OK my dude.
*  Leetcode 384 | medium | medium
*  Category: Design, fisher-yates
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;


class Solution {
public:
    vector<int> cpy;
    
    Solution(vector<int> nums) {
        cpy = nums;
        //srand(time(NULL));
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return cpy;
    }
    
    /** Returns a random shuffling of the array. */
    // Draw a picture.  Basically, you assume array from [0, k] is shuffled, and [k + 1, N] is shuffled.
    vector<int> shuffle() {
        int i = cpy.size();
        vector<int> temp = cpy;
        while(i >= 1){
            int ridx = rand() % i;
            swap(temp[ridx], temp[--i]);
        }
        return temp;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */