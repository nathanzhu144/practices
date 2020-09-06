/* Nathan Zhu 8:50 am, June 4th, 2020  Aoubtta start work!  Need to figure out the API issue today.
*  Leetcode 1324 | medium | medium
*  Category: Misc tricks
*/

#include <string>

using namespace std;

int maximum69Number (int num) {
    string num_str = to_string(num);
    auto pos = num_str.find_first_of("6");
    if(pos != string::npos) num_str[pos] = '9';
    return stoi(num_str);
}