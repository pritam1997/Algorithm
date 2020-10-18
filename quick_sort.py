def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item < pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


a = [12, 4, 6, 7, 7, 8, 4, 3, 3, 3, 5, 67, 9, 90, 2]
print(quick_sort(a))
