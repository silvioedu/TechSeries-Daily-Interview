def num_ways(n, m):
    if m == 1 or n == 1 :
        return 1

    return (num_ways(m - 1, n) +
            num_ways(m, n - 1))


if __name__ == '__main__' :
    print(num_ways(2, 2))
    # 2
    print(num_ways(5, 5))
    # 70
