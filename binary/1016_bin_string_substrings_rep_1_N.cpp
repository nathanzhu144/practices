// Nathan Zhu August 27th, 2019 10:57 pm
// Leetcode 1016 | medium | didn't think was so easy
// Category: binary
// Google- On-Site Interview
// Your interview score of 7.03/10 beats 90% of all users.
// Time Spent: 1 hour 4 minutes 24 seconds
// Time Allotted: 2 hours

// Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true 
// if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

// Example 1:
// Input: S = "0110", N = 3
// Output: true

#include <string>
#include <bitset>

using namespace std;

bool queryString(string S, int N) {
    while (N > 0){
        string s = bitset<32>(N--).to_string();
        
        // What this does.  We strip all zeroes off beginning of string, and then
        // we see if we can find it in S
        if(S.find(s.substr(s.find("1"))) == string::npos) return false;
    }
    
    return true;
}