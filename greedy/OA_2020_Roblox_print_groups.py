# Nathan Zhu March 23rd, 2020.  
# Leetcode n/a | n/a | medium
# Category: Greedy
#
# 3. A social network has n active users, numbered from 0 to n — 1, who selectively friend other users to create groups of friends within the network. We define the following:
# Two users, x and y, are direct friends if they friend each other on the network.
# Two users, x and z, are indirect friends if there exists some direct friend, y, 
# common to both users x and z.
# Two users, x and y, belong to the same group if they are friends (either directly or indirectly) with each other.

# In other words, if user x is part of a group, then all of user x’s friends and friends of 
# friends belong to the same group.

# We describe the number of people in each group as an array of n integers, counts, where each
# countsi (0 ? i < n) denotes the total number of users in the group that user i belongs to. 
# For example, if counts = [3, 3, 3, 3, 3, 1, 3], then there are three groups; 
# users 0, 1, 2, 3, 4, and 6 are in one of two 3-person groups, and user 5 is in a 1-person group.

# ID            0    1    2    3    4    5    6
# Group Size    3    3    3    3    3    1    3

# A group is valid if all the users in the group have minimal ID numbers. In other words, a 
# group of size k must contain the k smallest ID numbers belonging to a group of that size with 
# respect to the smallest user ID in the group. For example, if counts = [3, 3, 3, 3, 3, 1, 3], 
# then the grouping [0, 1, 2], [3, 4, 6], and [5] is valid; however, 
# the grouping [0, 1, 4], [2, 3, 6], and [5] is not valid because the group [0, 1, 4] does not contain 
# the three smallest user IDs for the set of user IDs belonging to 3-person groups (i.e., {0, 1, 2, 3, 4, 6}).
# # q3 starts here
import collections

def Q3(arr):
    c = collections.defaultdict(list)
    num_to_group = dict()
    N = len(arr)

    # grouping
    for i, num in enumerate(arr):
        c[num].append(i)
        num_to_group[i] = num

    # sorting each group
    for key, val in c.items():
        c[key] = val[::-1]

    used = set()
    ret = []
    for i in range(N):
        if i in used: continue

        group_size = num_to_group[i]

        curr = []
        for i in range(group_size):
            num = c[group_size].pop()
            used.add(num)
            curr.append(num)
        ret.append(curr)

    for item in ret:
        print(" ".join(map(str, item)))

        

if __name__ == "__main__":
    Q3([3, 3, 3, 3, 3, 1, 3])