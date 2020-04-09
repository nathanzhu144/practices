# Nathan Zhu EHS 55 John Street 9:14 am, August 5th, 2019. 
#            Stockton, CA March 23rd, 2020 4:50 pm 
# Leetcode 207 | medium | medium
# Category: Topological sort
# 
# Similar problems: course schedule II
# 
    
def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    #indegree is number of courses going into that node
    #outdegree is courses that lead out of that courses
    indegree = [0] * numCourses
    outdegree = collections.defaultdict(list)
    for pair in prerequisites:
        course, prereq = pair
        indegree[course] += 1
        outdegree[prereq].append(course)
        
    # we can only start by taking of of the courses with no prereq
    ans = []
    for i in range(numCourses):
        if indegree[i] == 0: ans.append(i)
    
    # we go through the courses that we can take currently,
    # see if that "unlocks" new courses.  End loop when we 
    # cannot take any new courses
    idx = 0
    while idx < len(ans):
        for course in outdegree[ans[idx]]:
            indegree[course] -= 1
            if indegree[course] == 0: ans.append(course)
        idx += 1
        
    # See if we take all the courses
    return len(ans) == numCourses
