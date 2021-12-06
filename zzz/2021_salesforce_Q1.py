import collections

# Really boring problem:
# Find number of subarrays in an integer array of length k that are strictly increasing.
# Ex.
# [1, 3, 4, 2, 3] k = 2
#  -  - 
#     -  -
#           -  -
# 3 subarrays of length 2
def countHighlyProfitableMonths(arr, k):
    N, i, ret = len(arr), 0, 0

    while i < N:
        ct = 0
        first = True
        while i < N and (first or arr[i] > arr[i - 1]):
            first = False
            ct += 1
            i += 1
        ret += max(0, (ct - k + 1))
    return ret
            
if __name__ == "__main__":
    print(countHighlyProfitableMonths([1, 2, 3, 3, 4, 5], 3))