array_list = [8, 5, 2, 6, 9, 1, 0, 7]
print(array_list)


def sort_list(array_list, start, stop):
    if start >= stop - 1:
        return None
    mid = start + ((stop - start) // 2)
    sort_list(array_list, start, mid)
    sort_list(array_list, mid, stop)
    merge_list(array_list, start, mid, stop)


def merge_list(array_list, start, mid, stop):
    i = start
    j = mid
    lst = []
    while i < mid and j < stop:
        if array_list[i] < array_list[j]:
            lst.append(array_list[i])
            i += 1
        else:
            lst.append(array_list[j])
            j += 1
    while i < mid:
        lst.append(array_list[i])
        i += 1

    for k in range(len(lst)):
        array_list[start + k] = lst[k]


sort_list(array_list, 0, len(array_list))
print(array_list)
