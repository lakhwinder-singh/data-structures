array_list = [7, 5, 2, 6, 9, 1, 0, 8]
print(array_list)


def sort_list(array_list, start, stop):
    if start >= stop:
        return
    p = partition(array_list, start, stop)
    sort_list(array_list, start, p - 1)
    sort_list(array_list, p + 1, stop)


def partition(array_list, start, stop):
    intended_position = start - 1
    pivot = array_list[stop]

    for i in range(start, stop):
        if pivot >= array_list[i]:
            intended_position += 1
            array_list[intended_position], array_list[i] = array_list[i], array_list[intended_position]

    array_list[intended_position + 1], array_list[stop] = array_list[stop], array_list[intended_position + 1]
    return intended_position + 1


def binary_search(array, elem):
    begin = 0
    end = len(array)-1
    level =0
    while begin <= end:
        level +=1
        mid = (begin+end)//2
        if elem == array[mid]:
            print('found at level '+str(level))
            return True
        elif elem < array[mid]:
            end = mid-1
        else:
            begin = mid+1
    return False




sort_list(array_list, 0, len(array_list) - 1)
print(array_list)
#
# x=int(input('Enter ''x'' you want to search : '))
# if not binary_search(array_list,x):
#     print('could not find element in the array')
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')