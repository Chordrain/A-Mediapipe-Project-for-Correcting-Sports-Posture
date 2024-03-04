from run_pose_landmark_model import run_pose_landmark_model
from modules.tools import landmarks2vec

if __name__ == '__main__':
    pose_landmarker_results = run_pose_landmark_model() # 获取关节点坐标

    vec = landmarks2vec(pose_landmarker_results)    # 获取坐标向量
    print(vec.shape)
