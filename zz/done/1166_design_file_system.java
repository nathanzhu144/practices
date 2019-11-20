/* Saturday October 5th, 2019 11:43 am Design file system, in Uglu 4th floor week of Wolverine trading onsite.
*  Leetcode 1163 | medium | medium
* 
*  putIfAbsent & getOrDefault are cool functions.
*/

class FileSystem {
    Map<String, Integer> file;
    public FileSystem() {
        file = new HashMap<String, Integer>();
        file.put("", -1);
    }
    
    public boolean createPath(String path, int value) {
        int idx = path.lastIndexOf("/");
        String parent = path.substring(0, idx);
        
        // For example, we can't do /c/d if 
        // /c doesn't exist.
        if(!file.containsKey(parent)) return false;
        return file.putIfAbsent(path, value) == null;
    }
    
    public int get(String path) {
        return file.getOrDefault(path, -1);
    }
}