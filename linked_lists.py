class Node:
    def __init__(self, data=None) -> None:
        self.value = data
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data):
        if not isinstance(data, Node):
            new_node = Node(data)
        else:
            new_node = data

        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        current_node = self.head
        idx = 0
        while current_node.next != None:
            idx += 1
            current_node = current_node.next
        return idx

    def __str__(self):
        elements = ''
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements += str(current_node) + ' -> '
        elements += 'None'
        return elements

    def reorder_list(self):
        pass
