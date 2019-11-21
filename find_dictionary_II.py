# Nathan Zhu 9:28 pm, On plane over Lake Michigan from Chicago to New York.
# 
# This is a very simple backtracking problem.
#

def word_search_II(board, dictionary):
    # returns true if word exists at board[i][j]
    def helper(board, row, col, word, word_idx, visited):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) \
            or (row, col) in visited or board[row][col] != word[word_idx]:
            return False
        
        # We know board[row][col == last char of word, so we have found whole word
        if word_idx + 1 == len(word): return True
        
        ret = False
        visited.add((row, col))
        ret = ret or helper(board, row + 1, col, word, word_idx + 1, visited)
        ret = ret or helper(board, row - 1, col, word, word_idx + 1, visited)
        ret = ret or helper(board, row, col + 1, word, word_idx + 1, visited)
        ret = ret or helper(board, row, col - 1, word, word_idx + 1, visited)
        visited.remove((row, col))

        return ret
    
    ret_words = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            for word in dictionary:
                if helper(board, row, col, word, 0, set()):
                    ret_words.append(word)
                    dictionary.remove(word)   # we don't need to look for this word again

    return ret_words

