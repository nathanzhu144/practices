# Q2 here
# 
# https://leetcode.com/discuss/interview-question/1261316/amazon-oa-sde-1-new-grad-2021-batch-india
#
# 1. I split the orders into two buckets, primes and nonprimes.  All nonprimes are stored in the order that they can in the input array.  For the primes, since we want to sort by the keywords, and then tiebreak by ID; I use python's sort function for primes with a tuple ( keywords, ID), so it first sorts by keywords in ascending order and then tiebreaks by ID.  Finally, after having sorted the primes, I re-combine both arrays together.  The primes go first, and the non-primes go last.  All of them are in correct order now.

# 2. Runtime depends on input. N represents length of our array.

# Worst case: Assuming we use a worst case NlogN sort like mergesort, our worst case here is NlogN, as we are sorting primes, and primes can be the whole input.  all other operations are O(N), and O(NlogN) dominates for a final answer of O(NlogN)

# Best case: is all of the orders are nonprimes, in which case we sort 0 elements.  However, we have O(N) other operations, as we end up iterating through whole array.  So, O(N)

# General time analysis: O(NlogN)
import functools
def sortOrders(orderList):
    prime, nonprime = [], []
    
    for item in orderList:
        arr = item.split()
        if arr[1].isalpha():
            prime.append((tuple(arr[1:]), arr[0], item))
        else:
            nonprime.append(item)
    prime.sort()
    
    return [item[2] for item in prime] + nonprime