/* Nathan zhu May 14th, 2020 1:55 pm. Stockton, CA, COVID-19.  Starting at Salesforce in four days.
*  Leetcode 1428 | medium | medium
*  Category: binary search
*  
*/

#include <vector>
#include <limits>
using namespace std;

class BinaryMatrix {
public:
    int get(int row, int col);
    vector<int> dimensions();
};
  
int search(BinaryMatrix& b, int r, int C){
    int left(0), right(C - 1);
    int ret = numeric_limits<int>::max();
    while (left <= right){
        int mid = (right - left) / 2 + left;
        if(b.get(r, mid)){
            ret = mid;
            right = mid - 1;
        }
        else left = mid + 1;
    }
    return ret;
}

int leftMostColumnWithOne(BinaryMatrix &b) {
    vector<int> dim = b.dimensions();
    if(!dim[0] or !dim[1]) return -1;
    int R(dim[0]), C(dim[1]);
    
    int ret = numeric_limits<int>::max();
    for(int r = 0; r < R; ++r) ret = min(search(b, r, C), ret);
    
    return (ret == numeric_limits<int>::max()) ? -1 : ret;
}