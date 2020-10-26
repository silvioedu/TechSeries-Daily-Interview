def decodeString(s):
    limiter = {'open': '[', 'close': ']'}
    stack = []
    n = len(s)

    for i in range(n):
        if s[i] == limiter['close']:
            temp = ''

            while stack[-1] != limiter['open']:
                temp = stack.pop() + temp

            stack.pop()

            n = ' '
            while len(stack) and stack[-1].isnumeric():
                n = stack.pop() + n
            n = int(n)

            temp = temp * n
            stack.append(temp)
        else:
            stack.append(s[i])

    return stack[0]


if __name__ == '__main__':
    print(decodeString('2[a2[b]c]'))
    # abbcabbc
