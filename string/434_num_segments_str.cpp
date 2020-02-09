/** Nathan Zhu January 2nd, 2019 4:33 pm Just got back from Santa Cruz, and point lobos yesterday.  Saw a bunch of mushrooms.
 *  Leetcode 434 | easy | EZ
 */
#include <cctype>
#include <string>

using namespace std;

int countSegments(string s) {
    int ret = 0;
    int N = s.size();
    
    for(int i = 0; i < N; ++i){
        // Move through all spaces to next char
        while(i < N and isspace(s[i])) ++i;
        
        // at this space i is at a new segment or is at end of string s.
        if (i == N) return ret;
        
        // Move through all chars, to next space
        while(i < N and !isspace(s[i])) ++i;
        ret++;
    }
    
    return ret;
}