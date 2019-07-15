# Nathan Zhu 7:41 am
# 55th John Street June 21th, 2019
# BFS solution, where every position Z a node N can get to is connected by an
# edge.
# Naive BFS is N^2, as theoretically ...
# Node 1 can add N - 1 nodes
# Node 2 can add N - 2 nodes
#  .
#  .
#  .
# Node N - 1 can add 1 node
#
#
# However, I have a visited set, so it should not ever re-add nodes.  The
# whole soln should only process N nodes.  It still "kinda" doees N^2 work, 
# as the for loop still iterates through all the possibilities...

def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums: return False
    
    curr_pos = 0
    BFS = collections.deque([0])   # BFS contains square positions
    visited = set()
    
    while BFS:
        curr_pos = BFS.popleft()
        if curr_pos >= len(nums) - 1: return True
        for jump in range(nums[curr_pos] + 1):
            next_pos = jump + curr_pos
            if next_pos in visited: continue
            visited.add(next_pos)
            BFS.append(next_pos)
    return False

def can_jump_greedy(nums):
    curr_pos = len(nums) - 1
    while True:
        if curr_pos == 0: return True
        leftmost = -1
        for i in range(curr_pos - 1, -1, -1):
            if nums[i] + i >= curr_pos:
                leftmost = i

        if leftmost == -1: return False
        else: curr_pos = leftmost

if __name__ == "__main__":
    print(can_jump_greedy([2, 0, 0, 0, 2]))

                    