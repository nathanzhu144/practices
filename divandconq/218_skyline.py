# Nathan Zhu Tuesday, July 30th, 2019 EHS 55th John Street
# Leetcode 218 | hard | yeah pretty hard...
# Category: Divide and Conqer (approach here) or priority queue
# Runtime: NLogN, cause we do O(N) in each stach frame, and we break into N/2 subproblems.
# I was scared of this problem for ages, thinking it was a dumb problem.
# There's a really cool divide and conquer soln that is really interesting, though.
#
# https://leetcode.com/problems/the-skyline-problem/discuss/61246/Share-my-divide-and-conquer-java-solution-464-ms
# https://faculty.kfupm.edu.sa/ics/darwish/stuff/ics353handouts/Ch4Ch5.pdf
# arr has buildings in the form [start_x, height, end_x]


# takes in buildingss-> return skyline
def get_skyline(arr):
    # Main function
    def helper(arr):
        if len(arr) == 0: return []
        if len(arr) == 1:
            start_x = arr[0][0]
            end_x = arr[0][1]
            height = arr[0][2]
            return [[start_x, height], [end_x, 0]]

        mid = len(arr) // 2
        return merge(helper(arr[: mid]), helper(arr[mid: ]))

    # We are given two skyline objects.  Merge them into a combined skyline.
    # Runs in O(N).
    def merge(left, right):
        leftidx, rightidx, currleftheight, currrightheight = 0, 0, 0, 0
        merged_list = []

        while leftidx < len(left) and rightidx < len(right):
            # This is x-position and height of new interval
            x, height = 0, 0

            # We separate into 3 different cases. 
            # 1. left_x  < right_x 
            # 2. left_x  > right_x
            # 3. left_x == right_x
            # We need to choose the leftmost building in both left and right for the next building in our merged list

            # Case 1: We choose the x-val of the point pointed to by leftidx
            if left[leftidx][0] < right[rightidx][0]:
                # Height of merged interval is maximum of current left height (left[leftidx][1]) and current right height (currrightheight)
                height = max(left[leftidx][1], currrightheight)
                # update current left height
                # store x-val of new point
                # remove front building of left from consideration
                currleftheight = left[leftidx][1]
                x = left[leftidx][0]
                leftidx += 1
            # Case 2: We choose the x-val of the point pointed to by rightidx
            elif left[leftidx][0] > right[rightidx][0]:
                height = max(right[rightidx][1], currleftheight)
                currrightheight = right[rightidx][1]
                x = right[rightidx][0]
                rightidx += 1
            # Case 3: The x-val pointed to by leftidx and rightidx are the same, so we take that point.
            # Note we must increment both indices, and since both graphs have changed height, the height is
            # just the maximum of the two heights.
            else:
                height = max(left[leftidx][1], right[rightidx][1])
                x = left[leftidx][0]
                currleftheight = left[leftidx][1]
                currrightheight = right[rightidx][1]
                leftidx += 1
                rightidx += 1

            # We only merge new slice on if the new point does not have same height as the previous point.
            # Otherwise, we have a redundant point in our skyline.
            # Ex.  merged_list = [[2, 1]]    new_point = [3, 1]
            #      This just extends a skyline of height one, so we don't add in [3,1] into our skyline.
            if len(merged_list) == 0 or merged_list[-1][1] != height:
                merged_list.append([x, height])
        # If left or right is not empty, merge rest of points onto end.
        if leftidx < len(left): merged_list.extend(left[leftidx: ])
        if rightidx < len(right): merged_list.extend(right[rightidx: ])
        return merged_list

    return helper(arr)

if __name__ == "__main__":
    print(get_skyline([[0,2,3],[2,5,3]]))