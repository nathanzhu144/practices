# Nathan Zhu Monday, August 5th, 2019 11:39 pm EHS 55 John Street, Last week of internship yo
# Leetcode 621 | medium | medium-harder medium
# Category: priority queue, greedy
# Link    : https://leetcode.com/problems/task-scheduler
#
# Runtime analysis: 
# O(N * n), where N is number of tasks, and n is cooldown period.
# 
# https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation
# Intuition: 
# Suppose there is no cooldown.  This question is not too hard then.  We try to "grab" the task 
# with the highest count first.  Then, we add it back to pq.  Then, "grab" the task with the highest
# count.  This one can be the same as the last task.  Do until pq is empty.
#
# However, in this problem there's a cooldown.  After grabbing the task with highest count, we cannot
# grab it again for n turns.  
#
# How to deal with this?  
#
# Instead of thinking of this problem in  terms of tasks, we can think of it in terms of 
# cooldown slices.  We go through the pq, going from bigger to smallest, and adding one of
# each to order. If there is more of the task to be done, we add it onto the cooldown backlog.
# If we run outta tasks, and cooldown is not over, we add "" until cooldown is done.
#
# Then, we do another time slice until backlog and pq are empty.
# 
# How does this prevent collisions?
# (Nonobvious)
# If the cooldown slice >= size of pq, we can guarantee the relative ordering chosen of
# the tasks will stay the same in the pq on the next iteration around.  Therefore, the 
# same task will always be separated by n spaces.
#
# If the cooldown slice < size of pq, we don't need to worry.  Again, relative ordering
# of chosen tasks will always the same, but some tasks can be replaced by other tasks.
# Overall, each task will be separated by n spaces or more than n spaces.
#

import heapq
import collections

def least_intervals(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    order, pq = [], []
    
    # Negating count makes pq act like a max-pq, higher count -> higher priority
    for task, count in collections.Counter(tasks).items():
        heapq.heappush(pq, (-count, task))

    while True:
        # To do a pass 
        i = 0
        cooldown = []
        while i <= n:
            if pq:
                count, task = heapq.heappop(pq)
                if count < -1:
                    cooldown.append((count + 1, task))
                order.append(count)
            else:
                order.append("")
            # we are done with all tasks
            if not pq and not cooldown: return len(order)
            i += 1

        for c in cooldown:
            heapq.heappush(pq, c)

if __name__ == "__main__":
    print(least_intervals(["A","A","A","B","B","B", "C"], 2))