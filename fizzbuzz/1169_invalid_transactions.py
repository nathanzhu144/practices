# Leetcode 1169 | medium | annoying
# Category: Fizzbuzz
# Nathan Zhu November 17th, 2021, 12:13 pm
# In starbucks near Ripon climbing gym.  


# Clarifications:
# If an amount exceeds 1000 dollars, it is invalid.  If this transaction triggers rule #2
# with another transaction, and is the only transaction to do so, is it valid?
#
# Ideas:
# we could solve it with brute force
# in two passes:
# time is NlogN, space is O(N)
# N is number transactions
# 1. flag all of transactions exceeding 1k  O(N)
# 2. pair-wise compare all transactions     O(N^2)
#    to see if they have same name and different city
#
# second idea:
# 
# 1. flag all of transactions exceeding 1k  O(N)
# 2. 
#     name => [(time1, city1, i1),(time2, city2, i2) .... ]  sorted by time, index stored for figuring out which index each record was originally
#     for each item, compare to all other transactions within 60 min.
#     
#     Thus, we eliminate comparing with people who are not this person, and times which are higher than t + 60 which we did in brute force
#     worst cases is still N^2, which happens when there's only one person, and all times are within 60 min.
def invalidTransactions_dumb(transactions):
    flagged_over_1k = set()
    flagged_too_close = set()
    N = len(transactions)
    for i, t in enumerate(transactions):
        name, time, amt, city = t.split(",")
        
        # exceeds 1k
        if int(amt) > 1000:
            flagged_over_1k.add(i)
            
    for i in range(N):
        for j in range(i + 1, N):
            namea, timea, amta, citya = transactions[i].split(",")
            nameb, timeb, amtb, cityb = transactions[j].split(",")
            if namea == nameb and abs(int(timea) - int(timeb)) <= 60 and citya != cityb:
                flagged_too_close.add(i)
                flagged_too_close.add(j)
                
    return [transactions[i] for i in flagged_over_1k.union(flagged_too_close)]

def invalidTransactions_smart(transactions):
    """
    :type transactions: List[str]
    :rtype: List[str]
    """
    flagged_over_1k = set()
    flagged_too_close = set()
    N = len(transactions)
    name_to_transactions = collections.defaultdict(list)
    for i, t in enumerate(transactions):
        name, time, amt, city = t.split(",")
        
        # exceeds 1k
        if int(amt) > 1000:
            flagged_over_1k.add(i)
            
        name_to_transactions[name].append((int(time), city, i))
    
    # sorting each bucket by time
    for k, v in name_to_transactions.items():
        v.sort()
    
    for name in name_to_transactions.keys():
        for curri, items in enumerate(name_to_transactions[name]):
            time, city, i = items
            
            currj = curri + 1
            # only compare each person's transactions to their other transactions within 60 min
            while currj < len(name_to_transactions[name]) and name_to_transactions[name][currj][0] <= time + 60:
                # diff cities, same name, within 60 min
                if city != name_to_transactions[name][currj][1]:
                    flagged_too_close.add(i)
                    flagged_too_close.add(name_to_transactions[name][currj][2])
                currj += 1

    return [transactions[i] for i in flagged_over_1k.union(flagged_too_close)]