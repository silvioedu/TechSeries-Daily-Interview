class Solution:

    def isValid(self, s):
        o = ['(', '[', '{']
        c = [')', ']', '}']

        for i in range(len(o)):
            if s.count(o[i]) != s.count(c[i]):
                return False

        return True


if __name__ == '__main__':
    s = "((()))"  # True
    #s = "[()]{}"  #True
    #s = "()(){(())"  #False
    #s = "" #True
    #s = "([{}])()" #True

    print(Solution().isValid(s))
