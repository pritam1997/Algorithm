def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        mid_value = sequence[midpoint]
        if mid_value == item:
            return midpoint
        elif item < midpoint:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1
    return None


a = [12, 4, 6, 7, 7, 8, 4, 3, 3, 3, 5, 67, 9, 90, 2]
item_a = 3
print(binary_search(a, item_a))
