
/* Nathan Zhu  Thursday July 16th, 2020  Hershal cancelled movie night this week!!! D:  Had leetcode prep w Meera, Neha, Shazeen
*  Leetcode n/a | n/a | hard
*  Category: Union Find
*/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>
#include <sstream>

using namespace std;


// union find class used as a helper
class UF{
public:
    unordered_map<string, string> parent;          // used in get_parent(string) to figure out which set a cell belongs to
    unordered_map<string, int> parent_to_max_ct;   // set label => max count in each set
    unordered_map<string, int> parent_to_curr_ct;  // set label => number of artifact pieces left to find in each set

    UF(){}

    // Create a new point in the UF class
    void create(string x){
        if(parent.count(x)) return;
        parent[x] = x;
        parent_to_curr_ct[x] = 1;
        parent_to_max_ct[x] = 1;
    }

    // returns empty if x is not part of any set
    // otherwise returns set label
    string get_parent(string x){
        if(!parent.count(x)) return "";
        if(parent[x] != x) parent[x] = get_parent(parent[x]);
        return parent[x];
    }

    // called assuming both string x and y exist in sets (i.e. they are labelled already)
    // joins two set labels & sizes of those labels, IF THEY ARE NOT SAME SET ALREADY
    bool join(string x, string y){
        string p1(get_parent(x)), p2(get_parent(y));
        if(p1 == p2) return false;   //check for same set
        parent[p1] = p2;
        parent_to_max_ct[p2] += parent_to_max_ct[p1];
        parent_to_curr_ct[p2] += parent_to_curr_ct[p1];
        return true;
    }
};

// Split helper function (string, char to split on) => vector of strings
vector<string> split(string& s, char delim){
    stringstream strstr(s);
    string temp;
    vector<string> ret;
    while(getline(strstr, temp, delim)){
        ret.push_back(temp);
    }
    return ret;
}

// Solution here
// Assumptions: No square is searched twice
//              No square has multiple artifacts
pair<int, int> solution(int N, string& artifacts, string& searched){
    UF u;  // union find instance used to get set label for coordinates

    // For each artifact, generate all the coordinates:
    // For each coordinate, categorize them in the same set in such a way that
    // u.get_parent(string coordinate) => returns set label
    for(auto& art : split(artifacts, ',')){
        vector<string> temp = split(art, ' ');
        string start(temp[0]), end(temp[1]);
        int startrow(stoi(start)), endrow(stoi(end));
        char startcol(start.back()), endcol(end.back());

        string startpos = to_string(startrow) + string(1, startcol);
        for(int row = startrow; row <= endrow; ++row){
            for(char ch = startcol; ch <= endcol; ++ch){
                string pos = to_string(row) + string(1, ch);
                u.create(pos);
                u.join(pos, startpos);
            }
        }
    }

    // For each search pos
    // If position is not an artifact continue
    // If position is an artifact, get the set label of that position
    // If position is first square in an artifact, increment incomplete by 1
    // If position is last square in an artifact, decrement incomplete by 1, increment complete by 1
    int complete(0), incomplete(0);
    for(auto& search : split(searched, ' ')){
        string set_label = u.get_parent(search);
        if(set_label.empty()) continue;      // position not on an artifact piece
        if(u.parent_to_curr_ct[set_label] == u.parent_to_max_ct[set_label]) incomplete++;
        if(u.parent_to_curr_ct[set_label] == 1){ incomplete--; complete++; }
        u.parent_to_curr_ct[set_label]--;
    }

    cout << "complete " << complete << " incomplete "<< incomplete << endl;
    return make_pair(complete, incomplete);
}


// Format: 
// "2B 2D 3D 4D 4A"
// artifacts = "1B 2C,2D 4D"
// N = 4
/*
Map 1        1  2  3  4  5  6  7  8  9  10
        A
        B   [1B 2B 3B [4B
        C    1C 2C 3C] 4C   [6C]
        D      [2D]    4D      [7D 8D 9D]
        E              4E]  [6E[7E 8E 9E 10E]
        F   [1F 2F 3F [4F]   6F]
        G    1G 2G 3G]
        H

Digging: "1F 2F 3F 1G 2G 3G" art1
         "2C"                incomplete1
         "6F"                incomplete2
         "6C"                art2
         "4B 4C 4D 4E"       art3
         "7E 8E 9E 10E"      art4
         "8D"                incompete3

         Note, add in random coords: 6A 7A 11A 1D 5E

         Should return [completed artifacts, incomplete arts] => [4, 3]
*/

int main(){
    string map1 = "1B 3C,2D 2D,4B 4E,4F 4F,6C 6C,6E 6F,1F 3G,7E 10E,7D 9D";
    string digs = "1F 2F 3F 1G 2G 3G 2C 6F 6C 4B 4C 4D 4E 7E 8E 9E 10E 8D 6A 7A 11A 1D 5E";

    solution(15, map1, digs);
}

//  [1B 2B 3B[4B
//   1C 2C 3C]4C   [6C]
//     [2D]   4D      [7D 8D 9D]
//            4E]  [6E[7E 8E 9E 10E]
//  [1F 2F 3F[4F]   6F]
//   1G 2G 3G]