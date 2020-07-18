class Solution:
    def minSubArrayLen(self, nums, s):

        if nums.count(s) > 0:
            return 1

        for k in range(2, len(nums) + 1):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + sum(nums[j:j+k-1]) == s:
                        return k

        return 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
    # 2
    # print(Solution().minSubArrayLen([1, 1, 1, 1], 7))
    # 0
    # print(Solution().minSubArrayLen([1, 1, 1, 1, 1, 1, 1, 1], 7))
    # 7
    # print(Solution().minSubArrayLen([1, 1, 1, 1, 1, 1, 1, 7], 7))
    # 1
