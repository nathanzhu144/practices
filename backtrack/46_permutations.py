#  Nathan Zhu, Tuesday July 2nd, 2019 10:15 am, Brooklyn New York in Lyft ride
#   
#  Idea here is very simple.
# We have a list, [1, 2, 3]
# we grab any of the elements
#    and recur for the rest, like
#
#    1 [2, 3]
#        1 2 [3]
#           1 2 3
#        1 3 [2]
#           1 3 2
#    2 [1, 3]
#        2 1 [3]
#           2 1 3
#        2 3 [1]
#           2 3 1
#    3 [1, 2]
#        3 1 [2]
#           3 1 2 
#        3 2 [1]
#           3 2 1
def helper(arr, curr_path, returned):
    if not arr: returned.append(curr_path[:])
        
    # pick 1, add it to path, and recur for everything else in the array
    for i in range(len(arr)):
        helper(arr[:i] + arr[i + 1:], curr_path + [arr[i]], returned)
ret = list()
helper(arr, list(), ret)
return ret
