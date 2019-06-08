

def helper(list, index):

    if len(list) == 3:
        return list[0] * list[1] * list[2]

    if index < 0:
        return float('Inf')

    newlist = list.pop(index + 1)
    return min(list[index] * list[index + 1] * list[index + 2] * helper(newlist, index - 1), helper(list, index - 1))

def matrix_mult(list):
    return helper(list, len(list) - 3)


if __name__ == "__main__":
    print(matrix_mult([1, 2, 3, 4, 3]))