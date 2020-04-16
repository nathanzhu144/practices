/** Nathan Zhu Jan 5th, 2020. 4:50 pm 481 class, sitting next to Mira. 
 *  Leetcode 1188 | medium | cool
 *  Category: Multithread
 *  
 *  Didn't know to use scopes to unlock locks.  This is cool.
*/


#include <condition_variable>
#include <mutex>
#include <thread>
#include <queue>
#include <shared_mutex>
#include <thread>

using namespace std;

class BoundedBlockingQueue {
private:
    condition_variable cv;
    mutex m;
    queue<int> q;
    int max_cap;
public:
    BoundedBlockingQueue(int capacity) {
        max_cap = capacity;
    }
    
    void enqueue(int element) {
        {
            unique_lock<mutex> lock1(m);
            
            cv.wait(lock1, [this]{ return q.size() < max_cap; });
            q.push(element);
        }
        
        // The state of the queue has changed.
        cv.notify_one();
    }
    
    int dequeue() {
        int ret = 0;
        {
            unique_lock<mutex> lock1(m);
            
            cv.wait(lock1, [this]{ return q.size() > 0; });
            ret = q.front();
            q.pop();
        }
        // The state of the queue has changed.
        cv.notify_one();
        return ret;
    }
    
    int size() {
        unique_lock<mutex> lock1(m);
        return q.size();
        
    }
};