# Nathan Zhu, Sunday June 30th, 2019 Just landed in Laguardia, 11:43 pm
#   yo i finally understand quicksort.  I did the divide and conq approach for
#   largest subarray sum, and I re-did the dutch flag problem.  After doign these
#   two problems, I "re-invented" quicksort.  Like, I suddenly understood a sort
#   that could combine these two.  It was a magical moment.

def quicksort(arr):
    def helper(arr):
        if not arr or len(arr) == 1:
            return arr

        pivot = arr[len(arr) // 2]

        left = [l for l in arr if l < pivot]
        mid = [m for m in arr if m == pivot]
        right = [r for r in arr if r > pivot]

        return helper(left) + mid + helper(right)
    
    return helper(arr)

def quicksort_indices(arr):
    def helper(arr, left, right):
        if right - left == 0 or right - left == 1:
            return
        pivot = arr[len(arr) // 2]

        
if __name__ == "__main__":
    print(quicksort([23, 2, 24, 2, -1, -2, -4, 23, 10]))