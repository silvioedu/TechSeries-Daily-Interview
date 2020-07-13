def singleNumber(nums):
    s = []
    [s.append(i) if nums.count(i) == 1 else None for i in sorted(list(dict.fromkeys(nums)))]
    return s


if __name__ == '__main__':
    print(singleNumber([4, 3, 2, 4, 1, 3, 2, 5]))
    # 1
