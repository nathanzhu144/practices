# Given an array nums of n integers, are there elements a, b, c 
# in nums such that a + b + c = 0? Find all unique triplets in the
#  array which gives the sum of zero.

# -4, -3, -2, -1 ... 1  2  3 
# Runtime is O(N^2)

#  Check A prevents this situation.
# -3, -3, -3, -2,   6,
#  ^Fir^ sec        ^ Third
# -3, -3, -3, -2,   6,
#      ^Fir^ sec    ^ Third
def three_sum(arr):
    arr = sorted(arr)

    ret = []
    # -3, -3, -3, -2,  2, 3 
    #                  ^ Third
    # We want first to stop at n - 2, otherwise we don't have room for second and third
    for first in range(len(arr) - 2):
        if first != 0 and arr[first] == arr[first - 1]: continue     # Check A, makes sure first is never duplicate
        second, third = first + 1, len(arr) - 1                     # we init second to first + 1

        while second < third:
            if arr[first] + arr[second] + arr[third] == 0: 
                ret.append([arr[first],arr[second], arr[third]])
                # Check B: Next 4 lines.  Prevents double counting of other two elements.
                while second < third and arr[second] == arr[second + 1]: second += 1
                while second < third and arr[third] == arr[third - 1]: third -= 1
                second -= 1
                third -= 1
            elif arr[first] + arr[second] + arr[third] < 0: second += 1
            elif arr[first] + arr[second] + arr[third] > 0: third -= 1
        
    return ret

            

if __name__ == "__main__":
    print(three_sum([-1,0,1,2,-1,-4]))
