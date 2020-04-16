/** Nathan Zhu Saturday, May 28th, 2020. Foundry Lofts, COVID-19
 *  Leetcode 1394 | easy | easy
 *  Category: fizzbuzz
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;

int findLucky(vector<int>& arr) {
    map<int, int> table;
    
    for(auto i: arr) table[i]++;
    
    for(auto it = table.rbegin(); it != table.rend(); ++it){
        if(it->first == it->second) return it->first;
    }
    return -1;
}