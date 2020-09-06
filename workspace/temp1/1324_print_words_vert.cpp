/* Nathan Zhu 8:50 am, June 4th, 2020  Aoubtta start work!  Need to figure out the API issue today.
*  Leetcode 1324 | medium | medium
*  Category: Misc tricks
*  I kinda like this kind of question now, similar to the PAYPALSTRING question.
*s
*/
#include <sstream>
#include <vector>
#include <string>

using namespace std;

vector<string> printVertically(string vertstr) {
    vector<string> s;
    vector<string> ret;
    stringstream strstr(vertstr);
    string temp;
    int N = 0;
    while(getline(strstr, temp, ' ')){
        s.push_back(temp);
        N = max(int(temp.size()), N);
    }

    // i is vertical idx
    // j is word index.
    for(int i = 0; i < N; ++i){
        string curr;
        for(int j = 0; j < s.size(); ++j){
            curr += (i < s[j].size()) ? s[j][i] : ' ';
        }
        while(curr.size() > 0 && curr.back() == ' ') curr.pop_back();
        ret.push_back(curr);
    }
    
    return ret;
}