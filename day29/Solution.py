def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]


if __name__ == '__main__':
    print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
    # 5
