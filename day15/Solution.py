def arraySquare(nums):
    square = []
    [square.append(pow(i, 2)) for i in sorted(nums)]
    return square


def findPythagoreanTriplets(nums):
    n = arraySquare(nums)
    # print(nums)
    for a in (range(len(n) - 2)):
        # print("a -> ", nums[a])
        for b in (range(a + 1, len(n) - 1)):
            # print("  b -> ", nums[b])
            for c in (range(b + 1, len(n))):
                # print("    c -> ", nums[c])
                # print('{} == {} + {} --> {}'.format(n[a], n[b], n[c], n[a] == n[b] + n[c]))
                # print('{} == {} + {} --> {}'.format(n[b], n[a], n[c], n[b] == n[a] + n[c]))
                # print('{} == {} + {} --> {}'.format(n[c], n[a], n[b], n[c] == n[a] + n[b]))
                if n[a] == n[b] + n[c] or \
                        n[b] == n[a] + n[c] or \
                        n[c] == n[a] + n[b]:
                    return True
    return False


if __name__ == '__main__':
    print(findPythagoreanTriplets([3, 12, 5, 13]))
    # True
    print(findPythagoreanTriplets([10, 4, 6, 12, 5]))
    # False
