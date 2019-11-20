# Nathan Zhu
# Leetcode 353 | med | not too easy
# Category: Design

import collections 

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        start = (0, 0)
        self.snake = collections.deque([start])    # [tail] [middle] [middle] [head]
        self.snakePos = set([start])
        self.foods = collections.deque(food)       
        self.width, self.height = width, height
        self.directions = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        head = self.snake[0]
        next_pos = (head[0] + self.directions[direction][0], head[1] + self.directions[direction][1])
        
        # Remove tail before checking whether new head is valid because new head can be
        # if the previous tail position.
        tail = self.snake.pop()
        self.snakePos.remove(tail)
        if next_pos in self.snakePos or not (0 <= next_pos[1] < self.width and 0 <= next_pos[0] < self.height):
            return -1
        
        # Checking to see where the food currently is.
        curr_food = (-1, -1)
        if len(self.foods): curr_food = tuple(self.foods[0])
            
        
        # Add next HEAD position of snake.
        self.snake.appendleft(next_pos)
        self.snakePos.add(next_pos)
        
        if curr_food == next_pos:
            # We change foods to reflect that a food has been eaten.
            self.foods.popleft() 
            # Add back tail BACK because eating the food is
            # equivalent to combining food with the body
            self.snake.append(tail)
            self.snakePos.add(tail)
        
        # Score is proportional to body length 
        return len(self.snake) - 1