class BinarySearchTree:
    class __Node:
        def __init__(self, item, left=None, right=None):
            self.item = item
            self.left = left
            self.right = right

        def getItem(self):
            return self.item

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setItem(self, item):
            self.item = item

        def setLeft(self, left):
            self.left = left

        def setRight(self, right):
            self.right = right

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.item

            if self.right != None:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None

    def insert(self, item):

        def __insert(root, item):
            if root is None:
                return BinarySearchTree.__Node(item)
            if item < root.getItem():
                root.setLeft(__insert(root.getLeft(), item))
            else:
                root.setRight(__insert(root.getRight(), item))
            return root

        self.root = __insert(self.root, item)

    def __iter__(self):
        if self.root is not None:
            return self.root.__iter__()
        else:
            return [].__iter__()


def main():
    s = input('enter list of string ')
    x_lst = s.split(',')
    tree = BinarySearchTree()

    for i in x_lst:
        if i != '':
            tree.insert(int(i))
    for i in tree:
        print(i)


if __name__ == "__main__":
    main()

