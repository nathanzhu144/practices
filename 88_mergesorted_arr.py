# Wednesday June 24th, 2019 10:08 am Overlooking Hudson River
# Leetcode 88 | easy | ehh, easy if you see the right insight
#  
# If arr1 has extra space, you can do it in-place with O(N) time by inserting into back.


# This is same format as adding two strings or adding two
# linked lists.
# This is a standard way of doing it.
def merge_two_sorted_arr_extra_space(arr1, arr2):
    arr1i, arr2i = 0, 0
    ret = []
    while arr1i < len(arr1) or arr2i < len(arr2):
        arr1val, arr2val = float('inf'), float('inf')
        if arr1i < len(arr1): arr1val = arr1[arr1i]
        if arr2i < len(arr2): arr2val = arr2[arr2i]

        if arr1val < arr2val: 
            ret.append(arr1val)
            arr1i += 1
        else: 
            ret.append(arr2val)
            arr2i += 1

    return ret


# Intuition:
# We do a merge from the back.
# If we have 2 sorted arrays, it is clear that the biggest element in 
# the merged array is the maximum of the 2 back elements... and so on.
#
# Example
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6]
#
# nums1 = [1,2,3,0,0,0]
#                    ^ max(3, 6) is 6, which must be here

def merges_two_sorted_arr_no_extra_space(arr1, m, arr2, n):
    # We calculate index of back element.
    i = m + n - 1   
    arr1i, arr2i = m - 1, n - 1

    while arr1i >= 0 or arr2i >= 0:
        arr1val, arr2val = float('-inf'), float('-inf')
        if arr1i >= 0: arr1val = arr1[arr1i]
        if arr2i >= 0: arr2val = arr2[arr2i]

        if arr1val > arr2val:
            arr1[i] = arr1val
            i -= 1
            arr1i -= 1
        else:
            arr1[i] = arr2val
            i -= 1
            arr2i -= 1

    return arr1

if __name__ == "__main__":
    print(merge_two_sorted_arr_extra_space([1, 5], [1, 2, 3, 5, 6]))