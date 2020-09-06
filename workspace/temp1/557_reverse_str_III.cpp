/** Nathan Zhu, Stockton, CA.May 28th, 2020, 10:11 pm Saw amber and her mom on a walk today.  They were surprised Renying is working at Facebook.
 *  Leetcode 557 | easy | easy
 *  Category: fizzbuzz
 * 
 * 
*/

#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

string reverseWords(string s) {
    stringstream str(s);
    vector<string> ret;
    string buff;
    while(getline(str, buff, ' ')){
        reverse(buff.begin(), buff.end());
        ret.push_back(buff);
    }
    
    string res;
    for(int i = 0; i < ret.size(); ++i){
        if(i != 0) res += " ";
        res += ret[i];
    }
    
    return res;
}