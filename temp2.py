import math
import collections      
def number_tiles(tiles):
    # since we sorted tiles, any substring of tiles will be sorted
    tiles = sorted(tiles)
    visited = set()
    
    def helper(tiles, visited):
        if not tiles: return 0
        if tiles in visited: return 0
        visited.add(tiles)
        # possible sequences = n! / 
        
        tiles_count = collections.defaultdict(lambda: 0)
        ret = 0
        for i in range(len(tiles)):
            ret += helper(tiles[:i] + tiles[i + 1:], visited)
            tiles_count[tiles[i]] += 1
            
        # Let's calculate total permutations of current tiles
        curr_string_perm = math.factorial(len(tiles))
        for key in tiles_count: curr_string_perm /= math.factorial(tiles_count[key])
        
        return ret + curr_string_perm
    
    return helper(tiles, visited)

if __name__ == "__main__":
    print(number_tiles("AA"))