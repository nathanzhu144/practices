/* Nathan Zhu May 11th, 2020, Stockton, CA, COVID-19
*  Leetcode 1392 | hard | easy with KMP
*  Category: KMP
*/

#include <vector>
#include <string>

using namespace std;

vector<int> make_KMP(string s){
    int N = s.size();
    vector<int> kmp (N, 0);
    int j(0), i(1);
    
    while(i < N){
        if(s[i] == s[j]){
            kmp[i] = j + 1;
            i++; j++;
        }
        else{
            if(j != 0){
                j = kmp[j - 1];
            }
            else{
                i++;
            }
        }
    }
    
    return kmp;  // do not need to return ref due to NRVO.
}

string longestPrefix(string s) {
    vector<int> kmp(make_KMP(s));
    int N = s.size();
    return s.substr(0, kmp.back());
}