def selection_sort(list_a):
    index_length = range(0, len(list_a) - 1)

    for i in index_length:
        min_value = i

        for j in range(i + 1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

        if list_a[i] > list_a[min_value]:
            list_a[i], list_a[min_value] = list_a[min_value], list_a[i]
    return list_a


a = [4, 6, 2, 8, 7]
print(selection_sort(a))

'''
def selection_sort(list_a):
    index_length = len(list_a) - 1
    sorted = False
    min = list_a[0]

    while not sorted:
        sorted = True
        for i in range(list_a.index(min), index_length):
            for j in range(i + 1, len(list_a)):
                if list_a[i] > list_a[j]:
                    min = list_a[j]
                    list_a[i], list_a[j] = list_a[j], list_a[i]
                    sorted = False
                    break
    return list_a


a = [4, 6, 2, 8, 7]
print(selection_sort(a))
'''
