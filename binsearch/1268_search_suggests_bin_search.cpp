/* Nathan Zhu April 22nd, 2020 Stockton, CA Covid-19
*  Leetcode 1268 | medium | medium
*  Category: Structures / Trie / Binary search
*
*  In this one, I don't use a trie, but use Binary search on a prefix.
*/
using namespace std;
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <tuple>

// Learned structured binding today!!

vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
    vector<vector<string>> ret;
    set<string> pset(products.begin(), products.end());
    vector<string> pvec(pset.begin(), pset.end());
    
    sort(pvec.begin(), pvec.end());
    
    int N = searchWord.length();
    
    
    for(int i = 1; i <= N; ++i){
        string prefix = searchWord.substr(0, i);
        auto it = lower_bound(pvec.begin(), pvec.end(), prefix);
        
        auto end = it;
        for(auto [i] = std::tuple{int(0)}; end != pvec.end() and end->find(prefix) == 0 and i < 3; end = next(end), i++) ;
        ret.emplace_back(it, end);
    }
    
    return ret;
}