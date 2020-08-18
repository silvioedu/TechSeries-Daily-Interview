class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    values = []
    for li in lists:
        while li:
            values.append(li.val)
            li = li.next

    values.sort(reverse=True)

    result_list = ""
    lastNode = ""
    for i in values:
        result_list = Node(i) if i == values[0] else Node(i, lastNode)
        lastNode = result_list

    return result_list


if __name__ == '__main__':
    a = Node(1, Node(3, Node(5)))
    b = Node(2, Node(4, Node(6)))
    print(merge([a, b]))
    # 123456

