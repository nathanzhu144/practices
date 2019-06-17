def pyramidTransition(bottom, allowed):
    """
    :type bottom: str
    :type allowed: List[str]
    :rtype: bool
    """
    
    allowed_dict = {}
    
    for i in allowed: 
        key = (i[0], i[1])
        if key in allowed_dict:
            allowed_dict[key].append(i[2])
        else:
            allowed_dict[key] = i[2]
            
    layer = list(bottom)
    
    def helper(layer, allowed_dict, visited):
        if len(layer) == 1:
            return True
        
        if tuple(layer) in visited:
            return False
    
        for i in range(len(layer) - 1):
            key = (layer[i], layer[i + 1])
            if key in allowed_dict:
                poss_replacements = allowed_dict[key]

                for rep in poss_replacements:
                new_layer = layer[:]
                new_layer[i] = rep
                new_layer.pop(i + 1)
                    
                if helper(new_layer, allowed_dict, visited):
                    return True
            else:
                continue

    
                    
        visited[tuple(layer)] = False
        return visited[tuple(layer)]
    
    return helper(layer, allowed_dict, {})


if __name__ == "__main__":
    pyramidTransition("ABC", ["ABD","BCE","DEF","FFF"])