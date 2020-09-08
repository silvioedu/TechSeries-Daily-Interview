def findRanges(nums):
    interval = 3
    num_groups = round((max(nums) - min(nums)) / interval, 0)
    
    ranges = []
    for i in range(min(nums),max(nums),interval+1):
        r = str(i) + '->' + str(i+interval)
        ranges.append(r)
    return ranges


if __name__ == '__main__':
    print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
    # ['0->2', '5->5', '7->11', '15->15']
