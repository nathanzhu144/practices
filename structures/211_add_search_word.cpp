
/**  Nathan Zhu December 31st, 2019 Just went to see the swimming pool of Heart's castle from afar yesterday. 6:20 am.  Last day of 2019.
 *   Leetcode 211 | medium | medium
 *   Category: Data structure design / Trie
 */
#include <unordered_map>
#include <string>

using namespace std;

class Node{
    public:
    unordered_map<char, Node*> table;
    bool ends_here = false;
    string word;
};

class WordDictionary {
public:
    Node* root;
    
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new Node();
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        Node* curr = root;
        
        for(char c : word){
            if(!curr->table[c])
                curr->table[c] = new Node();
            curr = curr->table[c];
        }
        curr->word = word;
        curr->ends_here = true;
    }
    
    /*Does a modified DFS everytime sees a .*/
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search_helper(string& word, Node* n){
        if(word == "" and n->ends_here) return true;
        if(word[0] == '.'){
            for(auto& key_pair : n->table){
                string temp = word.substr(1);
                if(search_helper(temp, n->table[key_pair.first])) return true;
            }
        }
        else{
            if(n->table.find(word[0]) != n->table.end()){
                string temp = word.substr(1);
                return search_helper(temp, n->table[word[0]]);
            }
        }
        return false;
    }
    
    bool search(string word) {
        return search_helper(word, root);
    }
};
