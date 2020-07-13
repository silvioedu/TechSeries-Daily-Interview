class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2, c = 0):
        v1 = l1.val + l1.next.val * 10 + l1.next.next.val * 100
        v2 = l2.val + l2.next.val * 10 + l2.next.next.val * 100
        t = v1 + v2
        lt = ListNode(str(t)[2])
        lt.next = ListNode(str(t)[1])
        lt.next.next = ListNode(str(t)[0])
        return lt

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next