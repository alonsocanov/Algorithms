
class Node(object):
    def __init__(self, data=None) -> None:
        self.value = data
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            if other.value == self.value:
                return True
        return False


class LinkedList(object):
    def __init__(self, data=Node()) -> None:
        if not isinstance(data, Node):
            node = Node(data)
        else:
            node = data
        self.head = node

    def append(self, data):
        if not isinstance(data, Node):
            new_node = Node(data)
        else:
            new_node = data
        if self.head == Node():
            self.head = new_node
        else:
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
        while current_node != None:
            elements += str(current_node) + ' -> '
            current_node = current_node.next
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

    def remove(self, ind):
        if ind < 0:
            dummy = LinkedList()
            dummy.head.next = self.head
            left = dummy
            right = self.head
            abs_n = abs(ind)
            while abs_n > 0 and right:
                right = right.next
                abs_n -= 1

            while right:
                left = left.next
                right = right.next
            # delete
            left.next = left.next.next
            return dummy.next
        else:
            dummy = LinkedList()
            dummy.head.next = self.head
            i = 0
            curr = self.head
            while i < ind:
                curr = curr.next
                i += 1

    def intersection(self, list_2):
        l1, l2 = self.head, list_2.head
        while l1 != l2:
            if l1:
                l1 = l1.next
            else:
                l1 = list_2.head
            if l2:
                l2 = l2.next
            else:
                l2 = self.head
        return l1

    def reverse(self):
        # iterative
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def has_cycle(self) -> bool:
        # needs to test
        if not self.head or not self.head.next:
            return False
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    print("\nLinked list tests")
    nodes = []
    for i in range(6):
        nodes += [i]
    linked_list = LinkedList()
    for node in nodes:
        linked_list.append(node)
    print("Linked List:", linked_list)
    linked_list.reorder_list()
    print("Reordered linked List:", linked_list)
    linked_list.reverse()
    print("The reversed linked list is:", linked_list)

    print("\nLinked list Intersection")
    nodes = []
    for i in range(6):
        nodes += [i]
    linked_list_1 = LinkedList()
    for node in nodes:
        linked_list_1.append(node)
    print("Linked List 1:", linked_list_1)
    nodes = []
    for i in range(3, 6):
        nodes += [i]
    linked_list_2 = LinkedList()
    linked_list_2.append(9)
    for node in nodes:
        linked_list_2.append(node)
    print("Linked List 2:", linked_list_2)
    inter = linked_list_1.intersection(linked_list_2)
    print("Intersection Node:", inter)

    print("\nHas cycle")
    print("My list:", linked_list)
    print("Has cycle:", linked_list.has_cycle())
