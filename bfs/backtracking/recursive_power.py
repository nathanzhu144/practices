

def recursivepower(base, pow):
    if pow == 0:
        return 1

    return base * recursivepower(base, pow - 1)


print(recursivepower(2, 0))
print(recursivepower(2, 5))