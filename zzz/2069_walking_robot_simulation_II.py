

# timeout soln
class Robot(object):
    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.R, self.C, self.r, self.c = height, width, 0, 0
        self.dir = 0
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.dir_str = ["East", "North", "West", "South"]
        
    def in_bounds(self, testr, testc):
        return testr >= 0 and testc >= 0 and testr < self.R and testc < self.C
    
    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        for i in range(num):
            newr, newc = -1, -1
            
            while not self.in_bounds(newr, newc):
                dr, dc = self.dirs[self.dir]
                newr, newc = self.r + dr, self.c + dc
                
                # need to change direction
                if not self.in_bounds(newr, newc):
                    self.dir = (self.dir + 1) % 4
                
            self.r, self.c = newr, newc
                

    def getPos(self):
        """
        :rtype: List[int]
        """
        return [self.c, self. r]
        

    def getDir(self):
        """
        :rtype: str
        """
        return self.dir_str[self.dir]
        