/**
 * Nathan Zhu April 14th, 2020, Stockton, CA, COVID-19
 * Leetcode 1411 | hard | yeah pretty hard
 * Category: DP
 * 
 * Draw out the states.
*/

int numOfWays(int n) {
    long threes(6), twos(6), MOD(1e9 + 7);
    
    for(int i = 1; i < n; ++i){
        long temp_threes = threes * 2 + twos * 2;
        long temp_twos = twos * 3 + threes * 2;
        threes = temp_threes % MOD;
        twos = temp_twos % MOD;
    }
    
    return (twos + threes) % MOD;
}