/*  Nathan Zhu April 14th, 2020. 8:01 pm, just finished running/walking 3m, Stockton, CA COVID-19
*   Leetcode 721 | medium | easy
*   Category: Union-find w path compression
*
*/

using namespace std;

#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>


class UF{
public:
    unordered_map<string, string> table;
    void make_acc(string s){
        table[s] = s;
    }
    string find(string s){
        if (table[s] != s){
            table[s] = find(table[s]);
        }
        return table[s];
    }
    
    void union_(string a, string b){
        string p1 = find(a);
        string p2 = find(b);
        if(p1 == p2) return;
        table[p1] = p2;
    }
    
    
};


class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, string> email_to_user;
        unordered_set<string> all_emails;
        
        UF u = UF();
        for(vector<string>& v : accounts){
            for(string& email : vector<string>(v.begin() + 1, v.end())){
                string username = v[0];
                email_to_user[email] = username;
                
                if(!all_emails.count(email)) u.make_acc(email);
                all_emails.insert(email);
                u.union_(v[1], email);
            }
        }
        
        unordered_map<string, vector<string>> acc;
        for(string s : all_emails){
            acc[email_to_user[s] + " " + u.find(s)].push_back(s);
        }
        
        vector<vector<string>> ret;
        for(pair<string, vector<string>> p : acc){
            sort(p.second.begin(), p.second.end());
            vector<string> vec = p.second;
            vector<string> curr_acc;
            curr_acc.push_back(email_to_user[vec[0]]);
            curr_acc.insert(curr_acc.end(), vec.begin(), vec.end());
            ret.push_back(curr_acc);
        }
        
        return ret;
    }
};