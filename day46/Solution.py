class Solution:
    def sortColors(self, nums):
        return nums.sort()


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
    print("Before Sort: ")
    print(nums)
    # [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

    Solution().sortColors(nums)
    print("After Sort: ")
    print(nums)
    # [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
