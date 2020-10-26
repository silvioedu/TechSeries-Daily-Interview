class minStack(object):
    def __init__(self):
        self.numbers = []

    def push(self, x):
        self.numbers.append(x)

    def pop(self):
        self.numbers.pop() if len(self.numbers) > 0 else None

    def top(self):
        return self.numbers[-1] if len(self.numbers) > 0 else None

    def getMin(self):
        return min(self.numbers) if len(self.numbers) > 0 else None


if __name__ == '__main__':
    x = minStack()
    x.push(-2)
    x.push(0)
    x.push(-3)
    print(x.getMin())
    # -3
    x.pop()
    print(x.top())
    # 0
    print(x.getMin())
    # -2
