import mediapipe as mp
import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np


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


def run_pose_landmark_model(_show_video=False):
    BaseOptions = mp.tasks.BaseOptions
    PoseLandmarker = mp.tasks.vision.PoseLandmarker
    PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    model_path = "./models/pose_landmarker.task"

    # 以视频模式创建姿态标记模型实例
    options = PoseLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.VIDEO,
    )

    with PoseLandmarker.create_from_options(options) as landmarker:
        video = cv2.VideoCapture("./modules/sports/pullup/video/standard2.mp4")  # 加载视频
        frame_cnt = 0  # 设置帧时间戳

        # 判断视频是否被正确打开
        if video.isOpened():
            open, frame = video.read()
        else:
            open = False
            print("---------video loading failed---------")

        # 设置显示窗口大小
        if _show_video:
            cv2.namedWindow("frame", 0)
            cv2.resizeWindow("frame", 1000, 600)

        # annotated_images = []
        pose_landmarker_results = []

        # 运行pose landmark model
        while open:
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            pose_landmarker_result = landmarker.detect_for_video(mp_image, frame_cnt)
            pose_landmarker_results.append(pose_landmarker_result)
            
            # annotated_images.append(annotated_image)

            # 生成标注过的图像
            # 展示每一帧画面
            if _show_video:
                annotated_image = draw_landmarks_on_image(frame, pose_landmarker_result)
                cv2.imshow("frame", annotated_image)

            if cv2.waitKey(1) & 0xFF == 27:
                break

            open, frame = video.read()
            frame_cnt += 1
            
        video.release()
        cv2.destroyAllWindows()

    return pose_landmarker_results
