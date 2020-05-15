/* Nathan Zhu May 14th, 2020.  I struggled 2 hours on this problem cuz I Was passing in 1 << n as the bitmask lol.
*  Leetcode 1434 | hard | ok, concept was simple, but I didn't get bitmasking.
*  Category: bitmasking DP
*/
using namespace std;

#include <vector>
#include <cmath>

/**
 * For this problem, they made it so there are a lot more hats than people, so instead of looking at this problem 
 * at the lens of matching people to hats, we should look at it from the angle of matching people to hats.'
 * 
 * We consider at hat h, and assign people to this hat.
 * 
 * Reason is num hats is  0 <= h <= 40
 *           num ppl is 0 <= p <= 10
 * 
 * Since we have so many hats, our bitmask is length 40, and at most 10 bits will be set.
 * When we reverse the problem, our bitmask is length 10, and we will use at least 10 bits.
 * The 40-bit bitmask is too sparse, leading to significantly less pruning in our recursive calls.
*/
const int MOD = pow(10, 9) + 7;

int helper(vector<vector<int>>& hat_to_person, int hat, int mask, int num_ppl, vector<vector<int>>& table){
    if(mask + 1 == (1 << num_ppl)) return 1;        // When all num_ppl 0s in mask are 1s, we have a valid config.
    if(hat >= 40) return 0;
    if(table[hat][mask] != -1) return table[hat][mask];
    
    // The reason we init ret to this is to account for not wearing this hat.
    // We don't have to wear all the hats, and some solns might come from excluding this hat.
    int ret = helper(hat_to_person, hat + 1, mask, num_ppl, table);    
    
    // Logic of this is simple.
    // We are trying to now increment ret by all possibilities coming from WEARING THIS HAT.
    // We go through all people who can wear this hat, and attempt to make them wear this hat.
    for(auto person : hat_to_person[hat]){
        // Tests to see if this person is wearing another hat already.
        if((mask & (1 << person)) == 0){
            // This person is not wearing a hat yet, make them wear the hat.
            ret += helper(hat_to_person, hat + 1, mask | (1 << person), num_ppl, table);
            ret %= MOD;
            // Since we didn't pass mask by reference, no need to backtrack, but if we did, we would do this 
            // to allow us to calculate other solns in which this person is available to wear other hats.
            // mask ^= (1 << person);
        }
    }
    
    table[hat][mask] = ret;
    return ret;
}

int numberWays(vector<vector<int>>& hats) {
    int num_ppl = hats.size();
    int mask(1 << num_ppl);                           // mask should have num_ppl 0s to represent num_ppl people.
    vector<vector<int>> hat_to_person(40);            // there are at most 40 hats.
    vector<vector<int>> table(40, vector<int>(1 << num_ppl, -1));
    
    for(int person = 0; person < hats.size(); ++person){
        for(auto hat : hats[person]){
            hat_to_person[hat - 1].push_back(person);  // make hats 0-idxed
        }
    }
    
    return helper(hat_to_person, 0, 0, num_ppl, table);
}