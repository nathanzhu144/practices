/* Nathan Zhu Thursday, May 22nd, 2020 12:29 am, 3rd day at Salesforce just finished
*  Leetcode 1025 | easy | think this should be medium
*  Category: DP, minimax
*/

#include <unordered_map>

using namespace std;

bool helper(int n, unordered_map<int, bool>& table){
    if(table.count(n)) return table[n];
    if(n <= 1) return false;  // no moves with n <= 1
    
    for(int i = 1; i < n; ++i){
        if(n % i == 0 && !helper(n - i, table)){
            table[n] = true;
            return table[n];
        }
    }
    table[n] = false;
    return table[n];
}


bool divisorGame(int N) {
    unordered_map<int, bool> table;
    return helper(N, table);
}