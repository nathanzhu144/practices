/* Nathan Zhu December 24th, 2019 Did this on paper way to sugar bowl ski resort on December 21s, 2019
*  Leetcode 680 | easy | easy
*  Category: recursion
*
*  This question is about whether a word can form a palindrome if at most 1 char is removed,
*  I solved it with a recursive function where n chars can be removed.
* 
*/

#include <string>
#include <iostream>
using namespace std;

bool helper(string s, int left, int right, int num_changes){
    if(num_changes < 0) return false;
    
    while (left < right){
        if(s[left] == s[right]){
            left++; right--;
        }
        else return helper(s, left + 1, right, num_changes - 1) or helper(s, left, right - 1, num_changes - 1);
    }
    return true;
}
bool validPalindrome(string s) {
    return helper(s, 0, s.size() - 1, 1);
}