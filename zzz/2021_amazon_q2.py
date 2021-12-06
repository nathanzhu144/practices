# https://leetcode.com/discuss/interview-question/1488281/amazon-oa
# 1. I iterate through the array one character at a time, and greedily try to form pairs.  This is inspired by this idea:

# For any array, if at this point, if I have a "1":

# If I have K "...1 .... 0.." before this point, I can pair all K of those with this current 1, firming K  new "..1 ... 0 ... 1.."

# Conversely, if we have a "0"

# If I have K "0.... 1" before this point, I can pair all K of those with this current 0, firming K  new "..0 ... 1 ... 0."

# We also keep track of the number of 1s, and 0s we have seen so far.

# If we have K "1"s so far, and we see a "0", our count of "1 ... 0" goes up by K

# If we have K "0"s so far, and we see a "1" our count of "0 ... 1" goes up by K





# 2. This is a O(N) time complexity.

# I finish this task in one pass, and in each iteration, I am doing O(1) work.  

# Final answer: O(N)


def numberOfWays(arr):
    ret = 0
    count_z, count_zo, count_o, count_oz = 0, 0, 0, 0
    
    for num in arr:
        if num == '1':
            count_zo += count_z
            count_o += 1
            ret += count_oz
        elif num == '0':
            count_oz += count_o
            count_z += 1
            ret += count_zo
            
    return ret