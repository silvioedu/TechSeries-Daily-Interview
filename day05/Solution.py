class Solution:
    def getRange(self, arr, target):
        if arr.count(target) == 0:
            return [-1,-1]

        i = arr.index(target)
        j = len(arr) - arr[::-1].index(target) - 1

        return [i,j]


if __name__ == '__main__':
    #[1, 4]
    #arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    #x = 2

    #[6,8]
    #arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
    #x = 9

    #[1,2]
    #arr = [100, 150, 150, 153]
    #x = 150

    #[-1,-1]
    arr = [1,2,3,4,5,6,10]
    x = 9
    print(Solution().getRange(arr, x))
