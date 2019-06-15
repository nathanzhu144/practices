#  Leetcode 785
#  Nathan Zhu June 13th, 2019, Thursday 7:40 pm, 55th John Street, New York
#
#  We are given an array A of positive integers, and two positive integers 
#  L and R (L <= R).  Return the number of (contiguous, non-empty) subarrays 
#  such that the value of the maximum array element in that subarray is at
#  least L and at most R
# 
#  My first approach was correct, but didn't pass long test case (TLE)
# 

#  Note that brute force is N^3.  For each of the N^2 substrings of a string,
#  we iterate through the string to find the maximum.
#
#  However, one observation is that if we know the indices i and j, we can
#  get the max of a string in O(1) time, with a hash table.  Note that i and j
#  are INCLUSIVE.  So, if str = "dog", (1, 1) is "o" and (1,2) is "og"
#
#  Max str(i, j) = MAX(arr[i], hash_table[str(i + 1, j - 1)], arr[j])
#
#  If a max integer in (i,j) <= R, it is a potential soln
#  If a max integer in (i,j) is L <= (i,j) <= R it is a soln
#
#  NOTE: I don't store (i,j) as a potential soln if (i,j) > R 
#        because no string with that substring can ever be a soln
#
#  This is a correct N^2 from N^3 approach.
#  
def numSubarrayBoundedMax(arr, L, R):
    """
    :type A: List[int]
    :type L: int
    :type R: int
    :rtype: int
    """
    potentials = dict()   # pairs exist in here if they are < R, maps indices -> total
    returned = dict()
    for i in range(len(arr)):
        if arr[i] <= R:
            potentials[(i, i)] = arr[i]
            if arr[i] >= L:
                returned[(i, i)] = arr[i]

    for i in range(len(arr) - 1):
        if max(arr[i], arr[i + 1]) <= R:
            potentials[(i, i + 1)] = max(arr[i], arr[i + 1])
            if max(arr[i], arr[i + 1]) >= L:
                returned[(i, i + 1)] = max(arr[i], arr[i + 1])

    for j in range(2, len(arr)):
        for i in range(j - 1):
            if (i + 1, j - 1) in potentials:
                max_between_i_j = max(arr[i], potentials[(i + 1, j - 1)], arr[j])
                if max_between_i_j <= R:
                    potentials[(i, j)] = max_between_i_j
                    if max_between_i_j >= L:
                        returned[(i, j)] = max_between_i_j
    
    return len(returned)



if __name__ == "__main__":
    print(numSubarrayBoundedMax([2,9,2,5,6], 2, 8))