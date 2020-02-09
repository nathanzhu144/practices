# Nathan Zhu, Monday January 20th, 2020, Foundry Lofts, just talked to george about tarjan's
# Leetcode 1027 | medium | medium
# Similar idea to LiS.
#
# We memoize on [(idx, difference)]
# Pretty straightforward, surprised didn't come easier.

def longestArithSeqLength(A):
    c = collections.defaultdict(lambda: 1)
    N = len(A)
    for i in range(N):
        for j in range(i + 1, N):
            diff = A[j] - A[i]
            c[j, diff] = c[i, diff] + 1
            
    return max(c.values())
if __name__ == "__main__":
    print(longestArithSeqLength([3, 6, 9, 12]))