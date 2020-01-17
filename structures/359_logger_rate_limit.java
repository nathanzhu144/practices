/** Nathan Zhu
 *  Leetcode 359 | medium | medium (tricky)
 *  Category: Design.
 * 
 */

// Idea here is we have 2 categories:
// Assumption:
//   - all timestamps are increasing
//
// Datastructures.
// 1. We have some buckets, each of the buckets at idx timestamp % 10 has timestamp.
// 2. We have a set associated with each bucket, containing all the messages with that timestamp.
//
// Way it works.
//    Suppose we find that we look inside the bucket and we find the timestamp doesn't
//    match our timestamp.  More than 10 seconds have passed for all messages in that bucket
//    so we don't need to keep track of any of them anymore.  We clear the set, and replace
//    the bucket at idx timestamp % 10 with our new timestamp.
//
//    Suppose we look at see that inside the bucket the timestamp matches our current
//    timestamp.  We shouldn't invalidiate that bucket because 10 seconds haven't passed yet.
//
//    We go through all the buckets representing the time in the last 10 seconds
//    and check to see if the message has been seen at all in the last 10 seconds.  
//    Some of the buckets we check may not be valid (their timestamp is more than 10 seconds
//    away from our current time), so we need an if statement for that.
//
//    
// 2. 
class Logger {
    private int[] buckets;
    private Set[] sets;
    
    
    /** Initialize your data structure here. */
    public Logger() {
        buckets = new int[10];
        sets = new Set[10];
        
        for(int i = 0; i < sets.length; ++i){
            sets[i] = new HashSet<String>();
        }
    }
    
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    public boolean shouldPrintMessage(int timestamp, String message) {
        int idx = timestamp % 10;
        
        if(timestamp != buckets[idx]){
            sets[idx].clear();
            buckets[idx] = timestamp;
        }
        
        for(int i = 0; i < buckets.length; ++i){
            if(timestamp - buckets[i] < 10){
                if(sets[i].contains(message)) return false;
            }
        }
        
        sets[idx].add(message);
        return true;
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean para