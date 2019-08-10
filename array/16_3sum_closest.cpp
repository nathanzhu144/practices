/*  Nathan Zhu August 9th, 2019, Friday 8:52 pm.  Last night in NY man.  
    Leetcode 16 | medium | medium
    
    Very similar to 3-sum my man.
*/
# include <vector>
# include <cmath>
# include <climits> 
# include <algorithm>

using namespace std;

int threeSumClosest(vector<int>& arr, int target) {
    // [-1, 2, 1, -4]
    //   ^  
    //   first 
    //      ^ second 
    //             ^ third
    // first, second, third are indices
    std::sort(arr.begin(), arr.end());
    int smallestdiff = INT_MAX;
    int returned = INT_MAX;
    
    for(int first = 0; first < arr.size() - 2; ++first){
        int second = first + 1;
        int third = arr.size() - 1;
        while(second < third){
            int totsum = arr[first] + arr[second] + arr[third];
            // We can break out early if we find target, 
            if (totsum - target == 0){
                return target;
            }
            // This is the case where our total is too small, and we have to
            // increment second
            else if(totsum - target < 0){
                if(abs(totsum - target) < smallestdiff){
                    smallestdiff = abs(totsum - target);
                    returned = totsum;
                }
                while(second < third && arr[second] == arr[second + 1])
                    second += 1;
                second += 1;
            }
            // This is the case where total is too big, and we have to 
            // decrement third
            else{
                if(abs(totsum - target) < smallestdiff){
                    smallestdiff = abs(totsum - target);
                    returned = totsum;
                }
                while(second < third && arr[third] == arr[third - 1])
                    third -= 1;
                third -= 1;
            }
        }
    }
    
    return returned;
}