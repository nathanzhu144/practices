#include <vector>
#include <bitset>

using namespace std;

int lastStoneWeightII(vector<int> A) {
    bitset<1501> dp = {1};
    int sumA = 0;
    for (int a : A) {
        sumA += a;
        for (int i = min(1500, sumA); i >= a; --i)
            dp[i] = dp[i] + dp[i - a];
    }
    for (int i = sumA / 2; i > 0; --i)
        if (dp[i]) return sumA - i - i;
    return 0;
}

int main(){
    lastStoneWeightII({6, 4, 8});
}