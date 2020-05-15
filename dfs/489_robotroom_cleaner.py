# Nathan Zhu Friday August 9th, 2019. 12:30 am, EHS 55 John street, last day of work is tomorrow.
# Nathan Zhu Thursday May 7th, 2020. 12:35 am. Stockton, CA. First day of work at Salesforce is in a week-ish
# Leetcode 489 | hard | yeah pretty damn hard if you have never seen it before
# Category: DFS islands traversal with a "strong" twist

# The hard part of this program is here.
# When you do a DFS, you don't think about how a physical object interacts with everything.
#
# In this problem, whenver you finish cleaning a square and backtrack, you have to literally
# rotate the robot around, mark it backwards, and orient it in the original direction.
#
# Furthermore, whenever you go into a new stack frame, you have to keep a "olddir" integer
# that keeps track of which way the robot is facing when it enters the that square. Otherwise,
# given the directions array, it will go into the wrong direction first.

def cleanRoom(self, robot):
    """
    :type robot: Robot
    :rtype: None
    """
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # dfs is called only when (row, col) not in visited
    # olddir keeps track of which way the robot was pointing when dfs was called.
    def dfs(row, col, visited, olddir):
        visited.add((row, col))           
        robot.clean()
        
        for i in range(4):
            # Positions up, right, down, left in that order
            # Ordering is important to keep order consistent with robot turning left
            # NOTE: We have (i + olddir) % 4 because, to keep track of which direction the robot is facing
            newrow, newcol = row + directions[(i + olddir) % 4][0], col + directions[(i + olddir) % 4][1]
            
            # We only need to move and backtrack robot if robot successfully moves.
            if (newrow, newcol) not in visited and robot.move():
                # olddir + 1 is direction robot is facing
                dfs(newrow, newcol, visited, olddir + i)
                # as stack frame pops back, we need to do 2 things.
                # 1. Turns robot around.
                # 2. Moves robot back to original square.
                # 3. Moves robot back to original orientation.
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
                
            # Keep turning left 4 times.
            robot.turnLeft()
    visited = set()
    dfs(0, 0, visited, 0)
