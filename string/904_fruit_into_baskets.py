# Nathan Zhu August 27th, 2019 9:11 pm
# Leetcode 904 | medium | medium
# Category: sliding window string
# Google OA 1 hour total, 31 min 53 sec used, rating beating 85% of all users
# 
# What's longest subarray with only two elements?

def totalFruit(self, tree):
    """
    :type tree: List[int]
    :rtype: int
    """
    num_chars = 0

    # Maps char -> count in dict
    count = collections.defaultdict(int)

    max_fruit = 0
    left, right = 0, 0
    while right < len(tree):
        count[tree[right]] += 1
        if count[tree[right]] == 1: num_chars += 1
        right += 1

        while num_chars > 2:
            count[tree[left]] -= 1
            if count[tree[left]] == 0: num_chars -= 1

            left += 1

        max_fruit = max(max_fruit, right - left)

    return max_fruit