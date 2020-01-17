/* 
*  Nathan Zhu Saturday October 5th, 2019 11:16 am, week before CTC on-campus and wolverine on-site.
*  Leetcode 355 | medium | eehhh hard
*  This idea be genius yo.
*
*  Idea for this is each user has a linked list of posts.  
*  
*  Characteristics of the post linked list:
*  - Each post has a timestamp which is a static variable that is incremented everytime 
*    a post is created among any user.
*  - head of linked list if it exists is most recent (and has highest timestamp value in whole LL)
*
*
*  How Does this help us?
*  So out of the people we follow, we just want the 10 most recent posts.  We can make a PQ of size O(number people we follow)
*  instead of O(number of posts on all people we follow).  We know out of all the heads one of them has the highest timestamp
*  we want to add.  After we add the chosen head, if its next is valid, we add its next into the PQ.  
*
*  We have at most 10 insertions into the priorityqueue.

*/

class Twitter {
    private static int timestamp=0;
    
    private Map<Integer, User> userMap;
    
    private class Tweet{
        public int id;
        public int time;
        public Tweet next;
        
        public Tweet(int id){
            this.id = id;
            time = timestamp++;
            next = null;
        }
    }
    
    public class User{
        public int id;
        public Set<Integer> followed;
        public Tweet tweet_head;
        
        public User(int id){
            this.id = id;
            followed = new HashSet<>();
            follow(id);    // a user must follow themselves.
            tweet_head = null;
        }
        
        public void follow(int id){
            followed.add(id);
        }
        public void unfollow(int id){
            followed.remove(id);
        }
        
        public void post(int id){
            Tweet t = new Tweet(id);
            t.next = tweet_head;
            tweet_head = t;
        }
    }
    

    /** Initialize your data structure here. */
    public Twitter() {
        userMap = new HashMap<Integer, User>();
    }
    
    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        if(!userMap.containsKey(userId)){
            User u = new User(userId);
            userMap.put(userId, u);
        }
        userMap.get(userId).post(tweetId);
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    
    
    
    // Best part of this.
	// first get all tweets lists from one user including itself and all people it followed.
	// Second add all heads into a max heap. Every time we poll a tweet with 
	// largest time stamp from the heap, then we add its next tweet into the heap.
	// So after adding all heads we only need to add 9 tweets at most into this 
	// heap before we get the 10 most recent tweet.
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> res = new LinkedList<>();
        
        if(!userMap.containsKey(userId)) return res;
        
        Set<Integer> users = userMap.get(userId).followed;
        PriorityQueue<Tweet> q = new PriorityQueue<Tweet>(users.size(), (a,b)->(b.time - a.time));
        
        for(int user : users){
            Tweet t = userMap.get(user).tweet_head;
            
            // don't want to add null tweets into pq
            if(t != null) q.add(t);
        }
        
        int tweets_left = 10;
        while(!q.isEmpty() && tweets_left > 0){
            Tweet t = q.poll();
            res.add(t.id);
            tweets_left--;
            
            if(t.next != null) q.add(t.next);
        }
        
        return res;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        if(!userMap.containsKey(followerId)){
            User u = new User(followerId);
            userMap.put(followerId, u);
        }
        if(!userMap.containsKey(followeeId)){
            User u = new User(followeeId);
            userMap.put(followeeId, u);
        }
        userMap.get(followerId).follow(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
        if(!userMap.containsKey(followerId) || !userMap.containsKey(followeeId) || followerId == followeeId) return;
        
        userMap.get(followerId).unfollow(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */