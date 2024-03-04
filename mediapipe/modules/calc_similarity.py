import numpy as np


# 相似性计算
def calc_similarity(v1, v2):
    return (v1[0] * v2[0] + v1[1] * v2[1]) / (np.sqrt(v1[0] ** 2 + v1[1] ** 2) * np.sqrt(v2[0] ** 2 + v2[1] ** 2))


if __name__ == '__main__':
    x = calc_similarity([3, 2], [3, 2])
    print(x)
