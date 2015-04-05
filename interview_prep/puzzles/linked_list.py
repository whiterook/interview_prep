__author__ = 'Sergey'


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    @staticmethod
    def fill_from_string(input_string, delimiter=' '):
        head = None
        try:
            items = input_string.split(delimiter)
            for item in items:
                if head is None:
                    head = Node(item)
                else:
                    head.append_to_tail(item)
            return head
        except:
            print('argument is not a string')
            return head

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
    head = Node.fill_from_string('2 1 6 0 5 4')
    head.print_list()
    third_to_last = head.nth_to_last(3)
    print("third to last head data: ", third_to_last.data)


if __name__ == '__main__':
    main()


