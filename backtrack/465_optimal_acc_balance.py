# Nathan Zhu July 23rd, 2019 6:21 pm, in the office on a weekend again.
# Leetcode 465 | hard | pretty hard, I had little idea how to do it
# Category: Backtracking
# 
# Done in real-time in a "random-set on-site interview"
# Rating was 5.23/10, beating 84% of all users.
# 
# https://leetcode.com/problems/optimal-account-balancing/

# Input:
# [[0,1,10], [2,0,5]]
# Output:
# 2
# Explanation:
# Person 0 gave person 1 $10.
# Person 2 gave person 0 $5.

# Two transactions are needed. One way to settle the debt is person 1 pays person 0 and 2 $5 each

import collections


def minTransfers(transactions):
    """
    :type transactions: List[List[int]]
    :rtype: int
    """
    def backtrack(people, people_i, transactions_so_far):
        while people_i < len(people) and people[people_i] == 0:
            people_i += 1

        if people_i >= len(people):
            return transactions_so_far

        min_transactions = float('inf')
        for i in range(people_i, len(people)):
            if people[i] * people[people_i] < 0:
                people[i] += people[people_i]
                candidate_min = backtrack(people, people_i + 1, transactions_so_far + 1)
                min_transactions = min(min_transactions, candidate_min)
                people[i] -= people[people_i]

        return min_transactions
    
    # Have an array for outstanding transactions
    # - money means that person is owed money
    # + money means that person is has to give money
    
    temp = collections.defaultdict(lambda: 0)
    
    for t in transactions:
        temp[t[0]] += -1 * t[2]
        temp[t[1]] += t[2]
        
    people = [x for x in temp.values() if x != 0]
    
    return backtrack(people, 0, 0)