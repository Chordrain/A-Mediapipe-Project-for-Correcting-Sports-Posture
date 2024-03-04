import math
import numpy as np


# 计算节点之间的距离(欧氏距离)
def calc_dist(x, y):
    # return abs(x - y)
    return math.sqrt(math.fabs(x ** 2 - y ** 2))


# 时间动态规划
def dynamic_time_warping(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    admatrix = [[0 for j in range(len2)] for i in range(len1)]  # 累计距离矩阵，len1*len2

    # 构造第一列
    for i in range(len1):
        admatrix[i][0] = calc_dist(seq1[i], seq2[0])
        if i != 0:
            admatrix[i][0] += admatrix[i - 1][0]

    # 构造第一行
    for i in range(len2):
        admatrix[0][i] = calc_dist(seq1[0], seq2[i])
        if i != 0:
            admatrix[0][i] += admatrix[0][i - 1]

    # 填补剩余位置
    for i in range(1, len1):
        for j in range(1, len2):
            admatrix[i][j] = calc_dist(seq1[i], seq2[j]) + min(admatrix[i - 1][j], admatrix[i][j - 1],
                                                          admatrix[i - 1][j - 1])

    # for i in range(len1 - 1, -1, -1):
    #     for j in range(0, len2):
    #         print('%02d' % admatrix[i][j], end=' ')
    #     print()

    # 寻找匹配路径
    x, y = len1 - 1, len2 - 1
    match = [[False for j in range(len2)] for i in range(len1)]
    while x != 0 and y != 0:
        match[x][y] = True
        cads = [admatrix[x - 1][y] if x != 0 else 0xfff, admatrix[x][y - 1] if y != 0 else 0xfff,
                admatrix[x - 1][y - 1] if x != 0 and y != 0 else 0xfff]
        nextstep = np.argmin(cads)
        if nextstep == 0:
            x -= 1
        elif nextstep == 1:
            y -= 1
        else:
            x -= 1
            y -= 1
    match[x][y] = True

    # 打印匹配完成后的路径
    for i in range(len1 - 1, -1, -1):
        for j in range(0, len2):
            print('%1d' % int(match[i][j]), end=' ')
        print()


dynamic_time_warping([1, 3, 4, 9, 8, 2, 1, 5, 7, 3], [1, 6, 2, 3, 0, 9, 4, 1, 6, 3])
