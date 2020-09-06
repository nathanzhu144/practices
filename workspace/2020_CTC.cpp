
#include <vector>
#include <cassert>
using namespace std;

// how many moves can we move right?

int solution(vector<int>& arr){
    int N(arr.size());
    vector<int> right_m(N, -1);  // what pos can we get to going right
    vector<int> left_m(N, -1);   // what pos can we get to going left

    for(int i = 0; i < N; ++i){
        if(i == 0 || arr[i] < arr[i - 1]){
            int j = i;
            while(j < N - 1 && (arr[j] <= arr[j + 1])) ++j;
            right_m[i] = j;
        }
        else right_m[i] = right_m[i - 1];
    }

    for(int i = N - 1; i >= 0; --i){
        if(i == N - 1 || arr[i] < arr[i + 1]){
            int j = i;
            while(j > 0 && arr[j] <= arr[j - 1]) --j;
            left_m[i] = j;
        }
        else left_m[i] = left_m[i + 1];
    }

    int ret = 0;
    for(int i = 0; i < N; ++i) ret = max(right_m[i] - left_m[i], ret);
    return ret;
}

int main(){
    // assert(solution([2, 6, 8, 5]) == 2)
    // assert(solution([1, 5, 5, 2, 6]) == 3)
    // assert(solution([1, 1,]) == 1)
    vector<int> a1 = {2, 6, 8, 5};
    vector<int> a2 = {1, 5, 5, 2, 6};
    vector<int> a3 = {1, 1};
    vector<int> a4 = {2, 3, 6, 7, 1, 8, 9, 10, 11};
    //print(solution([2, 3, 6, 7, 1, 8] + [2] * (2 **10)))
    assert(solution(a4) == 7);
    assert(solution(a1) == 2);
    assert(solution(a2) == 3);
    assert(solution(a3) == 1);


}