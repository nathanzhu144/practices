# T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
# T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i]) = max(T[i-1][k][1], T[i-1][k][0] - prices[i])'


# T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
# T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])