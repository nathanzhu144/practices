# Nathan Zhu 12:24 pm, Thursday June 27th.  Lunch break, Amex Tower, 36th floor
# Leetcode 153 | medium | WTF HARD
# Jesus, binary search questions are literally harder than DP problems by so much - they're soooo annoying.  
# Legitimately binary search is the hardest
#
# Approaching this problem actually isn't that bad...
# 
# Ex. [7, 8, 9, 10, 15, 20, 2, 3]
#      L                       R
#
#     Suppose that arr[mid] > arr[R].  Then, you are on the left side of the array, and the target minimum is on the right side of the array.  You need to get to the left side of the array
#     Suppose that arr[mid] < arr[R].  Then, you are right side of the array, an the target minimum is on the right side of the array.  You just need to check if you have found the smallest.
#
#  However, you can use the same logic for comparing mid against left.  However, that approach is basically impossible to do bug-free under pressure.
#  
#  So, since mid = (left + right) // 2, it must be true that right != mid if left < right.  
#  This is true because we are taking the floor of the sum of the (left + right).  
#  
#  Therefore, we never have to worry about a case where arr[right] == arr[mid], BUT if we compare
#  against mid, there is a case where arr[left] == arr[mid].  
#
#  Not taking into account this equality leads to test cases like [2, 1] going into an infinite loop, 
#  As left index == 0 and mid index == 0, leading to no movement.
#
#  A solution that comes to mind is to replace
#        arr[mid] > arr[left]: left = mid + 1 
#               with 
#        arr[mid] >= arr[left]: left = mid + 1
#
#  The problem to this is subtle, and I'm not entirely sure what the mechanism of this is, as this passed 100+ test cases before
#  failing, but on this test case,
#.
        # [3, 4, 5, 1, 2]
        #  L     M     R
        # [3, 4, 5, 1, 2]
        #           L  R
        #           M
        # [3, 4, 5, 1, 2]
        #              L == R  (we returned 2 instead of 1 because arr[mid] >= arr[left]
        #                                                  and mid == left at this position
#  this approach has failures.
#
#  
#  We need another patch.
#  That patch is "realizing" that if arr[left] < arr[right], we have found the "correct" element, and returning arr[left]
#
#  I think it is easier to go with the easier soln.
#  


# THE HARD WAY
# So, if you compare middle element to the left, you have a doable, but harder way
def find_min_hard(arr):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(arr) - 1
    
    while left != right:
        # Note that if arr[left] < arr[right], we have found
        # the smallest index
        #
        # w/o this line, we fail test case
        # [3, 4, 5, 1, 2]
        #  L     M     R
        # [3, 4, 5, 1, 2]
        #           L  R
        #           M
        # [3, 4, 5, 1, 2]
        #              L == R  (we returned 2 instead of 1 because arr[mid] >= arr[left]
        #                                                  and mid == left at this position
        if arr[left] < arr[right]: return arr[left]
        
        mid = (left + right) // 2
        
        # If mid >= left, mid CANNOT be right index, so we can do left = mid + 1
        # Potential bug: If we replace arr[mid] >= arr[left] with arr[mid] > arr[left]
        #                we fail on testcase like 
        #  [2, 1]
        #   L R
        #   M
        #   ...
        #   infinite loop, as since mid == left, arr[mid] == arr[left]
        # 
        if arr[mid] >= arr[left]:
            left = mid + 1
        elif arr[mid] < arr[left]:
            right = mid
            
    return arr[left]

# THIS METHOD IS SUBSTANTIALLY EASIER THAN COMPARING TO TOP METHOD.  ONLY DIFFERENCE
# IS WE COMPARE MIDDLE TO RIGHT, INSTEAD OF MIDDLE TO LEFT, LOL.
# NOTE B:
# Because mid is floor of (left + right) / 2, if left < right, as is true in the while loop,
# and we are assigning mid to floor, everytime we do an assignment right = mid, right decreases
#
# In the other case, left increasing by 1.  
#
# Therefore, we never go into an infinite loop.
def find_min_easy(arr):
    left, right = 0, len(arr) - 1
    while left != right:
        #if arr[left] < arr[right]: return arr[left]

        mid = (left + right) // 2

        # Note that we do not need a <=
        # THIS IS BECAUSE MID INDEX IS STRICTLY LESS THAN RIGHT INDEX (see Note B)
        # Also, we know that all elements are distinct, so therefore arr[mid] != arr[right]
        if arr[mid] < arr[right]:
            right = mid
        elif arr[mid] > arr[right]:
            left = mid + 1
    
    return arr[left]

if __name__ == "__main__":

    print(find_min_hard([2, 1]))
    #print(find_min_easy([1, 2]))
    #print(find_min_easy([2, 1]))
    #print(find_min_easy([3, 4, 5, 1, 2]))