class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    left = ()
    count = 1
    n = node
    while n:
        left = (count, n.val)
        n = n.left
        count += 1

    right = ()
    count = 1
    n = node
    while n:
        right = (count, n.val)
        n = n.right
        count += 1

    if left[0] > right[0]:
        return left
    else:
        return right


if __name__ == '__main__':
    root = Node('a')
    root.left = Node('b')
    root.left.left = Node('d')
    root.right = Node('c')

    print(deepest(root))
    # (d, 3)
