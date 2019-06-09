### Nathan Zhu Sunday 12:19 pm June 9th, 2019 in Amex Building, 36th floor, private focus room
#   This problem took literally 2 hours lol.  I first tried implementing with DP, and got into issues
#   with cycles, but this is a BFS problem.  Did not recognize it as such.
#
#  This is the first problem I tried whiteboarding.  Shuffled problems, and got this one randomly
#  I first tried solving it by doing DP, but DP cannot work.  The reason is that there are cycles that
#  exist in snakes and ladders, and I there is no good way to get around that.

#  Idea here is to do a simple BFS.  
#  We return when we first get to the exit.  
#  
#
#  Snakes and ladders is a game such that you start at the bottom left and end at the top right
#  Return the FEWEST possible steps from start to end
#
#   /***********************
#    end 98 97 ..                   Note   end is square 99 
#                                        start is square 1
#
#    21 22 ...
#    20 19 ...    14 13 12 11
#    start 2 3 4 5 6 7 8 9 10
#    ***********************/
#
#  Step 1: We convert the 2d array into a 1d array, making it easier to do BFS stuff.
#
#   [0, 1, 2, ...  99, 100]
#
#  Step 2: Now we have a 1D board, and we do a BFS
#    
#   Let's think of an arbitrary square k, where 0 <= k <= N^2 - 1
#
#   From k, we can get to k + 1, k + 2, k + 3, k + 4, k + 5, k + 6,
#           but note that in the same move, if the square has a 
#           snake or ladder, we will go to a different square on 
#           that move
#
#   Therefore, k can add up to 6 nodes.
#
#   NOTE: We can get an infinite cycle if we just do this.  Reason is that
#         let's say we have a 3x3 board where every snake leads back to position
#         1.  It is obviously impossible to get to the end.
#
#         Solution is we keep a hash table of which numbers have been visited.
#         We only add a number onto the queue if that number has not been visited before.
#
# 
#   NOTE: Runtime is N^2, as there are N^2 positions on the board
#
#          
#
#  
def snakesAndLadders(board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    if not board:
        return 0

    oneDboard = list()

    #################################
    ##  Convert 2d list to 2d list ##
    #################################

    needtoswap = False
    for row in range(len(board) - 1, -1, -1):
        templist = []
        for col in range(0, len(board[0])):
            templist.append(board[row][col])

        if needtoswap:
            templist = templist[::-1]

        needtoswap = not needtoswap
        oneDboard.extend(templist)


    #########################################
    ##     Where the BFS takes place       ##
    #########################################

    curr_level = list()           #queue of board positions
    next_level = list()             
    curr_level.append(0)
    jump_counter = 0              # return value, tracks min number of jumps to get to end
    visited = dict()              # we put index into dict if we have visted it already

    while curr_level:      
        while curr_level:
            curr_position = curr_level[0]
            curr_level.pop(0)
            
            #when we reach the end of the board
            if curr_position == len(oneDboard) - 1:
                return jump_counter

            #We can jump curr + 1, curr + 2 ... curr + 6, just like a dice roll
            for i in range(1, 7):
                # doing this jump would put us out of bounds
                if curr_position + i >= len(oneDboard):
                    continue

                # calculating next jump from here
                nextposition = 0
                # if no snake/ladder
                if oneDboard[curr_position + i] == -1:
                    nextposition = curr_position + i
                # if we hit a snake/ladder
                else:
                    nextposition = oneDboard[curr_position + i] - 1
                
                # we don't want to do this move if we have already done it
                if nextposition in visited:
                    continue
                visited[nextposition] = True
                next_level.append(nextposition)

        curr_level = next_level[:]
        jump_counter += 1
        next_level = list()

    return -1


if __name__ == "__main__":
    print(snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]]))