class Solution:
    def reverseWords(self, str):
        reverse_words = []
        for w in str.split():
            reverse_words.append(w[::-1])
        return " ".join(reverse_words)


if __name__ == '__main__':
    print(Solution().reverseWords("The cat in the hat"))
    # ehT tac ni eht tah
