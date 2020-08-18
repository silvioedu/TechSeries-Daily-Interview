def buy_and_sell(arr):
    profit = []
    for i in range(len(arr)):
        buy = arr[i]
        for j in range(i+1, len(arr)):
            sell = arr[j]
            profit.append(sell - buy)
            print("buy {} sell {} profit {}".format(buy, sell, sell-buy))
    return max(profit)


if __name__ == '__main__':
    print( buy_and_sell([9, 11, 8, 5, 7, 10]))
    # 5
