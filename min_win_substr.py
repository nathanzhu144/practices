#  Nathan Zhu 1:29 pm Saturday 1:29 pm, Amex Tower, Executive suite, 36th floor overlooking Hudson river
#  This is the minimum window substring problem.
#
#  Classic sliding window problem.
#  Back to back SWE gives amazing explanation
#  https://www.youtube.com/watch?v=eS6PZLjoaq8
#
#  Leetcode 76

def minWindow(self, string, target):
    """
    :type s: str
    :type t: str
    :rtype: str
        """
    chars_table = dict()  # if a char in target has value > 0, that char is in target and we need more of that char
                            # if a char in target has value == 0 and that char is in target, we have enough of that char
                            # if a char in target has value < 0 and that char is in target, we have more than enough of that char
                            # if a char in target has value <= 0 and that char not in target, it is not relevant info
    
    # only necessary characters end up with a positive value in the dictionary
    # necessary chars in dict will have a count of how many we need
    for c in string: chars_table[c] = 0
    for c in target:
        if c not in chars_table: return ""
        else: chars_table[c] += 1

    left = right = 0
    starting_left = -1          # tracks beginning index of shortest substring
    min_length = float('inf')   # tracks min length of shortest substring
    counter = len(target)       

    while right < len(string):

        # This is where we move right pointer.
        # 1. we check if moving right pointer will add a char that we need.  
        #    if we do, we decrement counter by 1
        #    we can tell if it is a char we need by seeing if the dictionary entry
        #    is positive before we decrement
        # 2. we decrement its dictionary entry
        # 3. actually move right pointer
        # atomic operation
        if chars_table[string[right]] > 0: counter -= 1
        chars_table[string[right]] -= 1
        right += 1
        # atomic operation

        # counter 
        while counter == 0:
            # we find a new shortest substr
            if right - left < min_length:
                min_length = right - left
                starting_left = left

            # same as other operation, but reverse
            # atomic operation
            chars_table[string[left]] += 1
            if chars_table[string[left]] > 0: counter += 1
            left += 1
            # atomic oepration

    if min_length == float('inf'): return ""
    else: return string[starting_left: starting_left + min_length]




