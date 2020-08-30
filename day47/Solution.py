import numpy as np


def running_median(stream):
    med = []
    for i in range(1, len(stream)+1):
        med.append(np.median(stream[:i]))
    return med


if __name__ == '__main__':
    print(running_median([2, 1, 4, 7, 2, 0, 5]))
    # 2 1.5 2 3.0 2 2.0 2
