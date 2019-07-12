#
#  The idea behind egg drop is that we have a building with N floors and we have k eggs.  All eggs
#  are exactly the same, and all drops are the same.  There exists a floor "F" s.t. 0 <= F <= N where egg will
#  break if any egg dropped above F will break, but no egg will drop at F or below.
#
#  What's the fewest number of drops we need to know with certainty which floor F is, where N is the number
#  of floors and k is the number of eggs. 
#
#
#  Let M(N, K) be this minimum number.
# 
#  Let's first talk about a base case.
#
#  Base case:
#
#  M(N, 1) = N     => If we have 1 egg, and N floors, only way to know is to start from floor 0 and go up till N
#  
#  M(0, K) = 0     => If there are 0 floors, we trivially know that floor 0 must be the floor, as 0 <= 0 <= 0.
#  
#  M(1, K) = 1     => If there is 1 floor, no matter how many eggs we have, we have to see if that one floor is F or not
#
#  NOTE: SO, I was confused, as to why M(1, K) is 1. This is because, if you drop an egg on the 1th floor, and it don't break you know that
#                                                    it is definitely the first floor.  If it does break, you know it is the 0th floor.
# 
#         
#
#        The leetcode example talks about 2 floors 1 egg, and their answer for F(2, 1) = 2, as if you drop an egg on, "Drop the egg from 
#        floor 1.  If it breaks, we know with certainty that F = 0. Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
#        If it didn't break, then we know with certainty F = 2,  Hence, we needed 2 moves in the worst case to know what F is with certainty."
#
#
#  
#  A quick example is good for understanding the intuition behind this problem.
#
#  Let's say we have 2 eggs and N floors.
#
#  The way to figure this out is to do:
#      The answer to this is simply min(M(1, 2), M(2, 2), M(3, 2), ... M(N - 1, 2), M(N, 2)).  There exists a floor where
#      we can minimize the worst case, and by iterating through the worst cases from starting from every floor, we can 
#      figure out the best worst case.  Then, we want to go with that.
#
#     Note that the best worst case at every floor is maximum((M(floor - 1, K - 1), M(N - floor, K))
#        M(floor - 1, K - 1) is our egg breaks, so problem is simply checking the floor - 1 floors below with 1 fewer egg
#        M(N - floor, K) is our egg doesn't break, so we have to check the N - floors above us, with same number of eggs
#      
#     
#  The runtime complexity is O(kN^2).

def egg_drop(num_floors, num_eggs):
    def helper(num_floors,  num_eggs, finished):
        key = (num_floors, num_eggs)
        if key in finished:
            return finished[key]

        if num_floors == 1 or num_eggs == 1:
            return num_floors

        minimum = float('inf')
        for floor in range(1, num_floors + 1):  # range starts at 1 to aboid going to floor -1
            temp = max(helper(floor - 1, num_eggs - 1, finished), helper(num_floors - floor, num_eggs, finished)) + 1
            if temp < minimum:
                minimum = temp

        finished[key] = minimum
        return finished[key]

    return helper(num_floors, num_eggs, {})

    




if __name__ == "__main__":
    print(egg_drop(2, 6))