class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
    node = root_node

    if node.left is None or node.right is None:
        return floor, ceil

    floor = node.value
    node = node.left if k < node.value else node.right
    ceil = node.value

    floor, ceil = findCeilingFloor(node, k, floor, ceil)

    return floor, ceil


if __name__ == '__main__':
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

    print(findCeilingFloor(root, 5))
    # (4, 6)
