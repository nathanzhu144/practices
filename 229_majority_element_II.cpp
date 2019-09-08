// Nathan Zhu  September 5, 2019 5:13 PM
// Leetcode 229 | medium | NOT EASY, how tf you come up with this in an interview
// Microsoft- Online Assessment, Leetcode
// Your interview score of 4.99/10 beats 47% of all users.
// Time Spent: 48 minutes 12 seconds
// Time Allotted: 1 hour


// Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

// Note: The algorithm should run in linear time and in O(1) space.

// Example 1:

// Input: [3,2,3]
// Output: [3]


#include <vector>
#include <algorithm>
using namespace std;

vector<int> majorityElement(vector<int>& nums) {
    if(nums.size() == 0) return {};
    
    int cand1 = 0, cand2 = 1, num1 = 0, num2 = 0;
    
    for(int& i : nums){
        if(i == cand1) num1++;
        else if(i == cand2) num2++;
        else if(num1 == 0){
            cand1 = i;
            num1 = 1;
        }
        else if(num2 == 0){
            cand2 = i;
            num2 = 1;
        }
        else{
            num1--; num2--;
        }
    }
    
    vector<int> ret;
    if(count(nums.begin(), nums.end(), cand1) > nums.size() / 3) ret.push_back(cand1);
    if(count(nums.begin(), nums.end(), cand2) > nums.size() / 3) ret.push_back(cand2);
    
    return ret;
}