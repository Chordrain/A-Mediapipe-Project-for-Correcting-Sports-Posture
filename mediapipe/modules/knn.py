from sklearn import neighbors

# vec1是参照数据集，vec2是测试数据集
# vec1的最后一列是标签
def knn(vec1, vec2):
    knn = neighbors.KNeighborsClassifier()
    # 训练
    knn.fit(vec1[:-1], vec1[-1])
    # 预测
    predict = knn.predict(vec2)
    # 返回分类结果
    return predict
