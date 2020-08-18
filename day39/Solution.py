class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False

        count = 0
        for x in range(len(A)):
            if A[x] != B[x]:
                count += 1

        return True if count == 2 else False


if __name__ == '__main__':
    print(Solution().buddyStrings('ab', 'ba'))
    # True
    print(Solution().buddyStrings('ab', 'ab'))
    # False
    print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
    # True
    print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
    # False
    print(Solution().buddyStrings('', 'aa'))
    # False
