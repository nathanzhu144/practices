# 
# 
# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

# If there isn't any rectangle, return 0.
# NOTE:  All points are distinct.
#        If not, before we read into set, we prob ned to check to see if any
#        two points are same, making a rectangle area of 0
def min_area_rect(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    points_set = set()
    for x, y in points: points_set.add((x, y))

    ret = float('inf')
    for x1, y1 in points:
        for x2, y2 in points:
            # this check ensures we don't consider the same point twice.
            if x1 > x2 and y1 > y2:
                # verify other two points aren't in the set
                if (x2, y1) in points_set and (x1, y2) in points_set:
                    new_area = (y1 - y2) * (x1 - x2)
                    ret = min(ret, new_area)

    return ret if ret != float('inf') else 0
