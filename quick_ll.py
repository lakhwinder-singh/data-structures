class Node:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

    def add_node(self, item):
        node = Node(item)
        root = self
        root.prev = node
        if root.next is None:
            root.next = node
        else:
            next_node = root.next
            while next_node.next is not None:
                next_node = next_node.next
            next_node.next = node
            node.prev = next_node

    def parse_nodes(self):
        next_node = self.next
        while next_node.next is not None:
            print(next_node.item)
            next_node = next_node.next
        print(next_node.item)

    def parse_nodes_reverse(self):
        next_node = self.prev
        while next_node.prev is not None:
            print(next_node.item)
            next_node = next_node.prev
        print(next_node.item)

    def get_last_node(self):
        return self.prev

    def get_first_node(self):
        return self.next

    def delete_node(self, item):
        root = self
        first_node = root.next
        last_node = root.prev
        if first_node.item == item:
            if first_node == last_node:
                root.prev = root.next = None
            else:
                root.next = first_node.next
                first_node.next = None
            return
        if last_node.item == item:
            if first_node == last_node:
                root.prev = root.next = None
            else:
                root.prev = last_node.prev
                last_node.prev = None
            return
        node = root.next
        while node.next is not None:
            if node.item == item:
                next_node = node.next
                prev_node = node.prev
                prev_node.next = next_node
                next_node.prev = prev_node
                return
            node = node.next
        return

    def push(self, item):
        self.add_node(item)

    def pop(self):
        item = None
        node = self.get_last_node()
        if node is not None:
            item = node.item
            # self.prev = node.prev
            self.delete_node(item)
        if item is None:
            print('empty stack')
        else:
            print(item)
        return item

    def enqueue(self, item):
        self.add_node(item)

    def dequeue(self):
        item = None
        node = self.get_first_node()
        if node is not None:
            item = node.item
            self.next = node.next
        if item is None:
            print('empty queue')
        else:
            print(item)
        return item


if __name__ == '__main__':
    # head = Node(None)
    # head.add_node(1)
    # head.add_node(2)
    # head.add_node(3)
    # head.parse_nodes()
    # head.delete_node(2)
    # head.parse_nodes()
    # head.add_node(5)
    # head.parse_nodes()
    print('stack starts now')
    print('****************')
    stack = Node(None)
    stack.push(3)
    stack.push(5)
    stack.push(7)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.push(9)
    stack.pop()
    stack.pop()
    print('queue starts now')
    print('****************')
    queue = Node(None)
    queue.enqueue(2)
    queue.enqueue(4)
    queue.enqueue(6)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(8)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
