/*  Leetcode 213 | medium | lol if you can't figure out the trick rlly hard
    Category: DP
    Runtime : O(N)
 */
#include <vector>
#include <unordered_map>
using namespace std;


/* 8:06 am, Nathan Zhu, in Amex Tower, 36th floor, Desk 202B
*  I spent 30 minutes trying to find why I was failing a test case
*  until I realized that leetcode was calling the wrong function
*  cause I changed name of the function.
*  
*  Insight behind house robber II.
*
*  Unlike house robber I, house robber II is a circle of houses,
*  so robbing house 0 will ensure that you cannot rob the last house.
*
*  However, you can break the chain of dependencies easily, if you realize
*  you can rob either the first house or not rob the first house you create a gap
*  in the circle of houses.  
*
*  If you have this line of houses, max of robbing this circle of houses 
*  
*     [house N] -> House 0   House 1   House 2    ...    House n-1  House n -> [house 0]
*
*  is same as 
*
*  MAX of 
*  House 0   House 1   House 2    ...    House n-1
*            House 1   House 2    ...    House n-1  House n
*  
*
*/

/**for house robber 1**/
int helper(vector<int> &nums, int index, unordered_map<int, int> &mem)
{

    if (mem.count(index) != 0){return mem[index];}
    if (index < 0){return 0;}

    mem[index] = std::max(helper(nums, index - 1, mem),
                          helper(nums, index - 2, mem) + nums[index]);

    return mem[index];
}

int house_robber_I(vector<int> nums)
{
    unordered_map<int, int> mem;
    return helper(nums, nums.size() - 1, mem);
}


/** SPECIFIC TO THIS VARIATION OF HOUSE ROBBER **/
int house_robber_II(vector<int> &nums)
{

    if (nums.size() == 0){ return 0;}
    if (nums.size() == 1){ return nums[0];}

    vector<int> first = vector<int>(nums.begin() + 1, nums.end());
    vector<int> second = vector<int>(nums.begin(), nums.end() - 1);

    return std::max(house_robber_I(first), house_robber_I(second));
}