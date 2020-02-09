/** Nathan Zhu Feb 1st, 2020.  Foundry Lofts 
 *  Leetcode 8 | medium | damn annoying lol
 *  Category: fizzbuzz
 *  
*/

#include <string>
#include <climits>


using namespace std;

int myAtoi(string str) {
    int sign = 1;
    
    std::size_t ind = str.find_first_not_of(' ');
    
    if(ind == string::npos) return 0;
    
    if(str[ind] == '-' or str[ind] == '+') sign = (str[ind++] == '-') ? -1 : 1;
    
    long long ret = 0;
    while(str[ind] >= '0' and str[ind] <= '9'){
        ret = ret * 10 + (str[ind] - '0');
        if(sign * ret <= INT_MIN) return INT_MIN;
        else if(sign * ret >= INT_MAX) return INT_MAX;
        ind++;
    }
    
    return sign * ret;
}