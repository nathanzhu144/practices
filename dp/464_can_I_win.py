# Nathan Zhu Saturday July 13th, 2019 Amex Building 36th floor 3:31 pm
# Leetcode 464 | medium | I think medium
# Category: DP / Backtracking / Minimax
#  
# This is a variant of a classic minimax algorithm.  
# 
# In the "100 game," two players take turns adding, to a running total, 
# any integer from 1..10. The player who first causes the running tota
#  to reach or exceed 100 wins.
# 
# WPlayers CANNOT re-use numbers.
# For example, two players might take turns drawing from a common pool of numbers of 1..15 
# without replacement until they reach a total >= 100.
    
# 1, 2, 3, ... 15
# Choose 1.    num_left == 100


def can_I_win(max_choosable_integer, total):
    numbers = [n for n in range(1, max_choosable_integer + 1)]  
    if sum(numbers) < total: return False                    # If total of numbers cannot get to total, obviously 
                                                             # we cannot win.     

    def helper(not_used_numbers, total, mem):
        # NOTE: We don't need to memoize not_used_numbers, with remaining total cause numbers that are not used
        #       implicitly store remaining total.  You can't get a different total with same remaining numbers.
        # If we have seen this scenario play out, we know how it turns out.
        key = tuple(not_used_numbers)
        if key in mem: return mem[key]

        # We can win here, take it!!
        if max(not_used_numbers) >= total: return True

        # we haven't won yet.. it's the next player's turn.
        # importantly, if we win just one permutation then
        # we're still on our way to being able to 'force their hand'
        for i in range(len(not_used_numbers)):
            # If we can ever put our opponent in a position where they will definitely lose
            # we return True
            if not helper(not_used_numbers[:i] + not_used_numbers[i + 1:], total - not_used_numbers[i], mem):
                mem[key] = True
                return True
            # if we modified not_used_numbers, we would backtrack here, but we make a copy of not_used_numbers
        mem[key] = False
        return False

    return helper(numbers, total, dict())
    
if __name__ == "__main__":
    print(can_I_win(10, 11))
