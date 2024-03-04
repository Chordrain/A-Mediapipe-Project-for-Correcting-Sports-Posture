vec = []    # vec应该为一个3d向量，该程序能将其拆解成一个矩阵输出
ii, jj, kk = vec.shape
print("[", end="", sep="")
for i in range(ii):
    print("[", end="", sep="")
    for j in range(jj):
        print("[", end="", sep="")
        for k in range(kk):
            print(vec[i][j][k], sep="", end="")
            if k + 1 != kk:
                print(",", end="", sep="")
        print("]", end="", sep="")
        if j + 1 != jj:
            print(",", end="", sep="")
    print("]", end="", sep="")
    if i + 1 != ii:
        print(",", end="", sep="")
print("]", end="", sep="")
