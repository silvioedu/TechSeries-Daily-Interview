def two_sum(list, k):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if (list[i] + list[j] == k):
                #print("{} + {}".format(list[i],list[j]))
                return True
    return False

if __name__ == '__main__':
    print(two_sum([4,7,1,-3,2], 5))
    # True
