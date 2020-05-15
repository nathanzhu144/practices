/* Nathan Zhu April 9th 1:05 am, Stockton, CA during COVID-19.  Meera, Shazeen and I met up today for virutal leetcode prep!
*  Leetcode 1073 | medium | medium
*  Category: Binary addition / bits stuff / misc tricks
*
*  This is a good question man.
*
*  Note that: [1, 1] and [1] add up to [0] and not [0, 0].
*/


#include <vector>
#include <algorithm>
#include <string>

using namespace std;

vector<int> addNegabinary(vector<int>& arr1, vector<int>& arr2) {
    vector<int> ret;
    
    reverse(arr1.begin(), arr1.end());
    reverse(arr2.begin(), arr2.end());
    
    int i1 = 0, i2 = 0;
    int carry = 0;
    
    while(i1 < arr1.size() or i2 < arr2.size() or carry != 0){
        int val1 = (i1 < arr1.size()) ? arr1[i1++] : 0;
        int val2 = (i2 < arr2.size()) ? arr2[i2++] : 0;
        
        int tot = val1 + val2 + carry;
        //C++ mods don't wrap to positive side, but can be negative too.
        ret.push_back((tot + 2) % 2);
        //If current carry is ordinarily one is regular binary addition, it actually is -1, 
            //because signs of alternating terms are flipped.  Furthermore, if a total sum at
            //a digit is -1, we should place a 1 in the digit's place, and make the carry. 
            //Reason is: 4 can be represented as -4 + 8, just as 16 can be rep as -16 + 32.
        if(tot == -1) carry = 1;
        else if(tot >= 2) carry = -1;
        else carry = 0;
    }
    
    
    if(all_of(ret.begin(), ret.end(), [](int x){ return x == 0;})) return {0}; // ADding two non-zeros can give a 0
    while(!ret.empty() and ret.back() == 0) ret.pop_back();                    // Removing leading 0s before reverse
    reverse(ret.begin(), ret.end());
    return ret;
}