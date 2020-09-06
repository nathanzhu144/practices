/* Nathan Zhu Tuesday, Stockton, CA. 7:23 pm, June 16th, 2020 Called Sophie from Amex today.
*  Leetcode 1297 | medium | medium
*  Category: sliding window
*  Rolling hash would be true O(N), but would be harder to code.
*/

#include <unordered_map>
using namespace std;

int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
    int ret(0), N(s.size()), num_chars(0);
    unordered_map<char, int> char_cts;
    unordered_map<string, int> word_cts;
    
    for(int i = 0; i < N; ++i){
        char_cts[s[i]]++;
        if(char_cts[s[i]] == 1) num_chars++;
        if(i > minSize - 1){
            char_cts[s[i - minSize]]--;
            if(char_cts[s[i - minSize]] == 0) num_chars--;
        }
        
        if(i >= minSize - 1 && num_chars <= maxLetters){
            auto new_w = s.substr(i - (minSize - 1), minSize);
            word_cts[new_w]++;
            ret = max(ret, word_cts[new_w]);
        }  
    }
    return ret;
}