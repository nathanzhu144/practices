# Nathan Zhu Sunday July 21st, 2019.  Amex 36th floor. 
# Leetcode 937 | easy | EZ
# Category: Fizzbuzz
#
# Observations:
# So, I learned something in python.  Since python's sort is stable, if you want to
# sort a list of something with more than 1 characteristic, if you first sort it by
# tie-breaking characteristic, then sort it by main characteristic, you  can get the
# correct ordering.

# Question 
# You have an array of logs.  Each log is a space delimited string of words.
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, 
# with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.


def reorderLogFiles(self, logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    num_log, alpha_log = [], []

    # classify two types of logs
    for log in logs:
        if log.split()[1].isalpha():
            alpha_log.append(log)
        else:
            num_log.append(log)

    # So, note that python sort is stable, so if we sort by identifier.  
    # Then, we sort by lexicographic order, ignoring identifer
    # That way, it will be sorted in lexicographic order, with identifier as tie-breaker
    alpha_log.sort(key = lambda x: x.split()[0])
    alpha_log.sort(key = lambda x: x.split()[1:])

    return alpha_log + num_log