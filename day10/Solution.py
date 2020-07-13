def check(lst):
    if len(lst) <= 2:
        return True

    for i in range(2, len(lst)):
        #print("{} > {}".format(lst[i-1], lst[i]))
        if lst[i-1] > lst[i]:
            return False
    return True


if __name__ == '__main__':
    print(check([13, 4, 7]))
    # True
    print(check([5, 1, 3, 2, 5]))
    # False
