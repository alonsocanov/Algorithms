from requests import head


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
        # find middle of list
        slow, fast = self.head, self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = self.head, prev
        while second:
            tmp_1, tmp_2 = first.next, second.next
            first.next = second
            second.next = tmp_1
            first, second = tmp_1, tmp_2
