
    int maxSum(vector<int>& A, vector<int>& B) {
        int i = 0, j = 0, n = A.size(), m = B.size();
        long a = 0, b = 0, mod = 1e9 + 7;
        while (i < n || j < m) {
            if (i < n && (j == m || A[i] < B[j])) {
                a += A[i++];
            } else if (j < m && (i == n || A[i] > B[j])) {
                b += B[j++];
            } else {
                a = b = max(a, b) + A[i];
                i++, j++;
            }
        }
        return max(a, b) % mod;
    }


    You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:

Choose array nums1 or nums2 to traverse (from index-0).
Traverse the current array from left to right.
If you are reading any value that is present in nums1 and nums2 you are allowed to change
 your path to the other array. (Only one repeated value is considered in the valid path).
Score is defined as the sum of uniques values in a valid path.

Return the maximum scor