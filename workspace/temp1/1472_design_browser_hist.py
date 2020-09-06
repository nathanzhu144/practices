# /* Nathan Zhu June 7th, 2020  
# *  Leetcode 1472 | medium | medium
# *  Category: Design Stack
# */



class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.curr, self.forw = [homepage], []
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.forw = []
        self.curr.append(url)

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while len(self.curr) > 1 and steps > 0:
            steps -= 1
            self.forw.append(self.curr.pop())
        return self.curr[-1]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.forw and steps > 0:
            steps -= 1
            self.curr.append(self.forw.pop())
        return self.curr[-1]
        