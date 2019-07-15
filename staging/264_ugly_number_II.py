# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.


# 1 = 2^0  * 3^0 * 5^0
# 2 # 2^1 * 3^0 * 5^0
# 3 = 2^0 * 3^1 * 5^0
# 4 = 2^2 * 3^0 * 5^0
# 5 = 2^0 * 3^0 * 5^1

def nth_ugly(n):
    # power_2 is 0 cause we need to get 1
    power_2, power_3, power_5 = 1, 1, 1
    ugly_arr = [1]

    for i in range(1, n):
        next_ugly = (min(2 ** power_2, 3 ** power_3, 5 ** power_5))
        ugly_arr.append(next_ugly)

        if next_ugly % 2 == 0:
            power_2 += 1
        if next_ugly % 3 == 0:
            power_3 += 1
        if next_ugly % 5 == 0:
            power_5 += 1
        
    return ugly_arr[-1]

if __name__ == "__main__":
    print(nth_ugly(10))
    print(nth_ugly(1))

        

