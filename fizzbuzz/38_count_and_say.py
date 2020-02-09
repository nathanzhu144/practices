# Nathan Zhu Friday Jan 17th, 2020 3:02 pm Duderstadt Library where they are talking about proving the NlogN soln for finding closest pair of pts in NlogN time
# Leetcode 38 | easy | not hard, but damn this one frustrated me too long
# Category: Fizzbuzz

def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    curr = "1"
    
    for i in range(1, n):
        count = 1
        temp = []
        for i in range(1, len(curr)):
            if curr[i] == curr[i - 1]: count += 1
            else:
                temp.append(str(count))
                temp.append(str(curr[i - 1]))
                count = 1
                
        temp.append(str(count))
        temp.append(str(curr[-1]))
        
        curr = "".join(temp)
        
    return curr
                    
                    
if __name__ == "__main__":
    print(countAndSay(5))