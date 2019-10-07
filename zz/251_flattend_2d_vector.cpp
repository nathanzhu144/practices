/* Nathan Zhu Sunday 12:39 pm Oct 6th, 2019
   Leetcode 251 | med | med
   
   Category: Design question
             Flatten 2d vector.
*/

#include <vector>

using namespace std;

class Vector2D {
private:
    vector<vector<int>>::iterator outercurr;
    vector<vector<int>>::iterator outerend;
    vector<int>::iterator inner;     
public:
    Vector2D(vector<vector<int>>& v) {
        outercurr = v.begin();
        outerend = v.end();

        // We check to see if outercurr is actually valid.
        if(outercurr != outerend) inner = v.begin()->begin();
    }
    
    int next() {
        hasNext();   // If we have reached the end of the current vector
                     // hasNext() should move us to next valid vector.
        int ret = *inner;
        inner++;
        return ret;
    }
    
    bool hasNext() {
        while(outercurr != outerend && inner == outercurr->end()){
            ++outercurr;
            // Don't deref this if this list is empty.
            if(outercurr != outerend) 
                inner = outercurr->begin();
        }
        
        return outercurr != outerend;
    }
};
