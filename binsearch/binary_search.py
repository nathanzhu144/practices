#

##################################
##     Classic binary search    ##
##################################
#  1. If target is not in array, after the binary
#     search low > high.  One iteration before we exit, 
#     it is true that low == high
#
#  2. med is the floor of (low + high) / 2
#
#  3. If we find the target, we return immediately
# 
#  4. If we do not find a target, we exclude it 
#     by making lower bound 1 above it or upper
#     bound 1 below it.  Therefore arr[med] is excluded
#     in every iteraton
def bin_search(arr, target): 
    low, high = 0, len(arr) - 1

    while low <= high:
        med = (low + high) / 2

        if arr[med] == target:
            return med

        if arr[med] > target:
            high = med - 1
        else:
            low = med + 1

##################################
#    Searching for lower bound   #
############################3######
# 
#  If my target is smaller or equal to middle term, the scope
#  should be narrowed down to the left, but INCLUDING the middle term, 
#  Else, if my target is larger than the middle item, we should narrow
#  down the scope to the right
#
#  Note, 
#    When should I end the loop?
#    We end iteration when min == max, so both min and max point to same item
#
#    Why can't high = med - 1?
#    It is possible that med is leftmost item, this would incorrectly takke
#    it out of the search
#
#    What if the target doesn't exist in the array?
#    We return when low == high.  It isn't guaranteed that the returned 
#    positon actually has the target, we need to check if it has the target.
def find_leftmost(arr, target):
    low, high = 0, len(arr) - 1

    while low < high:
        med = (low + high) / 2

        if arr[med] >= target:
            high = med
        else:
            low = med + 1

    if arr[low] == target:
        return low
    else:
        return -1


def 