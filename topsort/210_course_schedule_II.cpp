/* Nathan Zhu May 14th, 2020. 3:41 am, Stockton, CA.  Called Hershal yesterday, about how we might not be able to see each other next sem.  Big sad man
*                                                     We also picked cherries yesterday, but they weren't ripe.  Starting salesforce in four days~
*  Leetcode 210 | medium | not bad
*  Category: Topological sort
*/

using namespace std;
#include <vector>
#include <unordered_map>
#include <unordered_set>
// Questions I'd ask:
// 1. Are there duplicates, not in this case.

vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    vector<int> ret;
    unordered_map<int, unordered_set<int>> prereqs;   // postreq -> list of preqreq
    unordered_map<int, unordered_set<int>> postreqs;  // prereq  -> list of postreq, postreq is a 
                                            // course with this preqreq
    int N(numCourses);
    
    for(auto& vec : prerequisites){
        int pre(vec[1]), post(vec[0]);
        prereqs[post].insert(pre);
        postreqs[pre].insert(post);
    }
    
    for(int i = 0; i < N; ++i){
        if(!prereqs.count(i)) prereqs[i];  // make an empty list
    }
    
    while(N--){
        vector<int> taken;
        
        for(auto& [post, prereq_list] : prereqs){
            if(prereq_list.empty()){
                ret.push_back(post);        // we can now take this course
                taken.push_back(post);      // store this course, validate courses w this course as aprereq
            }
        }
        
        for(auto taken_course: taken){
            prereqs.erase(taken_course);     // ensures no double add for course
            for(auto nextc : postreqs[taken_course]){
                prereqs[nextc].erase(taken_course);
            }
        }
    }
    
    return (ret.size() == numCourses) ? ret : vector<int>();
}