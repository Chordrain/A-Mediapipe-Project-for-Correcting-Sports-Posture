import numpy as np

# 将得到的关节点信息转换为ndarray
def landmarks2vec(pose_landmarks):
    vec2d = []
    for pose in pose_landmarks:
        vec1d = []
        pose_landmarks_list = pose.pose_landmarks[0]
        for idx in range(len(pose_landmarks_list)):
            x = pose_landmarks_list[idx].x
            y = pose_landmarks_list[idx].y
            z = pose_landmarks_list[idx].z
            v = pose_landmarks_list[idx].visibility
            p = pose_landmarks_list[idx].presence
            vec1d.append([x, y, z, v, p])
        vec2d.append(vec1d)
    vec3d = np.array(vec2d)
    return vec3d
