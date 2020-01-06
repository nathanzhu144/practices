/**
 * Nathan Zhu January 4th, 2019 8:14 pm
 * Leetcode 284 | medium | kinda hard to think of.
 * 
 * The idea is that a peeking iterator calls next, and stores it temporarily.
*/

#include <vector>

using namespace std;

class Iterator {
    struct Data;
	Data* data;
public:
	Iterator(const vector<int>& nums);
	Iterator(const Iterator& iter);
	virtual ~Iterator();
	// Returns the next element in the iteration.
	int next();
	// Returns true if the iteration has more elements.
	bool hasNext() const;
};


class PeekingIterator : public Iterator {
    int m_next;
    bool m_hasnext; 
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    m_hasnext = Iterator::hasNext();
        if(m_hasnext) m_next = Iterator::next();
	}

    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        return m_next;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    int ret = m_next;
        m_hasnext = Iterator::hasNext();
        if(m_hasnext) m_next = Iterator::next();
        return ret;
	}

	bool hasNext() const {
	    return m_hasnext;
	}
};