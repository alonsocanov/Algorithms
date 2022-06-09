
class Node(object):
    def __init__(self, data=None) -> None:
        self.value = data
        self.left = None
        self.right = None

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            if self.value == other.value:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.value < other.value
        return False

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.value > other.value
        return False


class Tree(object):
    def __init__(self, node=Node()) -> None:
        self.head = node

    def insert(self, node):
        if not isinstance(node, Node):
            new_node = Node(node)
        else:
            new_node = node

        if self.head == Node():
            self.head = node
        else:
            curr = self.head
            if new_node > curr:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.add(new_node)
            elif new_node < curr:
                if self.right in None:
                    self.right = new_node
                else:
                    self.right.add(new_node)

    def __str__(self):
        pass


tree = Tree()
tree.insert(10)
tree.insert(40)
tree.insert(5)
