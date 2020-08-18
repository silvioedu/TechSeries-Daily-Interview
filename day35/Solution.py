def max_subarray_sum(arr):
    return max(sum(arr[i:]) for i in range(len(arr)))


if __name__ == '__main__':
    print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
    # 137
