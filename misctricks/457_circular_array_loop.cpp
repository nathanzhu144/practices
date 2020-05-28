/*  Nathan Zhu 5:45 am Saturday May 16th, 2020.  Man, my wisdom tooth kinda hurts today.  Drinking a lot of cold water rn.
*   Leetcode 457 | medium | not too bad
*   Category: misc tricks, finding cycle in linked list in O(1) memory and with more edge cases.
*/


using namespace std;
#include <vector>

// assume 0 and positive are same sign
// not dependent on number of bits or 2s complement repr
bool same_sign(int a, int b){
    return (a < 0 == b < 0);
}

// the + num.size() is because C++ does not convert mods from negative to positive.
int find_next(vector<int>& nums, int pos){
    return ((nums[pos] + pos) + nums.size()) % nums.size();
}

bool find_cycle(vector<int>& nums, int pos){
    int slow(pos), fast(pos);

    while(true){
        int curr = fast;
        int fnext = find_next(nums, curr);
        int fnext_next = find_next(nums, fnext);
        if(curr == fnext or fnext == fnext_next) return false;      // cycle of 1 length not cycle, note we need to check both edges.
                                                                    // case like [-1, -2, -3, -4, -5], where -1 -> -5 -> -5 - -5 ... -5
                                                                    // involve the second edge being caught in a cycle.
        if(!same_sign(nums[curr], nums[fnext]) or !same_sign(nums[fnext], nums[fnext_next])) return false;
        
        slow = find_next(nums, slow);
        fast = fnext_next;
        if(slow == fast) return true;    // there is a cycle
    }
    
    return false; //never gets here.
}
bool circularArrayLoop(vector<int>& nums) {
    for(int i = 0; i < nums.size(); ++i){
        if(find_cycle(nums, i)) return true;
    }
    return false;
}