/* Nathan Zhu May 9th, 2020 
*  Leetcode 211 | medium | not bad
*  Category: Trie
*  Spent so long on find_helper because I had a 1-off indexing error lol
*/
#include <string>
#include <unordered_map>
using namespace std;

class TrieNode{
public:
    string word;
    bool ends = false;
    unordered_map<char, TrieNode*> table;
};

class Trie{
private:
    TrieNode* root;
    
    bool find_helper(string& s, int i, TrieNode* currnode){
        if(i == s.size()){
            return currnode->ends;
        }
        
        if(s[i] == '.'){
            for(auto [key, neigh] : currnode->table){
                if(find_helper(s, i + 1, neigh)) return true;
            }
        }
        else return currnode->table.count(s[i]) and find_helper(s, i + 1, currnode->table[s[i]]);
        return false;
    }
    
public:
    
    Trie(){ root = new TrieNode; }
    
    void add_word(string& s){
        TrieNode* curr = root;
        
        for(char ch : s){
            if(curr->table.count(ch) == 0) curr->table[ch] = new TrieNode;
            curr = curr->table[ch];
        }
        curr->ends = true;
        curr->word = s;
    }
    
    
    bool find(string& s){
        return find_helper(s, 0, root);
    }
    
};

class WordDictionary {
public:
    Trie t;
    /** Initialize your data structure here. */
    WordDictionary() {
        t = Trie();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        t.add_word(word);
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return t.find(word);
    }
};