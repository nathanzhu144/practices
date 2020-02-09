# Nathan Zhu Feb 3rd, 2020, Monday.  SI 106 discussion, talking about mutation diagrams or something.
# Leetcode 853 | medium | not bad
# Category: Stack / misc tricks

# Good explanation.
# https://leetcode.com/problems/car-fleet/discuss/255589/Python-Code-with-Explanations-and-Visualization-Beats-95
# 

def car_fleet(target, position, speed):
    temp = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
    stack = list()
    for p, s in temp:
        time = (target - p) / (s * 1.0)
        if not stack or time > stack[-1]: stack.append(time)
    
    return len(stack)
            

if __name__ == "__main__":
    print(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))