array_list = [8, 5, 2, 6, 9, 1, 0, 7]
print(array_list)

def partition(array_list, start, stop):
    pivot = array_list[stop]
    i = start - 1
    for j in range(start, stop):
        if array_list[j] <= pivot:
            i += 1
            (array_list[i], array_list[j]) = (array_list[j], array_list[i])

    (array_list[i + 1], array_list[stop]) = (array_list[stop], array_list[i + 1])

    return i + 1


def quick_sort(array_list, start, stop):
    if start < stop:
        pivot_position = partition(array_list, start, stop)

        quick_sort(array_list, start, pivot_position - 1)
        quick_sort(array_list, pivot_position + 1, stop)


quick_sort(array_list, 0, len(array_list) - 1)
print(array_list)
