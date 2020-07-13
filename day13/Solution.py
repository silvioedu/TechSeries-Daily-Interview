class MaxStack:

    def __init__(self):
        self.array = []

    def push(self, val):
        self.array.append(val)

    def pop(self):
        self.array.pop()

    def max(self):
        self.array.sort(reverse=True)
        return self.array[0]


if __name__ == '__main__':
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print(s.max())
    # 3
    s.pop()
    s.pop()
    print(s.max())
    # 2
