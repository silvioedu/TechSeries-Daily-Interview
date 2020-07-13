class Solution:
    def hasDuplication(self,sub):
        # Remove duplicate values
        tmp = list(dict.fromkeys(sub))

        # If is different, has duplication values
        if (len(sub) != len(tmp)):
            return False
        return True

    def findLongestSubstring(self, s):
        longest = ""
        for i in range(len(s)):
            for j in (range(i+1, len(s))):
                sub = s[i:j]
                if not Solution().hasDuplication(sub):
                    break
                if len(sub) > len(longest):
                    longest = sub
        return longest

    def lengthOfLongestSubstring(self, s):
        return len(Solution().findLongestSubstring(s))


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
