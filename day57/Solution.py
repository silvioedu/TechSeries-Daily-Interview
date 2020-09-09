def getBonuses(performance):
    bonus = [1]
    for i in range(1, len(performance)-1):
        plus = 1
        if performance[i] > performance[i-1]:
            plus += 1
        if performance[i] > performance[i+1]:
            plus += 1
        bonus.append(plus)

    bonus.append(performance[len(performance)-1])
    return bonus


if __name__ == '__main__':
    print(getBonuses([1, 2, 3, 2, 3, 5, 1]))
    # [1, 2, 3, 1, 2, 3, 1]

