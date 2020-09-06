    int dp[102][102];
    
    int solve(vector<int> &cuts, int low, int high) {
        if(low+1==high) return 0;
        else if(dp[low][high]!=-1)
            return dp[low][high];
        
        else {
            int ans = INT_MAX;
            for(int i=low+1; i<high; i++) {
                int curr = cuts[high]-cuts[low] + solve(cuts, low, i) + solve(cuts, i, high);
                ans = min(ans, curr);
            }
            return dp[low][high] = ans;
        }
    }
    
    int minCost(int n, vector<int>& cuts) {
        cuts.push_back(0);
        cuts.push_back(n);
        memset(dp, -1, sizeof(dp));
        sort(cuts.begin(), cuts.end());
        return solve(cuts, 0, cuts.size()-1);
    }