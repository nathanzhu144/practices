Given a string s. An awesome substring is a non-empty substring of s such that we
 can make any number of swaps in order to make it palindrome.

Return the length of the maximum length awesome substring of s.


int longestAwesome(string s) {
    vector<int> dp(1024, s.size());
    int res = 0, mask = 0;
    dp[0] = -1;
    for (auto i = 0; i < s.size(); ++i) {
        mask ^= 1 << (s[i] - '0');
        res = max(res, i - dp[mask]);
        for (auto j = 0; j <= 9; ++j)
            res = max(res, i - dp[mask ^ (1 << j)]);
        dp[mask] = min(dp[mask], i);
    }
    return res;
}