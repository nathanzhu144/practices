/*  Nathan Zhu Auguest 2nd, 2019. 7:57 pm, EST, 55th John Street.  We had a bomb ass presentation today.
    Leetcode 811 | easy | EZ
    https://leetcode.com/problems/subdomain-visit-count/
    Category: Fizzbuzz

    First time coding something in C++ for a while.  substr is so useful for string questions.
 */

using namespace std;
#include <vector>
#include <string>
#include <unordered_map>

vector<string> subdomainVisits(vector<string>& cpdomains) {
    unordered_map<string, int> c;
    

    for(auto cp: cpdomains){
        //Step 1: We parse the input string and split it into the count
        //        component, and also the domain.
        int stringidx = cp.find(" ");
        int num = stoi(cp.substr(0, stringidx));
        string s = cp.substr(stringidx + 1);
        
        for(int i = 0; i < s.size(); ++i){
            //Everytime we find a ., we index the suffix after . in
            //For example, discuss.leetcode.com can be broken down into 
            //             leetcode.com & .com
            if (s[i] == '.')
                c[s.substr(i + 1)] += num;
        }
        //indexing original string
        c[s] += num;
    }
    
    vector<string> res;
    for(auto k: c){
        res.push_back(to_string(k.second) + " " + k.first);
    }
    
    return res;
}