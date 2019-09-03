# Nathan Zhu August 27th, 2019 10:57 pm
# Leetcode 1090 | medium | medium

# Category: priority queue, ban elements too much
# Google- On-Site Interview
# Your interview score of 7.03/10 beats 90% of all users.
# Time Spent: 1 hour 4 minutes 24 seconds
# Time Allotted: 2 hours

# Problem
# We have a set of items: the i-th item has value values[i] and label labels[i].
# Then, we choose a subset S of these items, such that:
# 
# |S| <= num_wanted
# For every label L, the number of items in S with label L is <= use_limit.
# Return the largest possible sum of the subset S.
# Example 1:
# Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
# Output: 9
# Explanation: The subset chosen is the first, third, and fifth item.

def largestValsFromLabels(values, labels, num_wanted, use_limit):
    """
    :type values: List[int]
    :type labels: List[int]
    :type num_wanted: int
    :type use_limit: int
    :rtype: int
    """
    # We use a map of labels -> num uses.  Everytime we pop something off pq
    #             we check to see how many times that label has been seen.
    #             if num times seen > use_limit, we can ignore that element and pop
    #             another element off.
    
    label_to_uses = collections.defaultdict(int)
    pq = list()
    retsum = 0
    
    for i in range(len(values)):
        heapq.heappush(pq, (-1 * values[i], labels[i]))
    
    # We keep going until we run outta elements in our pq, or we are done finding everything.
    while len(pq) > 0 and num_wanted > 0:
        value, label = heapq.heappop(pq)
        
        # We have used too many of this label.
        if label_to_uses[label] >= use_limit: continue
        
        label_to_uses[label] += 1
        retsum += (-value)
        num_wanted -= 1
        
    return retsum