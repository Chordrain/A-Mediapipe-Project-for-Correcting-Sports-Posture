import numpy as np


# 计算节点之间的距离(欧氏距离)
def euclidean_dist(landmarks1, landmarks2):
    sum = 0
    for coord_idx in range(landmarks1.shape[0]):
        sum += np.sqrt(np.sum(np.square(landmarks1[coord_idx][0:2] - landmarks2[coord_idx][0:2])))
    return sum


# 时间动态规划，vec1是标准视频，vec2是测试视频
def dynamic_time_warping(vec1, vec2):
    len1, len2 = vec1.shape[0], vec2.shape[0]
    admatrix = [[0 for j in range(len2)] for i in range(len1)]  # 构造初始累计距离矩阵，len1*len2

    # 构造第一列
    for i in range(len1):
        admatrix[i][0] = euclidean_dist(vec1[i], vec2[0])
        if i != 0:
            admatrix[i][0] += admatrix[i - 1][0]

    # 构造第一行
    for i in range(len2):
        admatrix[0][i] = euclidean_dist(vec1[0], vec2[i])
        if i != 0:
            admatrix[0][i] += admatrix[0][i - 1]

    # 填补剩余位置
    for i in range(1, len1):
        for j in range(1, len2):
            admatrix[i][j] = euclidean_dist(vec1[i], vec2[j]) + min(admatrix[i - 1][j], admatrix[i][j - 1],
                                                          admatrix[i - 1][j - 1])

    # for i in range(len1 - 1, -1, -1):
    #     for j in range(0, len2):
    #         print('%02d' % admatrix[i][j], end=' ')
    #     print()

    # 寻找匹配路径
    aligned = []
    x, y = len1 - 1, len2 - 1
    match = [[False for j in range(len2)] for i in range(len1)]
    while x != 0 and y != 0:
        match[x][y] = True
        aligned.append(x)
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
    aligned.append(x)

    # 打印匹配完成后的路径
    # for i in range(len1 - 1, -1, -1):
    #     for j in range(0, len2):
    #         print('%1d' % int(match[i][j]), end=' ')
    #     print()
    
    # aligned = []    # 对齐的结果，align[i]=x，表示测试视频的第i帧对应标准视频的第x帧
    # for col in range(0, len(match[0])):
    #     for row in range(len(match)):
    #         if match[row][col]:
    #             aligned.append(row)
    #             break

    return np.array(aligned)[::-1]