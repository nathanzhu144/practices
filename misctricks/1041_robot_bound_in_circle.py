def isRobotBounded(instructions):
    """
    :type instructions: str
    :rtype: bool
    """
    # if "instructions" leaves the robot facing the initial direction, the robot can just walk away, unless instructions don't go anywhere.
    # if "instructions" turns the robot around 90 degrees each time, then the first instructions are undone by the third instructions,
    # and the second instructions are undone by the fourth instructions.
    # if "instructions" turns the robot around 180 degrees each time, then the first instructions are undone by the second instructions.
    
    r, c = 0, 0
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    didx = 0 
    
    for ch in instructions:
        if ch == 'G':
            r += dirs[didx % 4][0]
            c += dirs[didx % 4][1]
        elif ch == "L": didx -= 1
        else: didx += 1
    
    return (r, c) == (0, 0) or didx % 4 != 0