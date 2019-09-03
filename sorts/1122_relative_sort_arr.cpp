#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
    int key[1001];
    int idx = 0;
    
    for(int i = 0; i < 1001; ++i) key[i] = 1000 + i;
    
    for(auto i: arr2) key[i] = idx++;
    
    sort(arr1.begin(), arr1.end(), [key](int c, int d){
        return key[c] < key[d];
    });
    
    return arr1;
}