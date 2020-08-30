class Solution(object):
    def threeSum(self, nums):
        sum0 = set()
        [sum0.add((nums[x], nums[y], nums[z])) if nums[x] + nums[y] + nums[z] == 0 else None
            for x in range(len(nums))
            for y in range(x+1, len(nums))
            for z in range(y+1, len(nums))]
        return sum0


if __name__ == '__main__':
    # Test Program
    nums = [1, -2, 1, 0, 5]
    print(Solution().threeSum(nums))

    nums = [0, -1, 2, -3, 1]
    print(Solution().threeSum(nums))