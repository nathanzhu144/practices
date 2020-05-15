# Nathan Zhu, April 4th, 2020 Meera's virtual birthday was yesterday!
# Leetcode 365 | medium | medium?
# Category: DFS, linked list cycle

def canMeasureWater(x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    if x > y: return canMeasureWater(y, x, z) # Not necessary, but hard to prove unncessary
    
    def transition(a, b):
        next_a, next_b = None, None
        if b == y:
            next_a, next_b = a, 0
        elif a == 0:
            next_a, next_b = x, b
        elif 0 < a <= x: 
            cap = y - b
            next_a = max(0, a - cap)
            next_b = min(y, b + a)
        return next_a, next_b
            
    a, b = x, y  # This is important to set to these two.
    visited = set()
    while True:
        curr = (a, b)
        if a == z or b == z or a + b == z: return True
        if curr in visited: return False
        visited.add(curr)
        a, b = transition(a, b)
            