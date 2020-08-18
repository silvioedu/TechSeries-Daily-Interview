def capacity(arr):

    n = len(arr)
    res = 0

    for i in range(1, n-1):

        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])

        res = res + (min(left, right) - arr[i])
        print("{} <- {} -> {}  =  {}".format(arr[i], left, right, res))

    return res


if __name__ == '__main__':
    print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # 6
