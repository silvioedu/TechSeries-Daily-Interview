class Solution:
    def moveZeros(self, nums):
        l = list(nums)
        count = l.count(0)

        i = 0
        x = count
        while x > 0:
            if l[i] == 0:
                l.pop(i)
                x -= 1
            else:
                i += 1

        [l.append(0) for i in range(count)]

        return l


if __name__ == '__main__':
    nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
    nums = Solution().moveZeros(nums)
    print(nums)
    # [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]