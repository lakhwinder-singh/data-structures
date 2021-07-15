class Node:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


def parse_nodes(head):
    node1 = head
    while True:
        node1 = node1.next
        print(node1.item)
        if node1.next == head_node.next:
            print('cyclic linked list')
            print('break')
            break


def create_new_node(head, item):
    node = Node(item)
    first_node = head.next
    if first_node is None:
        node.prev = node
        node.next = node
        head.next = node
        head.prev = node
    else:
        curr_last_node = first_node.prev
        node.next = first_node
        node.prev = first_node.prev
        curr_last_node.next = node
        first_node.prev = node


def delete_node(head, item):
    node1 = head
    while True:
        node1 = node1.next
        if node1.item == item:
            prev_node = node1.prev
            next_node = node1.next
            prev_node.next = next_node
            next_node.prev = prev_node
            print(str(node1.item) + ' deleted from list')
            break
        elif node1.next == head_node.next:
            print('cyclic linked list')
            print('break')
            break


# array_list = [8, 5, 2, 6, 9, 1, 0, 7]
head_node = Node(None)
# prev_node = head_node
# for i in array_list:
#     node = Node(i)
#     node.prev = prev_node
#     prev_node.next = node
#     prev_node = node
# node.next = head_node.next
# head_node.next.prev = node
# head_node.prev = head_node
# parse_nodes(head_node)
#
# x = int(input('How many numbers do you want to add? '))
# y = int(input('Enter starting point from the cyclic list: '))
#
# parse_node = head_node
# while True:
#     parse_node = parse_node.next
#     if parse_node.item == y:
#         head_node.next = parse_node
#         break
# sum = 0
# sum_node = head_node.next
# for i in range(x):
#     sum += sum_node.item
#     sum_node = sum_node.next
#
# print(sum)
# print('*awesomely done*')
# new_node = input('enter new node? T/F? ')
#
# if new_node == 'T' or new_node == 't':
#     item = int(input('enter item value '))
#     create_new_node(head_node, item)
#
# parse_nodes(head_node)

while True:
    print('Enter A for adding new node')
    print('Enter D for delete node')
    print('Enter P for Parsing or Viewing current list')
    x = input('Exit for any other input: ')

    if x == 'A' or x == 'a':
        print('You have chosen A : add/insert')
        i = int(input('Enter Item Value'))
        create_new_node(head_node, i)
    elif x == 'D' or x == 'd':
        print('You have chosen D : delete node')
        i = int(input('Enter Item Value you want to delete'))
        delete_node(head_node, i)
    elif x == 'P' or x == 'p':
        parse_nodes(head_node)
    else:
        print('Entered ' + x + ': which is not supported. Exiting')
        break
