# Nathan Zhu 3:51 pm Amex Tower 36th floor, Monday 3:53 pm
# Leetcode 657 | easy | super easy
# Did this question in 20 seconds!
#
#
# Input: "UD"
# Output: true 
# Explanation: The robot moves up once, and then down once.
#  All moves have the same magnitude, so it ended up at the origin where it started. 
#  Therefore, we return true.

def end_at_origin(moves):
    """
    :type moves: str
    :rtype: bool
    """
    x, y = 0, 0
    for move in moves:
        if move == "U": y += 1
        if move == "D": y -= 1
        if move == "R": x += 1
        if move == "L": x -= 1
    
    return x == 0 and y == 0