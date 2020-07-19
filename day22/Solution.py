def intersection(a, b):

    while a:
        c = b
        while c:
            if a.val == c.val:
                return c
            c = c.next
        a = a.next

    return 0


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def prettyPrint(self):
        c = self
        while c:
            print(c.val),
            c = c.next


if __name__ == '__main__' :
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next

    c = intersection(a, b)
    c.prettyPrint()
    # 3 4
