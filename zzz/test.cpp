#include <vector>
#include <set>
#include <unordered_map>


using namespace std;

int main(){
    return 0;
}



// you can use includes, for example:
// #include <algorithm>
#include <map>
#include <set>
#include <climits>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

void decrement_table(map<int, int>& table, int a){
    table[a]--;
    if(table[a] == 0) table.erase(a);
}
int solution(vector<int> &A, int K) {
    // write your code in C++14 (g++ 6.2.0)
    int ret = INT_MAX;
    map<int, int> table;

    for(auto num : A){
        table[num]++;
    }

    for(int i = 0; i < K; ++i){
        decrement_table(table, A[i]);
    }

    int right = K;
    ret = min(table.rbegin()->first - table.begin()->first, ret);
    while(right <= A.size()){
        ret = min(table.rbegin()->first - table.begin()->first, ret);
        if(right < A.size()) decrement_table(table, A[right]);
        table[A[right - K]]++;
        right++;
    }

    return ret;
}


q2

// you can use includes, for example:
// #include <algorithm>
#include <unordered_map>
#include <iostream>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int ceil_div(int a, int b){
    if(b == 0){
        return 0;
    }
    return int((a + b - 1) / b);
}
int solution(vector<int> &A, vector<int> &B) {
    // write your code in C++14 (g++ 6.2.0)

    int a_sum = 0;
    int b_sum = 0;
    int ret = 0;

    unordered_map<int, int> a_table;
    unordered_map<int, int> b_table;

    for(auto num : A){
        a_sum += num;
        a_table[num]++;
    }

    for(auto num : B){
        b_sum += num;
        b_table[num]++;
    }

    if(b_sum > a_sum){
        return solution(B, A);
    }

    // a_sum >= b
    int diff = a_sum - b_sum;
    for(int num = 6; num >= 2; --num){
        // //taking off num from a.
        // cout << "dealing with num" << num << endl;

        if(diff > a_table[num] * (num - 1)){
            ret += a_table[num];
            // cout << a_table[num] << " " << diff << " a table removal partial" << endl;
            diff -= a_table[num] * (num - 1);
        }
        else{
            // cout << ceil_div(diff, a_table[num]) << " " << diff << " a full table removal" << endl;
            ret += ceil_div(diff, num);
            return ret;
        }

        //increasing number from b.
        int rev_num = 6 - num + 1;
        if(diff > b_table[rev_num] * (num - 1)){
            ret += b_table[rev_num];
            // cout << b_table[num] << " " << diff << " b table removal partial" << endl;
            diff -= b_table[rev_num] * (num - 1);
        }
        else{
            // cout << "b_diff" << diff << endl;
            // cout << rev_num << " rev_num" << endl;
            // cout << ceil_div(diff, rev_num) << " " << diff << " b full table removal" << endl;
            ret += ceil_div(diff, rev_num);
            return ret;
        }
    }

    return -1;
}



