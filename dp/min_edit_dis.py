

def helper(source, dest, source_index, dest_index):
    if source_index < 0 or dest_index < 0:
        return source_index < 0 and dest_index < 0

    if source[source_index] == '.' or source[source_index] == dest[dest_index]
        return helper(source, dest, source_index - 1, dest_index - 1)
    
    if source[source_index] == '*':
        if source[source_index - 1] == '.' or source[source_index - 1] == dest[dest_index]:
            
        while source_index != -2:
            return helper(source, dest, source_index - 1, dest)