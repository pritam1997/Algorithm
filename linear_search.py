def linear_search(sequence, item):
    for i in range(len(sequence)):
        if sequence[i] == item:
            return i
    return None

a = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
item = 42

print(linear_search(a, item))

