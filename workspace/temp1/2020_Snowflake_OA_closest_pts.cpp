/* Nathan Zhu Snowflake OA, for Fall Co-op June 11th, 2020
*  Leetcode n/a | n/a | hard for nlogn soln
*
*  Easy, find closest pair of points in 2d.  There's a great nlogn algorithm, which requires 
*  some smart sorting, divide and conquer, and a proof with a constant number of points.
*
*  Did not implement it here, this timed out on some test cases
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


long distance(int x1, int y1, int x2, int y2){
    return pow(x1 - x2, 2) + pow(y1 - y2, 2);
}

// Complete the closestSquaredDistance function below.
long closestSquaredDistance(vector<int> x, vector<int> y) {
    int N(x.size());
    long ret = numeric_limits<long>::max();
    vector<pair<int, int>> pts;

    for(int i = 0; i < N; ++i){
        pts.emplace_back(x[i], y[i]);
    }

    for(int i = 0; i < N; ++i){
        for(int j = i + 1; j < N; ++j){
            auto [x1, y1] = pts[i];
            auto [x2, y2] = pts[j];
            ret = min(ret, distance(x1, y1, x2, y2));
        }
    }

    return ret;

}
int main()