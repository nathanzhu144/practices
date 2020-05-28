/*  Nathan Zhu May 18th, 2020.  9:25 pm, Stockton, CA, starting work tomorrow at Salesforce!
*   Leetcode 1386 | medium | not bad
*   Category: bitmasking
*/


#include <unordered_map>
#include <vector>

using namespace std;


int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
    unordered_map<int, int> table;
    
    int ret = 2 * n;
    
    for(auto vec: reservedSeats){
        auto [row, col] = pair{vec[0] - 1, vec[1] - 1};
        table[row] |= (1 << col);
    }
    
    // An observation we can make is we optimally want one family to sit on the left and the right, for two
    // families per row.  However, this is now always possible.  If it is not true that both left and right
    // are not reserved, we can maybe still sit one family.
    // The masks represent the seating arrangements of the family.
    //
    // Furthermore, we do subtraction instead of addition because the reservations are sparse in the test cases.
    for(auto [key, mask] : table){
        bool mid = ((0b1110000111 | mask) == 0b1110000111);
        bool left = ((0b1000011111 | mask) == 0b1000011111);
        bool right = ((0b1111100001 | mask) == 0b1111100001);
        
        if(left && right) continue;
        else if(left || right || mid) ret -= 1;
        else ret -= 2;
    }
    
    return ret;
}