import mediapipe as mp
import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import matplotlib.pyplot as plt
import json

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


# 将预测出的关节点在图中标出
def draw_landmarks_on_image(rgb_image, detection_result):
    pose_landmarks_list = detection_result.pose_landmarks
    annotated_image = np.copy(rgb_image)

    # 循环每个关节点进行标注
    for idx in range(len(pose_landmarks_list)):
        pose_landmarks = pose_landmarks_list[idx]

        # 标出标记点
        pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        pose_landmarks_proto.landmark.extend(
            [
                landmark_pb2.NormalizedLandmark(
                    x=landmark.x, y=landmark.y, z=landmark.z
                )
                for landmark in pose_landmarks
            ]
        )
        solutions.drawing_utils.draw_landmarks(
            annotated_image,
            pose_landmarks_proto,
            solutions.pose.POSE_CONNECTIONS,
            solutions.drawing_styles.get_default_pose_landmarks_style(),
        )
    return annotated_image


# 加载json
def load_json(path):
    with open(path) as f:
        data = json.load(f)["data"]
    return data