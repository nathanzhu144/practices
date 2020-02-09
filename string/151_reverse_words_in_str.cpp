/** 
 * Nathan zhu Jan 4th, 2019 3:12 pm Stockton California
 * Leetcode 151 | medium | not too bad
 * Category: string/fizzbuzz
 * 
 * Runtime: O(N)
 * This is the in-place soln with O(1) extra mem not including returned string
 * 
 */
#include <string>
#include <algorithm>
using namespace std;

void reverse(string& s, int start, int end){
    int i = start;
    int j = end;
    while(i < j) swap(s[i++], s[j--]);
}

// Reverses all words excluding whitespace.
void swap_words(string& s){
    int i = 0; int j = 0;
    
    while(j < s.size()){
        // j < i and i < j are geneius, the idea is that we need j to catch up to i and then i to catch up to j,
        while(i < j || (i < s.size() and s[i] == ' ')) i++;
        while(j < i || (j < s.size() and s[j] != ' ')) j++;
        reverse(s, i, j - 1);
    }
}

int trim_ws(string& s){
    int left = 0; int right = 0;
    while(right < s.size()){
        while(right < s.size() and s[right] == ' ') ++right;
        while(right < s.size() and s[right] != ' ') s[left++] = s[right++];
        while(right < s.size() and s[right] == ' ') ++right;               // This line is NECESSARY in cases where there's extra WS after last char (prevents extra soace)
        if(right < s.size()) s[left++] = ' ';
    }
    return left;
}

string reverseWords(string s) {
    reverse(s, 0, s.size() - 1);
    swap_words(s);
    int newsize = trim_ws(s);
    return s.substr(0, newsize);
}