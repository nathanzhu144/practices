# Nathan Zhu 8:56 pm, December 26th, 2019 Napa Valley California
# Leetcode 636 | medium | medium
#
# Why do we need a stack?
#0start 1start 1stop 2start 2 stop 0stop
#                   ^ 0 runs again here, so we need a stack to keep track.
#
# Note: I had this basically exact question for my final interview at Chicago Trading this year in Nov 2019.
#       I'd briefly heard of this question, but never did it.  Their question was only different in that
#       they didn't have the timestamp + 1 notation for stops, and that they had a follow-up.
def exclusiveTime(n, logs):
    """
    :type n: int
    :type logs: List[str]
    :rtype: List[int]
    """
    
    stk = list()
    ret = [0] * n   # maps func id -> time spent
    last_t = 0      # time last process finished working
    
    for log in logs:
        f_id, tag, timestamp = log.split(":")
        f_id, timestamp = int(f_id), int(timestamp)
        
        # If we see a start, we can assume the top thing on the stack (if it exists)
        # has been running from last_t to current timestamp
        # 1. update time running for that function
        # 2. add new starting function
        # 3. update timestamp
        if tag == "start":
            if stk: ret[stk[-1]] += timestamp - last_t
            stk.append(f_id)
            last_t = timestamp
        
        # If we see an end, we can assume that the top thing on the stack has ended.
        # Since "end" means run to end of that timeblock, it actually means running to
        # timestamp + 1.
        # 1, update running time for top function
        # 2. pop top func off stack
        # 3. update timestamp to timestamp + 1
        
        else:
            ret[stk[-1]] += timestamp + 1 - last_t
            stk.pop()
            last_t = timestamp + 1
    return  ret
    