# Nathan Zhu Johnny's house thanksgiving
# Leetcode 412 | easy | easy
# Category: Fizzbuzz

def fizzBuzz(n):
    return ["Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i) for i in range(1, n + 1)]