
class TreeNode(object):
    def __init__(self, data=None) -> None:
        self.value = data
        self.left = None
        self.right = None

    def __eq__(self, other) -> bool:
        if isinstance(other, TreeNode):
            if self.value == other.value:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, TreeNode):
            return self.value < other.value
        return False

    def __gt__(self, other):
        if isinstance(other, TreeNode):
            return self.value > other.value
        return False

    def __str__(self):
        string = ' '.join([str(self.value), str(self.left), str(self.right)])
        return string

    def insert(self, node):
        if not isinstance(node, TreeNode):
            new_node = TreeNode(node)
        else:
            new_node = node

        if self.value is None:
            self.value = new_node.value
        else:
            if new_node.value < self.value:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(new_node)
            elif new_node.value > self.value:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(new_node)

    def invert(self, root):
        # DFS
        if not root:
            return None
        else:
            tmp = root.left
            root.left = root.right
            self.right = tmp
            self.invert(root.left)
            self.invert(root.right)
            return root
