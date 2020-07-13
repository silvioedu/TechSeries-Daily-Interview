def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def staircase(n):
    return fibonacci(n + 1)


if __name__ == '__main__':
    print(staircase(4))
    # 5
    print(staircase(5))
    # 8
