# Nathan Zhu EHS 55 John Street 9:14 am, August 5th, 2019. 
#            Stockton, CA March 23rd, 2020 4:50 pm 
# Leetcode 210 | medium | medium
# Category: Topological sort
# 
# Similar problems: course schedule I

def findOrder(self, numcourses, prereq):
    # outdegrees acts like a map from a course -> courses it is a prereq for
    # indegrees is number of courses that lead to this course
    outdeg = [0] * numcourses

    # indegree is which nodes lead to this node
    indegree = [[] for i in range(numcourses)]
    
    # format: [[1, 0]]
    # course 0 leads to course 1
    for i in range(len(prereq)):
        outdeg[prereq[i][0]] += 1
        indegree[prereq[i][1]].append(prereq[i][0])
        
    course_order = []
    for i in range(numcourses):
        if outdeg[i] == 0: course_order.append(i)
    
    # Here's the real logic.
    # This code is actually genius.
    # So, there are 2 things about course_order that are important:
    # 1. When we add a course to course_order, we can take that course.
    # 2. By taking that course, we can possibly take more courses, so
    #    we inspect all the courses that this course is a prerequisite for
    #    we decrease their number of prerreq by 1, and check if they have 0 more
    #    prerequisites.  If they have 0 more prerequisites, we take this class.
    # 3. We only need to look at the last index of course_order. We have looked
    #    at the previous elements in courseorder to get to the courses we have taken by now.
    #
    l = 0
    while l != len(course_order):
        x = course_order[l]
        l += 1
        for i in range(len(indegree[x])):
            outdeg[indegree[x][i]] -= 1
            if outdeg[indegree[x][i]] == 0: course_order.append(indegree[x][i])

    if len(course_order) != numcourses: return []
        else: return course_order


if __name__ == "__main__":
    print(findOrder(2, [[1,0],[0,1]]))

#https://leetcode.com/problems/course-schedule-ii/discuss/190393/Topological-Sort-Template-General-Approach!!
