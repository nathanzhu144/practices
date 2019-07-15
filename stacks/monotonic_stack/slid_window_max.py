#  Nathan Zhu Saturday 4:23 pm, Leetcode Hard 239
#  This is a monotonic queue question.
#
#  Let's keep a queue,
#
#  We see the first 
#  Sliding window maximum
#  arr = [1,3,-1,-3,5,3,6,7], k = 3
# 
#  This is a variation of the next greater element problem, where we 
#  must use a monotonic stack.  However, there is a special restriction where
#  we have to use a monotic queue.
#
#  [1]
#  [3]
#  [3, -1]
#  [3, -1, -3]
#  [5]
#  [5, 3]
#  [6]
#  [7]
#
#  We have a deque of array indices. The array indices at the top are most recent, and array indices
#  are the least recent.  Array indices point to elements in increasing order as you go from top to bottom.
#  
#  Suppose we have the deque[3, 1, 2] pointing to the array [5, 2, -1].  We get a -2.  Even though -2 is smaller 
#  than anything in our original array, it farther right than anything in our array and can potentially be a
#  new smaller element.
#
#  Suppose we get a 1 instead.  1 is greater than -1, and 1 is farther right than -1.  There is no chance -1 can
#  ever be the local maximum of a subarray
#
#  If we get a 7.  7 is greater than any other element we have in our deque, and is farther right. 
#  If this is included, no other element in our current deque can ever be maximum of subarray
#
#  Also note that since we are limited to a window of size K, when we realize we have elements that come
#  before the left side of the window, we must prune them.
#  

import collections

def slid_window_max(arr, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    returned = list()
    mono_dec_q = collections.deque(list())
    left = 0

    for right in range(0, len(arr)):
        # Any elements on stack smaller than new right element are removed
        # We can go top -> bottom cause we know ordering of deque is smallest -> biggest
        while mono_dec_q and arr[right] > arr[mono_dec_q[-1]]:
            mono_dec_q.pop()

        # Any elements on deque out of the sliding window must be removed
        # We can go bottom -> top cause we know ordering of the deque is earliest -> newest
        while mono_dec_q and mono_dec_q[0] <= right - k:
            mono_dec_q.popleft()

        # add curr element to deque
        mono_dec_q.append(right)

        # we only start appening when left becomes at least size k
        if left >= k - 1:
            returned.append(arr[mono_dec_q[0]])
        left += 1
    return returned


if __name__ == "__main__":
    print(slid_window_max([1,3,-1,-3,5,3,6,7], 3))