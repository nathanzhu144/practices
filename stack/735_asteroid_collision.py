
def asteroidCollision(asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    """
    # Note that if we ever have two asteroids and the left one is
    # negative and the right one is positive, they will never meet.
    # The only way is the left ast being positive, and the right one being
    # negative.
    
    
    ret = list()
    for ast in asteroids:
        # We keep going untitl it is impossible to get collisions (right > left)
        while ret and ast < 0 < ret[-1]:
            # New asteroid destroys asteroid on left
            if ret[-1] < -ast:
                ret.pop()
                continue
            elif ret[-1] == -ast:
                ret.pop()
            # Doesn't destroy an asteroid, so this asteroid must be destroyed
            break
        # Only get here if asteroid is positive, or asteroid destroys all positive asteroids to its left
        else:
            ret.append(ast)
    return ret

if __name__ == "__main__":
    print(asteroidCollision([5, 10, -5]))