# Nathan Zhu Feb 9th, 2020.  I'm with Julie and Zhongfu today at the fishbowl.
# Leetcode 232 | easy | easy
# Category: Design.
#
# Apparently this can be used to do concurrency without threads?

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # stack1 [A, B, C]  [D E]
        # stack2 [C, B, A]   [E D]
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
        return self.stack2[-1]
        
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.stack1 and not self.stack2: return True
        return False