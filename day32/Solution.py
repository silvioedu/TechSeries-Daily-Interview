def merge(intervals):
    intervals.sort()
    total = []
    merge = []
    for interval in intervals:
        #print("interval {} starting {} ending {}".format(interval, interval[0], interval[1]))
        if interval[0] not in total and interval[1] not in total:
            merge.append(interval)
            [total.append(i) for i in range(interval[0], interval[1]+1)]

    return merge


if __name__ == '__main__':
    print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
    # [(1, 3), (4, 10), (20, 25)]
