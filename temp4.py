        
def func(seats):
    longest = 0
    curr_len = 0
    # We want to find the longest group of 0s
    # Unless on left or right
    i = 0
    while i < len(seats):
        if seats[i] == 1:
            while i < len(seats) and seats[i] != 0:
                i += 1
            if curr_len > longest:
                longest = curr_len
                curr_len = 0
            curr_len = 0
        elif i == len(seats) - 1 and seats[i] != 1:
            i += 1
            curr_len += 1
            if curr_len > longest:
                longest = curr_len
        else:
            i += 1
            curr_len += 1
    
    num_zeroes_left, num_zeroes_right = 0, 0
    for i in range(len(seats)):
        if seats[i] != 1: num_zeroes_left += 1
        else: break
            
    for i in range(len(seats) - 1, -1, -1):
        if seats[i] != 1: num_zeroes_right += 1
        else: break
    
    return [num_zeroes_left, num_zeroes_right, (longest + 1)]
if __name__ == "__main__":
    print(func([1,1,1,0,1,0,1,1,0,0,1]))


[["E","E","E","E","E","E","E","E"],
["E","E","E","E","E","E","E","M"],
["E","E","M","E","E","E","E","E"],
["M","E","E","E","E","E","E","E"],
["E","E","E","E","E","E","E","E"],
["E","E","E","E","E","E","E","E"],
["E","E","E","E","E","E","E","E"],
["E","E","M","M","E","E","E","E"]]
[0,0]

Output
    [0, 0]
    [["B","B","B","B","B","B","1","E"],
    ["B","1","1","1","B","B","1","M"],
    ["1","E","M","1","B","B","1","1"],
    ["M","E","1","1","B","B","B","B"],
    ["1","1","B","B","B","B","B","B"],
    ["B","B","B","B","B","B","B","B"],
    ["B","1","2","2","1","B","B","B"],
    ["B","1","M","M","1","B","B","B"]]
expected
    
    [["B","B","B","B","B","B","1","E"],
    ["B","1","1","1","B","B","1","M"],
    ["1","2","M","1","B","B","1","1"],
    ["M","2","1","1","B","B","B","B"],
    ["1","1","B","B","B","B","B","B"], 
    ["B","B","B","B","B","B","B","B"],
    ["B","1","2","2","1","B","B","B"],
    ["B","1","M","M","1","B","B","B"]]