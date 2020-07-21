class Solution(object):

    def pushDominoes(self, dominoes):
        force = [0] * len(dominoes)
        pos = ['R', 'L', '.']

        # Populate forces going from left to right
        f = 0
        for i in range(len(dominoes)):
            if dominoes[i] == pos[0]:
                f = len(dominoes)
            elif dominoes[i] == pos[1]:
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f

        # Populate forces going from right to left
        f = 0
        for i in range(len(dominoes)-1, -1, -1):
            if dominoes[i] == pos[1]:
                f = len(dominoes)
            elif dominoes[i] == pos[0]:
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f == 0 else pos[0] if f > 0 else pos[1] for f in force)


if __name__ == '__main__' :
    print(Solution().pushDominoes('..R...L..R.'))
    # ..RR.LL..RR
