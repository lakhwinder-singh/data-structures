array_list = [8, 5, 2, 6, 9, 1, 0, 7]
print(array_list)


def partition(array, start, stop):
    pivot = array[stop]
    i = start - 1
    j = stop - 1
    for k in range(start, stop):
        if array[k] <= pivot:
            i += 1
            (array[k], array[i]) = (array[i], array[k])

    (array[i + 1], array[stop]) = (array[stop], array[i + 1])
    return i + 1


def list_sort(array, start, stop):
    if start >= stop:
        return

    p = partition(array, start, stop)

    list_sort(array, start, p - 1)
    list_sort(array, p + 1, stop)


list_sort(array_list, 0, len(array_list) - 1)
print(array_list)

x = int(input('Enter the number of which you want to find highest sum: '))
sum = 0
for k in range(len(array_list) - 1, len(array_list) - 1 - x, -1):
    sum += array_list[k]
print(sum)
