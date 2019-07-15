# 321. Create Maximum Number
# Hard
https://leetcode.com/problems/create-maximum-number/discuss/77285/Share-my-greedy-solution
# Input:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# Output:
# [9, 8, 6, 5, 3]

# [4, 3, 5]
# [2, 9]

# max(4, [3, 5])
#        [2, 9]
# max(2, [4, 3, 5]
#              [9])

# if (,[2, 3, 5])

# 53  [1, 2, 3]
#     [1, 2, 3]

# Share
# Given two arrays of length m and n with digits 0-9 representing two numbers. 
# Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits 
# from the same array must be preserved. Return an array of the k digits.

# Note: You should try to optimize your time and space complexity.

def create_maxim_number(num1, num2, k, mem):
    def make_max_num(num, k, mem):
        key = (k, tuple(num))
        if key in mem: return mem[key]
        if not k: return ""
        if not num: return ""
        
        use_first = int(str(num[0]) + make_max_num(num[1:], k - 1, mem))
        n_use_fir = 0 if not make_max_num(num[1:], k, mem) else int(make_max_num(num[1:], k, mem))

        mem[key] = str(max(use_first, n_use_fir))
        return mem[key]



    def helper(num1, num2, k, mem):
        key = (k, tuple(num1), tuple(num2))
        if key in mem: return mem[key]
        if not k: return ""

        # If either num1 or num2 are empty, we return the non-empty one
        # There's only one way to make a number, as we have to maintain relative order of digits
        if not num1: return "".join(str(c) for c in make_max_num(num2, k, dict()))
        if not num2: return "".join(str(c) for c in make_max_num(num1, k, dict()))

        use_first = int(str(num1[0]) + helper(num1[1:], num2, k - 1, mem))
        use_secon = int(str(num2[0]) + helper(num1, num2[1:], k - 1, mem))
        n_use_fir = 0 if not helper(num1[1:], num2, k, mem) else int(helper(num1[1:], num2, k, mem))
        n_use_sec = 0 if not helper(num1, num2[1:], k, mem) else int(helper(num1, num2[1:], k, mem))
       
        mem[key] = str(max(use_first, use_secon, n_use_fir, n_use_sec))
        return mem[key]
    return helper(num1, num2, k, dict())

# def make_max_num(num, k, mem):
#     key = (k, tuple(num))
#     if key in mem: return mem[key]
#     if not k: return ""
#     if not num: return ""
    
#     use_first = int(str(num[0]) + make_max_num(num[1:], k - 1, mem))
#     n_use_fir = 0 if not make_max_num(num[1:], k, mem) else int(make_max_num(num[1:], k, mem))

#     mem[key] = str(max(use_first, n_use_fir))
#     return mem[key]

if __name__ == "__main__":
    # print(create_maxim_number([3, 9], [8, 9], 2, dict()))
    print(create_maxim_number([3,8,5,3,4], [8,7,3,6,8], 5, dict()))
    #print(make_max_num([3,8,5,3,4], 2, dict()))
    
# [3,8,5,3,4]
# [8,7,3,6,8]
# 5