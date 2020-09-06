
/* Nathan Zhu  Monday July 20th, 2020 10:40 pm Stockton, CA.  Emailed Katie & Jaewon today.
*  Leetcode 641 | medium | edge cases, but Ok.  annoying under pressure
*  Category: Design
*/

#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <string>
#include <queue>
#include <deque>
#include <utility>
#include <algorithm>
#include <cmath>
#include <limits>
#include <iostream>

using namespace std;

// //  7  0  0  0  0
//     0  1  2  3  4
//     F

class MyCircularDeque {
private:
    vector<int> arr;
    int front;
    int back;
    int currsize;
    int maxsize;
public:
    /** Initialize your data structure here. Set the size of the deque to be k. */
    MyCircularDeque(int k) {
        front = 0;
        back = 1;
        currsize = 0;
        maxsize = k; 
        arr = vector<int>(k, 0);
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    bool insertFront(int value) {
        if(currsize == maxsize) return false;
        arr[front] = value;
        front = (front - 1 + maxsize) % maxsize;
        ++currsize;
        return true;
    }
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    bool insertLast(int value) {
        if(currsize == maxsize) return false;
        arr[back] = value;
        back = (back + 1) % maxsize;
        ++currsize;
        return true;
    }
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    bool deleteFront() {
        if(currsize == 0) return false;
        front = (front + 1) % maxsize;
        --currsize;
        return true;
    }
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    bool deleteLast() {
        if(currsize == 0) return false;
        back = (back - 1 + maxsize) % maxsize;
        --currsize;
        return true;
    }
    
    /** Get the front item from the deque. */
    int getFront() {
        if(!currsize) return -1;
        return arr[(front + 1 + maxsize) % maxsize];
    }
    
    /** Get the last item from the deque. */
    int getRear() {
        if(!currsize) return -1;
        return arr[(back - 1 + maxsize) % maxsize];
    }
    
    /** Checks whether the circular deque is empty or not. */
    bool isEmpty() {
        return currsize == 0;
    }
    
    /** Checks whether the circular deque is full or not. */
    bool isFull() {
        return currsize == maxsize;
    }
};