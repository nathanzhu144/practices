# Nathan Zhu Thursday August 22nd, 2019 2:38 pm.  Stockton California
# Leetcode 349 | easy | EZ
# Category: Misc, Using a set lol


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1set, nums2set = set(nums1), set(nums2)
    return [s for s in nums1set if s in nums2set]