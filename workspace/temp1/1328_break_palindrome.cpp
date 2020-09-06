/* Nathan Zhu Stockton, CA, June 1st, 2020. 8:18 ams Tomorrow is the first day I start at Amex last year! :O
*  Leetcode 13298 | medium | medium
*  Category: misc tricks
*  Think about cases
*/


// "aabaa" "abb"
// "abba"
// "abbba" 

#include <string>
#include <algorithm>
using namespace std;
bool a_sandwich(string& s){
    for(int i = 0; i < s.size(); ++i){
        if(i == s.size() / 2) continue;
        if(s[i] != 'a') return false;
    }
    return true;
}

string breakPalindrome(string palindrome) {
    int N = palindrome.size();
    if(N == 1 or N == 0) return "";
    if(all_of(begin(palindrome), end(palindrome), [](char c){ return c == 'a'; })){
        palindrome.pop_back();
        return palindrome + "b";
    }
    //Normally, it is OK to replace first non-A character in a string with 'a'.  However, there is one
    // case where this will not break the palindrome, a case where there is an a-sandwich, like
    // "aacaa"  or "aza" or "aaaadaaaaa", all chars are a's except the character in the middle (also odd num chars)
    if(N % 2 == 1 && a_sandwich(palindrome)){
        palindrome.pop_back();
        return palindrome + "b";
    }
    else{
        // must be at least one non-a
        auto n = palindrome.find_first_not_of("a");
        palindrome[n] = 'a';
        return palindrome;
    }
}