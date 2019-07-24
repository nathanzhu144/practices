
import collections
import heapq

def freq_sort(string):
    c = collections.Counter(list(string))
    heap, ret = [], []
    for char, count in c.items():
        heapq.heappush(heap, (-1 * count, char))

    while heap:
        count, char = heapq.heappop(heap)
        ret.extend([char] * ((-1) * count))

    return "".join(ret)

if __name__ == "__main__":
    print(freq_sort("aasdseea"))