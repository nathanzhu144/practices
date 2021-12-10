# Nathan Zhu, 12/10/2021, 3 pm, Starbucks, Stockton, CA
# Leetcode 2050 | hard | fun
# Category: topological sort with a twist!

import collections

# Optimizations:
# We don't need to iterate through all keys in course_to_prereq every time to find
# courses we can take.  We can keep an additional data structure to track all
# courses with 0 dependencies in the beginning.  Everytime, we finish all dependencies
# of a course, we can add it to this data structure.
#
def minimumTime(n, relations, time):
    """
    :type n: int
    :type relations: List[List[int]]
    :type time: List[int]
    :rtype: int
    """
    # Note we are guaranteed a solution.
    course_to_prereq, prereq_to_course = collections.Counter(), collections.defaultdict(list)
    course_finished_time = collections.Counter()
    for i in range(1, n + 1):
        course_to_prereq[i] = 0
    for a, b in relations:
        prereq_to_course[a].append(b)
        course_to_prereq[b] += 1
    
    course_can_take = list()
    ret = 0
    
    for c, prereqs in course_to_prereq.items():
        if not prereqs: course_can_take.append(c)
            
    while len(course_to_prereq):
        new_course_can_take = []
        del_course = set()
        for finished_course in course_can_take:
            # calculated time is total time it takes to finish this course
            course_finished_time[finished_course] += time[finished_course - 1]
            ret = max(ret, course_finished_time[finished_course])
            for potential_new_course in prereq_to_course[finished_course]:
                course_to_prereq[potential_new_course] -= 1
                
                # this new couse is takeable now
                if course_to_prereq[potential_new_course] == 0:
                    new_course_can_take.append(potential_new_course)
                    
                # if multiple edges lead into this node, we want to carry in the largest cost
                course_finished_time[potential_new_course] = max(course_finished_time[potential_new_course], course_finished_time[finished_course])
            del_course.add(finished_course)
        for course in del_course:
            del course_to_prereq[course]
        course_can_take = new_course_can_take
    return ret
                

def minimumTimeUnoptimized(n, relations, time):
    """
    :type n: int
    :type relations: List[List[int]]
    :type time: List[int]
    :rtype: int
    """
    # Note we are guaranteed a solution.
    course_to_prereq, prereq_to_course = collections.defaultdict(set), collections.defaultdict(list)
    course_finished_time = collections.Counter()
    for i in range(1, n + 1):
        course_to_prereq[i]
    for a, b in relations:
        prereq_to_course[a].append(b)
        course_to_prereq[b].add(a)
        
    ret = 0
    while len(course_to_prereq):
        del_course = set()
        for course, prereqs in course_to_prereq.items():
            if not prereqs:
                finished_course = course
                # calculated time is total time it takes to finish this course
                course_finished_time[finished_course] += time[finished_course - 1]
                ret = max(ret, course_finished_time[finished_course])
                for potential_new_course in prereq_to_course[finished_course]:
                    course_to_prereq[potential_new_course].remove(finished_course)
                    course_finished_time[potential_new_course] = max(course_finished_time[potential_new_course], course_finished_time[finished_course])
                del_course.add(finished_course)
        for course in del_course:
            del course_to_prereq[course]
    return ret