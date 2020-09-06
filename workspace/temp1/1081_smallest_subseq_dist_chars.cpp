/* Nathan Zhu Sunday, June 14th, Stockton, CA, 5:42 pm, went to 85 deg C today. Just realized I might not go back to UM like ever again.  Damn
*  Leetcode 1081 | medium | the exact same q was a hard before lol
*  Category: Monotonic stack
*/

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;


// Intuition:
// Monotonic stack of increasing characters.
// Everytime we see a character smaller than top, pop until empty or no longer true.
// However, also need to consider "at least one of each character"
// Basically, do the same as above, but not pop if that char is last occurrence in string.
//
//
// ARGUMENT FOR "WHY THIS?"
// My argument for why we continue if used[text[i]] > 0.  This signifies that we have
// this character already in our sequence.
//
// Case 1: Placing it in will make it bump into a char whose occurrence is last.
//         Ex. bd [b],  d has no future occ
//         In this case, there is NO letter that will change bd, as d has no future occ.
//         Furthermore, note that since b already has one occurrence, we don't need another, and 
//         leaving the new b out will always result in a smaller string.
//               
// Case 2: Placing it will make it bump into a char whose value is smaller than it.
//         Ex. bea [b].  a is smaller than b, e has no future occ in this case
//         This can only happen if there's a character whose occurrence is last in between 
//         this b and last b.  Otherwise, there would not be a character less than b in between
//         the two bs.  This character will NEVER be dislodged in any stack popping, and therebfore
//         we can again safely discard the second b.

string smallestSubsequence(string text) {
    vector<char> st;
    int N(text.size());
    unordered_map<char, int> used, last_i;
    
    for(int i = 0; i < N; ++i) last_i[text[i]] = i;
    
    for(int i = 0; i < N; ++i){
        if(used[text[i]] > 0) continue;  // WHY THIS?
        while(st.size() && text[i] <= st.back() && i <= last_i[st.back()]){
            used[st.back()]--;
            st.pop_back();
        }
        
        st.push_back(text[i]);
        used[text[i]]++;
    }
    
    return string(begin(st), end(st));
}