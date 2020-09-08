def products(nums):
    prod = []
    for i in range(len(nums)):
        p = 1
        for j in range(len(nums)):
            if i != j:
                p *= nums[j]
        prod.append(p)
    return prod


if __name__ == '__main__':
    print(products([1, 2, 3, 4, 5]))
    # [120, 60, 40, 30, 24]
