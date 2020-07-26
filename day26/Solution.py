def witnesses(heights):
    count = 0
    for i in range(len(heights)-1):
        if heights[i] > heights[i+1]:
            count += 1
    return count + 1


if __name__ == '__main__':
    print(witnesses([3, 6, 3, 4, 1]))
    # 3
