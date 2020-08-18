def maximum_product_of_three(lst):
    len_lst = len(lst)
    product = []
    for i in range(len_lst-2):
        for j in range(i+1, len_lst-1):
            for k in range(j+1, len_lst):
                product.append(lst[i] * lst[j] * lst[k])

    return max(product)


if __name__ == '__main__':
    print(maximum_product_of_three([-4, -4, 2, 8]))
    # 128