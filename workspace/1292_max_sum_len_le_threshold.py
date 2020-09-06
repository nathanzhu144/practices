

# def maxSideLength(A, threshold):
#     s = 0
#     def a(i, j):
#         return A[i][j] if i >= 0 <= j else 0
#     for i in range(len(A)):
#         for j in range(len(A[0])):
#             A[i][j] += a(i-1, j) + a(i, j-1) - a(i-1, j-1)
#             if i >= s <= j:
#                 tot = a(i, j) - a(i-s-1, j) - a(i, j-s-1) + a(i-s-1, j-s-1)(
#                 if tot <= threshold:
#                     s += 1
#     return s

# int maxSideLength(vector<vector<int>> A, int threshold) {
#     auto size = A;
#     int res = 0;
#     for (int i = 0; i < A.size(); i++) {
#         for (int j = 0, a = 0; j < A[0].size(); j++) {
#             #define A(i, j) (i < 0 || j < 0 ? 0 : A[i][j])
#             A[i][j] = (a += A[i][j]) + A(i-1, j);
#             int& s = size[i][j] = (i && j) ? size[i-1][j-1] + 1 : 1;
#             while (A(i, j) - A(i-s, j) - A(i, j-s) + A(i-s, j-s) > threshold)
#                 s--;
#             res = max(res, s);
#         }
#     }
#     return res;
# }


# def maxSideLength(A, threshold):
#     if not A or not A[0]: return 0
#     R, C = len(A), len(A[0])
#     res = 0

#     size = [[A[r][c] for c in range(C)] for r in range(R)]

#     def a(i, j):
#         return A[i][j] if i >= 0 <= j else 0

#     for r in range(R):
#         b = 0
#         for c in range(C):
#             b += A[r][c]
#             A[r][c] = b + a(r - 1, c)
#             size[r][c] = size[r - 1][c - 1] + 1 if (r > 0 and c > 0) else 1
#             s = size[r][c]
#             while a(r, c) - a(r - s, c) - a(r, c - s) + a(r - s, c - s) > threshold:
#                 s -= 1
#             res = max(res, s)

#     return res

import collections
def maxSideLength(mat, threshold):
    sqsum = lambda x1, y1, x2, y2: p[x2 + 1][y2 + 1] - p[x1][y2 + 1] - p[x2 + 1][y1] + p[x1][y1]
    m, n = len(mat), len(mat[0])
    p = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            p[i + 1][j + 1] = mat[i][j] + p[i][j + 1] + p[i + 1][j] - p[i][j]
    diagonals = collections.defaultdict(list)
    for i in range(m):
        for j in range(n):
            diagonals[i - j].append((i, j))
    res = 0
    for diag in diagonals.values():
        lo = curr = 0
        for hi in range(len(diag)):
            curr = sqsum(*diag[lo], *diag[hi])
            while curr > threshold and lo < hi:
                lo += 1
                curr = sqsum(*diag[lo], *diag[hi])
            if curr <= threshold:
                res = max(res, hi - lo + 1)
    return res

            
if __name__ == "__main__":
    print(maxSideLength([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6))