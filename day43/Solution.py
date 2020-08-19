class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    n = root
    last = 0
    while n:
        if last == 0:
            last = n.key
            n = n.left
            continue

        if last < n.key:
            return False
        n = n.left

    n = root
    last = 0
    while n:
        if last == 0:
            last = n.key
            n = n.right
            continue

        if last > n.key:
            return False
        n = n.right

    return True


if __name__ == '__main__':
    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(4)
    a.right.left = TreeNode(6)
    print(is_bst(a))

    #    5
    #   / \
    #  3   7
    # / \ /
    #1  4 6

