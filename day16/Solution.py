def distance(s1, s2):
    d = 0
    l1 = list(s1)
    l2 = list(s2)
    for i in range(len(l1)):
        if l2.count(l1[i]) == 0:
            d += 1
            continue

        l2_index = l2.index(l1[i], i)
        l2_distance = l2_index - i
        if l2_distance > 0:
            l2.pop(l2_distance)
            d += l2_distance

    return d


if __name__ == '__main__':
    print(distance('biting', 'sitting'))
    # 2
