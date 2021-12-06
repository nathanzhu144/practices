
# Greedy problem.
# You are trying to spell a word.
# To do so you have to use a wheel with the alphabet sorted on it.
#  [Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B]
# Note how alphabet wraps around, imagine a circle like this array.
# 
# Your char pointer starts at A, and takes 1 cost to move once.  
# What is minimum cost to spell the whole word?
# 
# Intuition:
# We have to spell the word in order
# We can choose to move left or right from character to character.
# We can greedily choose the shortest distance moving left or right.
#
# Only gotcha is you have to move the pointer in the very beginning from 'A'
# to the first letter.

def getTime(s):
    # Write your code here
    ret = 0
    if s[0] != 'A':
        s = 'A' + s
    for a, b in zip(s, s[1:]):
        diff = min(abs(ord(a) - ord(b)), 26 - abs(ord(b) - ord(a)))
        ret += diff
    return ret