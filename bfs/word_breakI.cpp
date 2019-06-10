/*  Nathan Zhu Monday 12:18 pm June 10, 2019
*   Word break worst case is 2^n 
*   
*   So, word break classically can be solved with DP, but it can
*   also be efficiently solved with a BFS.  
*
*   "We can use a graph to represent possible solutions, where the vertices
*    of the graph are the positions of the first characters of the words and
*    each edge represents a word."
*
*   Ex. Dict = { "nightmare", "night", "mare"}
*            string = nightmare
*    The graph would look like, where there is an edge from
*    [0, 5], [5, 9] and [0, 9]
*
*    0 ->  5 -> 9
*    |          ^
*     ----------
*
*    Seeing the graph, the question is simply whether we can
*    generate a path from 0 to 9. The most efficient way of traversing
*    the graph is using BFS.  To avoid processing duplicate nodes, we use a 
*    visited hash set.
*
*    Time complexity is O(n^2) with visited.  This observation stems from the 
*    fact that there are n^2 substrings in a string.  This also can be observed from
*    fact that in a graph with N nodes where all N nodes are connected, we have
*    a total of 
*
*       (n - 1) + (n - 2) + ... + 2 + 1 = 
*    Space complexity is 
*    O(n) as we are only storing up to n nodes.
 */
#include <string>
#include <queue>
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;


bool word_breakI(string str, unordered_set<string> dictionary){
    unordered_map<int, bool> visited;

    queue<int> BFS;
    BFS.push(0);

    while(!BFS.empty()){
        int front = BFS.front();
        BFS.pop();

        if (visited.find(front) == visited.end()){
            visited[front] = true;

            for(unsigned int i = front; i < str.size(); ++i){
                string word = string(str, front, i - front + 1);   // i - front + 1 is length of string we are making

                if(dictionary.find(word) != dictionary.end()){
                    BFS.push(i + 1);

                    if(i + 1 == str.length()){
                        return true;
                    }
                }
            }
        }
    }
    return false;
}