# Nathan Zhu, Amex Building, last week of work, Monday August 5th, 2019 1:17 am
# Leetcode 630 | hard | yeah pretty hard
#
# Thinking of the algorithm and convincing yourself, let alone someone else
# the algorithm is correct in 30 minutes is challenging at best.
#
# Intuition:
# This is DIFFERENT from optimal lecture hall scheduling, as lecture halls have a scheduled
# start and end time. These classes can be started anytime, but have to end before the end time.
# 
# This makes it a different algorithm.
#
# So, we first sort all classes by their end time. We keep a tally of the start time for the next class.
# we are always taking classes, so everytime we take a class, we just add class duration to start time to get next start time
# 
# While we add classes, we add the length of each class of our priority queue.  Our pq represents the
# current classes we have in our schedule.  Since we don't need to print the exact schedule later, we 
# only store lengths in our pq.
#
# If we add a class, and start goes from:  start <= end ->  start > end,
# that means that we have scheduled in so many classes, we have one too many class in our backpack.
# The optimal strategy *obviously* to reduce our start is to take the longest class we have taken
# so far, and remove it from our schedule.  This CAN be the class we just added, or any of the 
# previous classes we have taken.  Removing this one class guarantees that start will be <= end after
# the class is removed. 
#
# At the end, we just return the length of the pq. 
#
# 
# Followup: 
# Suppose we wanted to print the schedule of classes to take.  How to do this?
# Easy, in the priority queue we keep an identification so we know which class this length corresponds to.
# Then, at the end, we iterate through the courses sorted by earliest end, and return the ones inside priority queue.
import heapq

def scheduleCourse(courses):
    pq = []          # pq holds lengths of all classes we have taken so far
    start = 0
    for length, end in sorted(courses, key=lambda x:x[1]):
        start += length
        heapq.heappush(pq, -length)
        if start > end:
            start += heapq.heappop(pq)
    return len(pq)

if __name__ == "__main__":
    print(scheduleCourse( [[1,2],[1,3], [100, 100]]))