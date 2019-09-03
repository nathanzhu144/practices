/** Nathan Zhu, Monday August 8th, 2019, 2:38 am PST, Stockton California in middle of night downstairs, 
 *                                                    Last week of internship is over.  Feels strange to be in New York yesterday.
 *  Leetcode 8 | medium | lol hard, annoying?
 *  Category: Fizzbuzz
 *  
 * find_first_not_of is cool, didn't know that, returns string::npos if cannot find in string
*/


#include <string>
#include <climits>

using namespace std;

int myAtoi(string str) {
    int sign = 1;
    std::size_t ind = str.find_first_not_of(' ');
    long long int res = 0;
    
    //Checks to see if index is in range
    if(ind == string::npos) return 0;
    
    //Finds sign if exists
    if(str[ind] == '-' || str[ind] == '+'){
        sign = (str[ind++] == '-') ? -1 : 1;
    }
    
    while(str[ind] >= '0' && str[ind] <= '9'){
        res = 10 * res + (str[ind++] - '0');
        if(res * sign <= INT_MIN) return INT_MIN;
        if(res * sign >= INT_MAX) return INT_MAX;
    }
    
    return sign * res;
    
}