class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    @staticmethod
    def reverseIteratively(head):
        reverse = None
        following = head.next
        while head:
            head.next = reverse
            reverse = head
            head = following
            if following:
                following = following.next


if __name__ == '__main__':
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail
    print("Initial list: ")
    testHead.printList()
    #4 3 2 1 0

    testHead.reverseIteratively(testHead)
    print("List after reversal: ")
    testTail.printList()
    #0 1 2 3 4
