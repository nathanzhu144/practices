/* Nathan Zhu May 19th, 2020. 2nd day at Salesforce!  Met my manager today.
*  Leetcode 1352 | medium | damn I struggled too much on this one
*  Category: Design
*/

#include <vector>

using namespace std;
class ProductOfNumbers {
private:
    vector<long> prefix;
public:
    ProductOfNumbers() {
        prefix = {1};
    }
    
    void add(int num) {
        if(num == 0) prefix = {1};
        else prefix.push_back(prefix.back() * num);
    }
    
    int getProduct(int k) {
        return (prefix.size() <= k) ? 0 : (prefix.back() / prefix[prefix.size() - k - 1]);
    }
};