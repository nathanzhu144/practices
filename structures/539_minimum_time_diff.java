
/** Nathan Zhu 
 *  Leetcode 539 | medium | medium
 *  Category: Design
 * 
 */

public int findMinDifference(List<String> timePoints) {
    boolean[] times = new boolean[24 * 60];
    for(String time : timePoints){
        String[] t = time.split(":");
        int h = Integer.parseInt(t[0]);
        int m = Integer.parseInt(t[1]);
        if(times[60 * h + m]) return 0;
        times[60 * h + m] = true;
    }
    
    int prevtime = 0, mindiff = Integer.MAX_VALUE;
    int first = Integer.MAX_VALUE, last = Integer.MIN_VALUE;
    
    for(int i = 0; i < 24 * 60; ++i){
        if(times[i]){
            if(first != Integer.MAX_VALUE){
                mindiff = Math.min(mindiff, i - prevtime);
            }
            first = Math.min(first, i);
            last = Math.max(last, i);
            prevtime = i;
        }
    }
    
    // Since time is a cycle, we want to find the "smallest"
    // time difference  and the "biggest" time difference.
    return Math.min(mindiff, (24 * 60 - last + first));
}