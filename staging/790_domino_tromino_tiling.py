We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.


XX
XX

XX
X
 
#    ??AA
#    ??AA

#    ??BA 
#    ??BA

#    ???G
#    ??GG

#   ?  ??
#   ??  ?
#    ??GG
#    ???G

# Let F_norm(n) be number of tilings for a 2 x n rectangle.
# Let F_top(n) be number of tilings for a 2 x n rectangle with a tile sticking out at top
# Let F_bottom(n) be number of tilings for a 2 x n rectangle with a tile sticking out at the bottom.
#
# 

def f_bottom(n, mem):
    if n < 2: return 0
    if n in mem: return mem[n]
    mme[n] = f_norm(n, mem)