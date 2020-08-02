def findKthLargest(nums, k):
    return sorted(nums, reverse=True)[k-1]


if __name__ == '__main__':
    print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
    # 5
