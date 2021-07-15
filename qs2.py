array_list = [5, 8, 2, 6, 9, 1, 0, 7]
print(array_list)


def partition(arraylist, start, stop):
    pivot_elem = array_list[stop]
    intended_pos = start - 1
    for i in range(start, stop):
        if pivot_elem >= arraylist[i]:
            intended_pos += 1
            (arraylist[intended_pos], arraylist[i]) = (arraylist[i], arraylist[intended_pos])

    (arraylist[intended_pos + 1], arraylist[stop]) = (arraylist[stop], arraylist[intended_pos + 1])

    return intended_pos+1


def quicksort(arraylist, start, stop):
    if start < stop:
        pivot_pos = partition(arraylist, start, stop)

        quicksort(arraylist, start, pivot_pos - 1)
        quicksort(arraylist, pivot_pos + 1, stop)


quicksort(array_list, 0, len(array_list) - 1)
print(array_list)