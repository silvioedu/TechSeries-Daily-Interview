class Solution:
    minLimit = 2**31 * -1
    maxLimit = 2**31 - 1

    def reverse(self, x):
        rev = int(str(x)[::-1])

        if self.minLimit < rev < self.maxLimit:
            return rev
        return 0


if __name__ == '__main__':
    print(Solution().reverse(123))
    # 321
    print(Solution().reverse(2**31))
    # 0

