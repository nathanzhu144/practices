/**
 * Nathan Zhu 
 * Leetcode 706 | easy | EZ
 * Category: Design.
 */

class MyHashMap {
    private static final double LOAD_FACTOR = 0.75;
    private Node[] nodes;
    private int size;

    /** Initialize your data structure here. */
    public MyHashMap() {
        nodes = new Node[5];
        size = 0;
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        int idx = hash(key);
        
        for(Node n = nodes[idx]; n != null; n = n.next){
            if(n.key == key){
                n.value = value;
                return;
            }
        }
        
        nodes[idx] = new Node(key, value, nodes[idx]);
        size++;
        
        if(size / nodes.length > LOAD_FACTOR) rehash();
        
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        int idx = hash(key);
        
        for(Node n = nodes[idx]; n != null; n = n.next)
            if(n.key == key) return n.value;
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        int idx = hash(key);
        
        Node pre = new Node(-1, -1, nodes[idx]);  // sentinal node before head
        for(Node prev = pre; prev.next != null; prev = prev.next){
            if(prev.next.key == key){
                prev.next = prev.next.next;
                break;
            }
        }
        nodes[idx] = pre.next;  // This is in case we remove head, we need to re-assign
                                // correct head to the bucket.
        size--;
    }
    
    private int hash(int key){
        return key % nodes.length;
    }
    
    private void rehash(){
        Node[] tmp = nodes;
        nodes = new Node[tmp.length * 2];
        size = 0;
        
        for(Node head : tmp){
            for(Node x = head; x != null; x = x.next){
                put(x.key, x.value);
            }
        }
    }
    
    class Node{
        int key;
        int value;
        Node next;
        
        public Node(int key, int value, Node next){
            this.key = key;
            this.value = value;
            this.next = next;
        }
    }
}

class Node{
    
}
/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */