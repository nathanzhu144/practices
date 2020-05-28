/* Nathan Zhu, May 20th, 2020, Stockton, CA.  3rd day of Salesforce internship!
*  Leetcode 839 | hard | not bad
*  Category: UF
*
*/

#include <unordered_map>
#include <string>
#include <vector>
using namespace std;
class UF{
private:
    unordered_map<string, string> parent;
    int num_graphs;
public:
    UF() : num_graphs(0){}
    
    void touch(string& str){
        if(parent.count(str)) return;
        num_graphs++;
        parent[str] = str;
    }
    
    string find(string& str){
        if(parent[str] != str) parent[str] = find(parent[str]);
        return parent[str];
    }
    
    void join(string& str1, string& str2){
        string p1(find(str1)), p2(find(str2));
        if(p1 == p2) return;
        parent[p1] = p2;
        num_graphs--;
    }
    
    int get_ct(){ return num_graphs; }
};

bool similar(string& a, string& b){
    int change = 0;
    for(int i = 0; i < a.size(); ++i){
        if(a[i] != b[i]) change++;
        if(change > 2) return false;
    }
    return change == 2;
}


class Solution {
public:
    int numSimilarGroups(vector<string>& A) {
        int N(A.size());
        UF u;
        
        for(int i = 0; i < N; ++i){
            for(int j = i + 1; j < N; ++j){
                u.touch(A[i]);
                u.touch(A[j]);
                if(similar(A[i], A[j])) u.join(A[i], A[j]);
            }
        }
        return u.get_ct();
    }
};