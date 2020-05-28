/** Nathan Zhu Saturday, May 23d, 2020 Stockton, CA. Watched lights out with Neha and Rak today.  Also went to apple store
 *  Leetcode 622 | medium | medium
 *  Oh yeah I had basically this problem for my optiver first round.  
 *  I was thinking really hard and messed this one up.
 * 
 *  The idea for this one actually is pretty simple.  Imagine a circular buffer, with two pointers, one at REMOVE position
 *  and one at INSERT position.  Insert keeps track of where we will insert next in the buffer.  Remove is where we will
 *  remove next in the buffer.
 * 
 *  [?   ?   ?]    INSERT REMOVE BOTH AT POSITION 0 INITIALLY
 *   INS
 *   REM
 * 
 *  [2   ?   ?]    INSERT 2 IN QUEUE, WE MOVE INSERT TO RIGHT
 *  REM INS
 *  
 *  [2   3   ?]    INSERT 3 IN QUEUE, WE MOVE INSERT TO RIGHT
 *  REM     INS
 * 
 *  [?  2   ?]     REMOVE 2 IN QUEUE, MOVE REMOVE TO RIGHT.
 *      REM  INS
*/     

#include <vector>

using namespace std; 

class MyCircularQueue {
private:
    int size;
    int k;
    vector<int> arr;
    int ins;
    int rem;
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        arr = vector<int>(k);
        this->k = k;
        size = 0;
        ins = rem = 0;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if(size == k) return false;
        arr[ins] = value;
        size++;
        ins = (ins + 1) % k;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if(size == 0) return false;
        size--;
        rem = (rem + 1) % k;
        return true;
    }
    
    /** Get the front item from the queue. */
    int Front() {
        if(size == 0) return -1;
        return arr[rem];
    }
    
    /** Get the last item from the queue. */
    int Rear() {
        if(size == 0) return -1;
        return arr[(ins - 1 + k) % k];   // watch for neg overflow in c++
    }
    
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return size == 0;
    }
    
    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return size == k;
    }
};
