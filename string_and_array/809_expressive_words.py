# Nathan Zhu August 31st, 2019 10:45 am
# Leetcode 809 | medium | medium
# 
# Google- On-Site Interview
# Your interview score of 4.57/10 beats 76% of all users.
# Time Spent: 1 hour 59 minutes 25 seconds
# Time Allotted: 2 hours

# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

# For some given string S, a query word is stretchy if it can be made to be equal to S by
# any number of applications of the following extension operation: choose a group consisting 
# of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but
# we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension 
# like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be
# stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

# Given a list of query words, return the number of words that are stretchy. 



class Solution {
public:
    bool check(string& extend, string& original){
        int n = extend.size(), m = original.size(), o = 0;
        
        for (int e = 0; e < extend.size(); ++e){
            if (extend[e] == original[o]) o++;
            else if (e > 0 && e + 1 < extend.size() && extend[e - 1] == extend[e] && extend[e] == extend[e + 1]);
            else if (e > 1 && extend[e] == extend[e - 1] && extend[e - 1] == extend[e - 2]);
            else return false;
        }
        
        return o == original.size();
        
    }
    
    int expressiveWords(string S, vector<string>& words) {
        vector<string> ret;
        
        for(auto& w: words){
            if (check(S, w)) ret.push_back(w);
        }
        return ret.size();
    }
};