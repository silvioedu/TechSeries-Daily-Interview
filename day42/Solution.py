def first_missing_positive(nums):
    nums.sort()
    positive = []
    for n in nums:
        if n <= 0:
            continue
        positive.append(n)

    for i in range(min(positive), max(positive)):
        if i not in positive:
            return i


if __name__ == '__main__':
    print(first_missing_positive([3, 4, -1, 1]))
    # 2