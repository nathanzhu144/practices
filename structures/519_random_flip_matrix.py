# Nathan Zhu 11:25 pm Santa Cruz December 29th, 2019
# Leetcode 519 | medium | yeah medium?
# Category: Probability / Reservoir sampling / Design question
# I was really proud of myself that I figured out a way to do this with exactly one call to rand per flip,
# and while my big N notation was exactly the same, as I used the optimal algorithm, I did not implement
# the algorithm optimally.

# Optimal Reservoir sampling.
import random


class ReservoirSampling:
    def __init__(self, n):
        self.n = n
        self.upper_b = n
        self.m = dict()
        self.build()

    def build(self):
        self.upper_b = self.n
        self.m = dict()

    def get_next(self):
        self.upper_b -= 1
        r = random.randint(0, self.upper_b)
        ret = self.m.get(r, r)                    # if r doesn't exist in table, return r, else return r's val
        self.m[r] = self.m.get(self.upper_b, self.upper_b)  # map the value we drawed, r, to last element in array (or whatever it points to)
        return ret

    def reset(self):
        self.build()


class Solution:
    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.R = n_rows
        self.C = n_cols
        self.reservoir = ReservoirSampling(n_rows * n_cols)

    def flip(self):
        """
        :rtype: List[int]
        """
        val = self.reservoir.get_next()
        r, c = self.n2rc(val)
        return [r, c]


    def n2rc(self, n):
        row = n // self.C
        col = n - row * self.C
        return [row, col]

    def reset(self):
        """
        :rtype: void
        """
        self.reservoir.reset()



# This soln works in an interview, passed all but last 2 test cases on LC.  
# It is easier to write, and has the same bigN notation, but is less efficient in runtime as it manages two arrays.
# Also uses the idea of Reservoir sampling.

# import random
# class Solution(object):

#     def __init__(self, n_rows, n_cols):
#         """
#         :type n_rows: int
#         :type n_cols: int
#         """
#         self.zero = []
#         self.one = []
#         #self.matrix = [[0 for c in range(n_cols)] for r in range(n_rows)]
#         self.R = n_rows
#         self.C = n_cols
        
#         for r in range(self.R):
#             for c in range(self.C):
#                 self.zero.append([r, c])

#     def flip(self):
#         """
#         :rtype: List[int]
#         """
#         idx = random.randint(0, len(self.zero) - 1)
#         self.zero[idx], self.zero[-1] = self.zero[-1], self.zero[idx]
#         r, c = self.zero.pop()
        
#         self.one.append([r, c])
#         return [r, c]
        

#     def reset(self):
#         """
#         :rtype: None
#         """
        
#         self.zero.extend(self.one)
#         self.one = list()


if __name__ == "__main__":
    s = Solution(2, 3)
    for i in range(2 * 2):
        print(s.flip())
    s.reset()
    for i in range(2* 2):
        print(s.flip())