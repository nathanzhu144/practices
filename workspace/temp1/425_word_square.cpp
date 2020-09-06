/* Nathan Zhu Wednesday, Stockton, CA. 10:47 pm, June 17th, 2020.  Tomorrow is our 2nd anniversary. :)  Also, about to hit 50% of questions done on LC today.  49.9% rn!
*  Leetcode 425 | hard | good onem can't figure out a clean way to do this without globals in c++
*  Category: Backtracking / Trie
*/


#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;

struct Node{
    string word = "";
    unordered_map<char, Node*> mapping;
    bool ends_here = false;
};

class Trie{
private:
    Node* root = nullptr;
    
public:
    Trie(){ root = new Node(); }
    
    void insert(const string& w){
        Node* curr = root;
        
        for(auto ch : w){
            if(!curr->mapping.count(ch)) curr->mapping[ch] = new Node();
            curr = curr->mapping[ch];
        }
        
        curr->word = w;
        curr->ends_here = true;
    }
    
    vector<string> get_cand(const string& w){
        Node* curr = root;
        vector<string> ret;
        vector<Node*> st;
        
        for(auto ch: w){
            if(!curr->mapping.count(ch)) return ret;
            curr = curr->mapping[ch];
        }
        
        st.push_back(curr);
        while(st.size()){
            auto ptr = st.back(); st.pop_back();
            if(ptr->ends_here) ret.push_back(ptr->word);
            for(auto [c, neigh_ptr] : ptr->mapping) st.push_back(neigh_ptr);
        }
        
        return ret;
    }
};


vector<vector<string>> wordSquares(vector<string>& words) {
    Trie t = Trie();
    vector<vector<string>> ret;
    vector<vector<string>> st = {{}};
    
    unordered_set<string> temp(words.begin(), words.end());
    for(auto word : temp) t.insert(word);
    if(words.empty()) return ret;
    int wsize = words[0].size();
    
    while(st.size()){
        vector<string> top = st.back(); st.pop_back();
        
        // we completed a word square
        if(top.size() == wsize){
            ret.push_back(top);
            continue;
        }
        
        // finding correct prefix.
        string prefix = "";
        if(top.size() > 0){
            int c = top.size();
            for(int r = 0; r < c; ++r) prefix += top[r][c];
        }
        
        // look for possible next words in next level of word square
        for(auto cand : t.get_cand(prefix)){
            vector<string> neigh = top;
            neigh.push_back(cand);
            st.push_back(neigh);
        }
    }
    
    return ret;
}
