#  Nathan Zhu American Express Tower, 2:27 pm, focus room 36th floor
#  havent had breakfast yet
#
#  
#  So, given an array of gas, and an array of costs,
#  where at station k, gas[k] is amount of gas
#  you get at gas station, and cost[k] is amount of gas it costs to get to
#  the k + 1th station, try to find an index k, where if you start
#  at that index, you never run out of gas (your total gas never goes below 0) until
#  you get back to that index k.
#
#  Note you start with 0 gas.
# 
#  The idea behind this one is actually pretty interesting.  Define G(i) as amount
#  of gas increase you get at station i.  
#
#  G(i) = gas[i] - cost[i]
#
#
#  Now, let us start at station i.
#
#  Suppose we are able to go through...
#
#  G(i), G(i + 1) ... G(j - 1), G(j)
#  
#  And we run out of gas at position j.
#
#
#  It must be true that the summation of G(i) + G(i + 1) + ... + G(k - 1) + G(k) where i <= k < j
#  is positive or 0.  Otherwise we reach a contraction, as we would've run out of gas at G(k)
#  
#  This also means that IF starting a sequence at G(i) leads to a failed car ride, starting a sequence
#  at G(k) will also lead to failed car ride, as this is true:
#
#       G(i) + G(i + 1) + ... + G(k - 1) + G(k) + G(k + 1) + ... + G(j - 1) + G(j) >= G(k) + G(k + 1) + ... + G(j - 1) + G(j)
# 
#
#  Therefore, instead of going from station i to station i + 1, we can advance to checking station j + 1, as we 
#  guarantee that the stations between i and j+1 all will not work.
#
#  
#  NOTE: This results in an O(n) solution instead of an O(n^2) solution, as this results in scanning thru
#        the list only once
#  
def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    station = 0
    while station < len(gas):
        curr_gas = 0
        can_get_back = True
        
        for i in range(0, len(gas)):
            curr_gas += (gas[(station + i) % len(gas)] - cost[(station + i) % len(gas)])
            
            if curr_gas < 0:
                can_get_back = False
                station = i + station + 1
                break
                
        if can_get_back:
            return station
        
    return -1
                         

if __name__ == "__main__":
    print(canCompleteCircuit([1,2,3,4,5],[0,0,0,15,6]))