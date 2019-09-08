// Nathan Zhu September 5, 2019 5:13 PM
// Leetcode 796 | easy | damn this soln man


// Microsoft- Online Assessment, Leetcode
// Your interview score of 4.99/10 beats 47% of all users.
// Time Spent: 48 minutes 12 seconds
// Time Allotted: 1 hour

// We are given two strings, A and B.
// A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

// Example 1:
// Input: A = 'abcde', B = 'cdeab'
// Output: true
 #include <string>

 using namespace std;
 
 bool rotateString(string A, string B) {
        return (A.size() == B.size() && (A + A).find(B) != string::npos);
    }