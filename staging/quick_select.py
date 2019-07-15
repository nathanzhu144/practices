class Solution:
# @param {integer[]} nums
# @param {integer} k
# @return {integer}
def findKthLargest(self, nums, k):
    # QuickSelect idea: AC in 52 ms
    # ---------------------------
    #
    pivot = nums[0]
    left  = [l for l in nums if l < pivot]
    equal = [e for e in nums if e == pivot]
    right = [r for r in nums if r > pivot]

    if k <= len(right):
        return self.findKthLargest(right, k)
    elif (k - len(right)) <= len(equal):
        return equal[0]
    else:
        return self.findKthLargest(left, k - len(right) - len(equal))



    // Returns the k-th smallest element of list within left..right inclusive
  // (i.e. left <= k <= right).
  // The search space within the array is changing for each round - but the list
  // is still the same size. Thus, k does not need to be updated with each round.
  function select(list, left, right, k)
     if left = right        // If the list contains only one element,
         return list[left]  // return that element
     pivotIndex  := ...     // select a pivotIndex between left and right,
                            // e.g., left + floor(rand() % (right - left + 1))
     pivotIndex  := partition(list, left, right, pivotIndex)
     // The pivot is in its final sorted position
     if k = pivotIndex
         return list[k]
     else if k < pivotIndex
         return select(list, left, pivotIndex - 1, k)
     else
         return select(list, pivotIndex + 1, right, k)