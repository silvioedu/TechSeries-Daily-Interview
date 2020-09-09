def findRange(nums):
    pos_fim = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            pos_fim = i
            break

    ref = nums[pos_fim]
    pos_ini = 0
    for i in range(pos_fim):
        if nums[i] > ref:
            pos_ini = i-1
            break

    return nums[pos_ini], nums[pos_fim]


if __name__ == '__main__':
    print(findRange([1, 7, 9, 5, 7, 8, 10]))
    # (1, 5)

