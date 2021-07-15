class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict.keys():
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        vertex1, *vertex2 = tuple(edge)
        if len(vertex2) == 0:
            vertex2 = vertex1
        if vertex1 in self.graph_dict.keys():
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def generate_edges(self):
        edges = []
        for vertex in self.graph_dict.keys():
            for edge in self.graph_dict[vertex]:
                edges.append({vertex: edge})
        return edges

    def get_edges(self):
        return self.generate_edges()

    def get_node_edges(self, node):
        if node in self.graph_dict.keys():
            return self.graph_dict[node]
        else:
            return []

    def get_vertices(self):
        return list(self.graph_dict.keys())

    # def dfs(graph, start, visited=None):
    #     if visited is None:
    #         visited = set()
    #     visited.add(start)
    #     print(start)
    #     for next in set(list(graph[start])) - visited:
    #         dfs(graph, next, visited)
    #     return visited


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

    def check_node_exists(self, item):
        if self.next is not None:
            next_node = self.next
        else:
            return False
        while next_node.next is not None:
            if next_node.item == item:
                return True
            next_node = next_node.next
        if next_node.item == item:
            return True
        else:
            return False

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
                root.prev.next = None
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
        if not self.check_node_exists(item):
            self.add_node(item)

    def pop(self):
        item = None
        node = self.get_last_node()
        if node is not None:
            item = node.item
            # self.prev = node.prev
            self.delete_node(item)
        # if item is None:
        #     print('empty stack')
        # else:
        # print(item)
        return item

    def enqueue(self, item):
        if not self.check_node_exists(item):
            self.add_node(item)

    def dequeue(self):
        item = None
        node = self.get_first_node()
        if node is not None:
            item = node.item
            self.next = node.next
        # if item is None:
        #     print('empty queue')
        # else:
        # print(item)
        return item


def dfs(graph, stack, visited=None):
    vertex = stack.pop()
    if visited is None:
        visited = set()
    if vertex is None:
        return
    visited.add(vertex)
    print('visiting vertex :' + str(vertex))
    child_nodes = graph.get_node_edges(vertex)
    elig_children = child_nodes - visited
    for child in elig_children:
        stack.push(child)
    dfs(graph, stack, visited)


def bfs(graph, queue, visited=None):
    vertex = queue.dequeue()
    if visited is None:
        visited = set()
    if vertex is None:
        return
    visited.add(vertex)
    print('visiting vertex :' + str(vertex))
    child_nodes = graph.get_node_edges(vertex)
    elig_children = child_nodes - visited
    for child in elig_children:
        queue.enqueue(child)
    bfs(graph, queue, visited)


if __name__ == "__main__":
    g = {'0': set(['1', '2', '3']),
         '1': set(['0', '2']),
         '2': set(['0', '1', '4']),
         '3': set(['0']),
         '4': set(['2'])}
    # g1 = { 'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': [],
    #     'E': ['F'],
    #     'F': []
    #    }
    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.get_vertices())

    print("Edges of graph:")
    print(graph.get_edges())

    stack = Node(None)
    stack.push('4')
    dfs(graph, stack)
    print('bfs now')
    print('***************************')
    queue = Node(None)
    queue.enqueue('0')
    bfs(graph, queue)
