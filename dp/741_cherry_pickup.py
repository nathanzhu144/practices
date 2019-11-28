# Nathan Zhu 7:10 am Duderstadt library Nov 21st, 2019
# Leetcode 741 | hard | yeah pretty hard
# Category: DP / Backtracking
# Runtime N ^ 3, where N is a side of board, space is N ^ 3 as well.
#

# There are several intuitions:
# 
# Finding the maximum number of cherries on first leg, then
# maximum number of cherries on way back does NOT always give the global
# optimal cherry-pick.  Greed doesn't work.
#
# Ex. [1, 1, 0, 0, 1]
#     [0  0  0  0  0]
#     [0  0  0  0  0]
#     [1  0  0  1  1]
# Greedy will pick 4 on first round & 1 on second round, leaving 1 on table.
# However, it is obvious it should be possible to pick all the cherries
#
# 
# So, what does work?
# Note: A forward trip is "the same" as a backward trip.  You can get exactly same number of cherries 
# going down and right from top left as you can up and left from bottom right.  (assuming board same)
#
# So, say we keep track of both people at the same time and backtracked with both of them.
# Then it becomes a relatively straightforward problem with 4^(N ^ 2) runtime.
# 
# But, making it a DP problem with n ^ 4 is simple.  We just memoize with (r1, c1, r2, c2)
#
# Making it n^3 requires an additional insight.  
# r1 + c1 = r2 + c2, so r1 + c1 - r2 = c2.
# Therefore, we only need to memoize (r1, c1, r2), as c2 will always be dependent on those 3.


def cherry_pickup(grid):
    def helper(grid, N, r1, c1, r2, c2, mem):
        # This is smart
        key = (r1, c1, r2)
        if key in mem: return mem[key]

        # out of bounds or hit thorn
        # we don't check less than 0 because we never subtract
        if r1 >= N or c1 >= N or r2 >= N or c2 >= N or grid[r1][c1] == -1 or grid[r2][c2] == -1: 
            return float("-inf")

        # TRICKY #
        # This was hard to convince myself of, but the idea is that assuming r1 c1 hits the bottom right square.
        # r2 c2 has to be about to hit the bottom right square, assuming both are on the board, and there are NO thorns.
        #
        # If there are thorns, may *NOT* be true as well, but the cherries picked is -inf, discarding that path.
        # Therefore, it is always safe to just end the recursion taking the bottom right square once.
        if (r1 == N - 1 and c1 == N - 1) or (r2 == N - 1 and c2 == N - 1):
            return grid[N - 1][N - 1]

        num_cherries = 0
        # TRICY, BUT ONLY A LITTLE #
        # If we are on same square, don't double-pick the cherry.
        if r1 == r2 and c1 == c2: num_cherries += grid[r1][c1]
        else: num_cherries += grid[r1][c1] + grid[r2][c2]

        # with 2 ppl, 4 different ways to move.
        num_cherries += max(helper(grid, N, r1 + 1, c1, r2 + 1, c2, mem),
                            helper(grid, N, r1 + 1, c1, r2, c2 + 1, mem),
                            helper(grid, N, r1, c1 + 1, r2 + 1, c2, mem),
                            helper(grid, N, r1, c1 + 1, r2, c2 + 1, mem))
        mem[key] = num_cherries
        return mem[key]

    # We need max(0, ...) because helper returns -inf if there's no way through
    return max(0, helper(grid, len(grid[0]), 0, 0, 0, 0, dict()))



