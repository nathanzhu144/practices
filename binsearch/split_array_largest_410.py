# Nathan Zhu, 6:29 pm, Chicago, Saturday June 29th, 2019
# Leetcode 410 | leetcode hard | I can see why it isn't easy, but with insight it is combining 
#                                ideas of two harder easys.  I coded it right on first try,
#                                no syntax errors, even, except num_splits being one off due to a definition misunderst
#
# https://leetcode.com/problems/split-array-largest-sum/discuss/89819/C%2B%2B-Fast-Very-clear-explanation-Clean-Code-Solution-with-Greedy-Algorithm-and-Binary-Search
# That links explains it well.
#
# NOTE: Leetcode means NUM_SPLITS as num segments you can split into.  I mean
#       num_splits as num times you can split an array.  The idea is the same.


# Given num_splits and arr, we can agree that there exists a max_sum_in_subarry number "k"
# s.t. we can split under those conditions for this max_sum_in_subarr == "k", but not for
# a value of max_sum_in_subarray "k - 1"
#
# So, this decomposes into finding the minimum value where we can use num_splits to split the whole array.
def find_minimum_sum(arr, num_splits):

    # THIS GREEDY APPROACH ONLY WORKS WHEN ALL NUMS IN ARRAY ARE POSITIVE.
    # Given num_splits and a max_sum_in_subarr, is it possible to successfully split
    # the whole array.  If possible, return true.
    #
    # This is clearly very solvable with a greedy algorithm.  We iterate through the
    # array, and keep trying to add each element to a cumulative sum until an element
    # puts it over the sum.  Then, we cut before that element.  
    # 
    # 1. If any element arr[i] > max_sum_in_subarr, it is impossible.  
    # 2. If num_splits ever gets to 0 when we need another split, it is impossible
    def split_array_largest(arr, num_splits, max_sum_in_subarr):
        cumulative = 0

        for num in arr:
            if num > max_sum_in_subarr: return False  # condition 1
            if cumulative + num > max_sum_in_subarr:
                if num_splits == 0: return False      # condition 2
                # we successfully do another split
                else:
                    num_splits -= 1
                    cumulative = num
            else:
                cumulative += num

        return True

    # This is a very standard binary search code where we have a function F(x),
    # and we have an array where the values of F(x) are like
    # [FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE]
    # Find the first true.

    left, right = max(arr), sum(arr)
    returned = -1

    while left <= right:
        med = (right - left) // 2 + left

        # this is a standard lower_bound finding method, our F(x)
        # is split_array_largest
        if split_array_largest(arr, num_splits, med):
            returned = med
            right = med - 1
        else:
            left = med + 1
    return returned

if __name__ == "__main__":
    print(find_minimum_sum([7,2,5,10,8], 2))