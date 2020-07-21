# Nathan Zhu Tuesday July 23rd, 2019, Overlooking Hudson River 36th floor.
# Nathan Zhu Wednesday June 3rd, 2020, Stockton, CA. Not overlooking hudson, overlooking stockton, CA. A year later, and this is easier!  
#                                                    This time I did it with two stacks
# Leetcode 155 | easy | lol, not so easy
# 
# # Observations #
# 
# As the stack grows, we can easily prove that the minimum value of the stack
# will never increase - it can only stay the same or decrease.
# 
# Therefore, when we pop, we can get back to a higher minimum value,
#            when we push, we can get back to a lower minimum value
#
# Whenever we push a element, we push on the current minimum value.  Therefore,
# if we pop back to that element, the minimum of the stack will be the same as at that point.
#


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Data Structures #
        # Stack is a list of pairs (int, int), representing (curr_item, curr_min)
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # The magic happens here #
        # The key insight is in the observations...
        curr_min = self.getMin()
        if curr_min == None or x < curr_min:
            curr_min = x
        self.stack.append((x, curr_min))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack: return None
        else: return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack: return None
        else: return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    mi = MinStack()
    mi.push(0)
    mi.push(1)
    mi.push(0)
    print(mi.getMin())
    mi.pop()
    mi.top()
    print(mi.getMin())
