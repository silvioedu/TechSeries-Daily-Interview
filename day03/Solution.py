class Solution:
    def isPlalindrome(self,s):
        return s == s[::-1]

    def longestPalindrome(self, s):
        sub = []
        longest = []

        for j in range(0,len(s)):
            for i in range(0,len(s)):
                sub = s[i:len(s)-j]
                if Solution().isPlalindrome(sub) is True:
                    if len(sub) > len(longest):
                        longest = sub
                    break

        return longest

if __name__ == '__main__':
    s = "tracecars"
    #s = "banana"
    #s = "million"
    print(str(Solution().longestPalindrome(s)))
