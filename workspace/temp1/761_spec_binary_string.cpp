
/* Nathan Zhu Tuesday, Stockton, CA. 11:49 pm, June 16th, 2020 Called Sophie from Amex today.
*  Leetcode 761 | hard | damn beautiful, did not see this one coming
*  Category: recursion, pure recursion dude
*/
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// https://leetcode.com/problems/special-binary-string/discuss/113212/Think-of-it-as-Valid-Parentheses
// https://leetcode.com/problems/special-binary-string/discuss/113211/JavaC%2B%2BPython-Easy-and-Concise-Recursion


string helper(string s){
    int i(0), count(0);   // count counts balanced parens
                            // i marks beginning of next nested parens.
    
    vector<string> ret;
    for(int j = 0; j < s.size(); ++j){
        if(s[j] == '1') ++count;
        else --count;
        if(count == 0){ 
            ret.push_back("1" + helper(s.substr(i + 1, j - i - 1)) + "0");
            i = j + 1;
        }
    }
    
    sort(begin(ret), end(ret));
    reverse(begin(ret), end(ret));
    string res = "";
    for(auto s : ret) res += s;
    return res;
}
string makeLargestSpecial(string S) {
    return helper(S);
}