# Nathan Zhu Chicago O'Hare Airport, plane delayed 3 hours, currently 6:17 pm.
# Leetcode 301 | hard | I think somewhat hard, not too bad
# 
# So, this is a very tupical BFS problem.  Idea is what's the least number of parens you can remove
# to make a parens balanced.  We do a BFS
#
# I think cool part of this program the ingenious way of validating a parens.
#

def remove_inv_parens(s):
    # checks if a parens is balanced
    # this is actually a really easy way of checking whether a list is balanced, 
    # idea is if counter ever becomes negative, parens combination is unbalanced, and 
    # if counter is positive at end, parens combination is unbalanced
    # DOESN'T WORK FOR MULTIP TYPES OF PARENS
    def valid(string):
        counter = 0
        for i in string:
            if i == "(": counter += 1
            if i == ")": counter -= 1
            if counter < 0: return False
        return counter == 0

    def helper(string):
        level = [string]
        visited = set()
        
        while True:
            returned = filter(valid, level)            # we filter using valid, to see if any parens are valid now
            if returned: return returned               # if any are, we return all of them

            # We take turns removing a 
            level = [string[:i] + string[i + 1:] for string in level for i in range(len(string)) if string[i] == "(" or string[i] == ")"]   # generating new parens combinations by removing 
                                                                                                                                            # a parens
            level = list(set(level))                                                            # removing all duplicates in this level
            level = filter(lambda string: string not in visited, level)                         # removing all that are already visited
            for string in visited: visited.add(string)                                          # adding new strings to visited table
            
    return helper(s)
