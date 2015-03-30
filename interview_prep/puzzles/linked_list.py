__author__ = 'Sergey'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def append_to_tail(self, data):
        end = Node(data)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    def print_list(self):
        h = self
        while h is not None:
            print(h.data)
            h = h.next

    def nth_to_last(self, n):
        """Returns the nth to last element of singly linked list"""
        fast = self
        i = 1
        while i <= n:
            if fast is None:
                return None
            i += 1
            fast = fast.next
        slow = self
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow


def main():
    node = Node(2)
    node.append_to_tail(1)
    node.append_to_tail(6)
    node.append_to_tail(0)
    node.append_to_tail(5)
    node.append_to_tail(4)
    node.print_list()
    third_to_last = node.nth_to_last(3)
    print("third to last node data: ", third_to_last.data)


if __name__ == '__main__':
    main()


