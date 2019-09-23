# Nathan Zhu Sunday Sept 22nd, 2019
# Leetcode 65 | hard | FOOOKING HARD MANN
# Category: Fizzbuzz / state diagram / trash / brainmelter
# 
# THIS IS SUM TRASH
#
# So the idea behind this is the figure out what inputs are a valid number.  This is a great and flexible impl
# because depending on what interviewer wants, you can change the state diagram.  
# I actually like this implementation a lot.



def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    state = [{}, 
    # State (1) - initial state (scan ahead thru blanks)
    {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
    # State (2) - found a sign (NOTE: sign followed by a . MUST be followed by a number, NUMBER CANNOT B FOLLOWED BY ANOTHER DOT
    #                          (NOTE: number followed by a . does not necessarily have to be followed up by a number)
    {'digit': 3, '.': 4},
    # State (3) - digit consumer (until non-digit, like a dot, "e" or blank)
    {'digit': 3, '.': 5, 'e': 6, 'blank':9},
    # State (4) - found dot (HAPPENS AFTER SIGN, NEEDS NUMBER.)
    {'digit': 5},
    # State (5) - found dot (HAPPENS AFTER NUMBER, could have number, e or blank)
    {'digit': 5, 'e': 6, 'blank': 9},
    # State (6) - found 'e' (only a sign or a digit valid)
    {'sign': 7, 'digit': 8},
    # State (7) - sign after 'e' (only digit)
    {'digit': 8},
    # State (8), digit after 'e' (can have space or blanks)
    {'digit': 8, 'blank': 9},
    # State (9) - Terminal state (fail if non-blank found)
    {'blank': 9}]

    currstate = 1

    for c in s:
        if c >= '0' and c <= '9': c = 'digit'
        elif c == ' ': c = 'blank'
        elif c in '+-': c = 'sign'

        if c not in state[currstate]: return False
        currstate = state[currstate][c]

    if currstate not in [3, 5, 8, 9]: return False
    else: return True


if __name__ == "__main__":
    print(isNumber("1 4"))