from string import punctuation
import heapq

def strip_punctuation(paragraph):
    return ''.join(c for c in paragraph if c not in punctuation)

if __name__ == "__main__":
    paragraph = "a, a, a, a, b,b,b,c, c"
    paragraph = [word.lower() for word in (strip_punctuation(paragraph)).split()]
    print(paragraph)