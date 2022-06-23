
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
        string = ""
        if self.value:
            string += str(self.value) + '-'
        if self.left:
            string += str(self.left) + '-'
        if self.right:
            string += str(self.right) + '-'
        return string

    def __add__(self, other):
        if isinstance(other, TreeNode):
            return self.value + other.value
        return 0

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

    def validate(self, root):
        # BST recursive
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))

    def max_depth_recursive_dfs(self):
        if not self.value:
            return 0

        return 1 + max(self.max_depth_recursive_dfs(self.left), self.max_depth_recursive_dfs(self.right))

    def max_depth_bfs(self):
        if not self.value:
            return 0
        level = 0
        q = [self.left, self.right]
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    def max_depth_dfs(self):
        # stack (iterative)
        if not self.value:
            return 0
        stack = [[self.left, 1], [self.right, 1]]
        res = 1
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

    def diameter(self):
        '''
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
        '''
        if not self.value:
            return -1
        res = [0]

        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(node)
        return res[0]

    def max_path_sum(self):
        # dfs
        if not self.value:
            return 0
        stack = [self.left, self.right]
        res = 0
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                l_max = 0
                if node.left:
                    l_max = max(node.left, 0)
                r_max = 0
                if node.right:
                    r_max = max(node.right, 0)
                res = max(res, node + l_max + r_max)
        return res


if __name__ == '__main__':
    print("\nTest Tree")
    tree = TreeNode()
    tree.insert(10)
    tree.insert(40)
    tree.insert(5)
    tree.insert(20)
    tree.insert(4)
    print('The tree is:', tree)
    depth = tree.max_depth_bfs()
    print("The max depth is:", depth)
    depth = tree.max_depth_dfs()
    print("The max depth is:", depth)
    max_path = tree.max_path_sum()
    print("the max is path sum is:", max_path)

    inv_tree = tree.invert(tree)
    print('The tree inverted is:', inv_tree)
