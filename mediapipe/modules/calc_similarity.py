import math


def CalcSimilarity(v1, v2):
    return (v1[0] * v2[0] + v1[1] * v2[1]) / (math.sqrt(v1[0] ** 2 + v1[1] ** 2) * math.sqrt(v2[0] ** 2 + v2[1] ** 2))


if __name__ == '__main__':
    x = CalcSimilarity([3, 2], [3, 2])
    print(x)
