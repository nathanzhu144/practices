/* Nathan Zhu May 22nd, 2020  had cool BBB meetup on zoom with everyone from Alexandra, Wesley, Austin, Eric, Shuta, Ritsuma, Sienna, Peifu, etc.
*  Leetcode 456 | medium | kinda hard
*  Category: Monotonic stack
*
*  I actually was pretty struggling on this question.
*  However, upon thinking of the numbers 1 and 3 as forming an interval, and if a number 2
*  is inside htat interval you return true it kinda makes more sense.
*
*  I think revisiting this one will be good, as I feel need more practice thinking about this one
*/

#include <vector>
#include <utility>
using namespace std;


bool find132pattern(vector<int>& nums) {
    vector<pair<int, int>> stk;
    
    for(auto num : nums){
        if(!stk.size() || num < stk.back().first) stk.emplace_back(num, num);
        else{
            int newmin = stk.back().first;
            while(stk.size() && num > stk.back().second){
                stk.pop_back();
            }
            if(stk.size() && stk.back().first < num && stk.back().second > num){
                return true;
            }
            stk.emplace_back(newmin, num);
        }
    }
    
    return false;
}