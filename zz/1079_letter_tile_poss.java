    // Nathan Zhu Sunday sept 29th, 2019. 12:26 pm Foundry, First Java program that's real dude.
    // Leetcode 1079 | medium | medium
    // Category: Backtracking/permutations
    
    /**
    This solution is genius man - 
    Insights: 
    - Most important thing is knowing the count of characters
      order doesn't matter for permutations
      However, duplicate characters can cause problems for us
      
      So, what we do is we can sort the word, and if we
      use a character, and next char is same, we don't use it
      
      OR 
      
      Have a "visited" set of strings
      
      OR
      
      We do it *this* way.
      
      We have an array of size 26, each with the count of 
      a corresponding letter in the alphabet.  We check to 
      see if a bucket is 0 (if we are out of those letters)
      and if it is 1, we can choose to take it and move
      to the next bucket.

       w
    */
    public int numTilePossibilities(String tiles) {
        int[] count = new int[26];
        for (char c : tiles.toCharArray()) count[c - 'A']++;
        return dfs(count);
    }
    
    int dfs(int[] arr){
        int sum = 0;
        for(int i = 0; i < 26; ++i){
            if(arr[i] == 0) continue;
            sum++;
            arr[i]--;
            sum += dfs(arr);
            arr[i]++;
        }
        
        return sum;
    }