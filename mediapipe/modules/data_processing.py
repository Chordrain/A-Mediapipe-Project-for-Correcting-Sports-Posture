import numpy as np
import math
import json
import matplotlib.pyplot as plt
import os
from PIL import Image


# 载入骨骼数据
def LoadPoseKeypointsData(file):
    with open(file, "r") as file:
        data = json.load(file)
    keypoints_raw = data["people"][0]["pose_keypoints_2d"]
    keypoints = []
    temp = []
    for i, v in enumerate(keypoints_raw):
        if (i + 1) % 3 != 0:
            temp.append(v)
        else:
            keypoints.append(temp)
            temp = []
    return keypoints


# 返回目录下的所有文件名
def ScanDirectory(_dir):
    all_files = []
    for root, dirs, files in os.walk(_dir):
        for file in files:
            # 输出文件路径
            all_files.append(os.path.join(root, file))
    return all_files


def Recentralize(keypoints, center):
    keypoints = keypoints.copy()
    xdiff = keypoints[1][0] - center[0]
    ydiff = keypoints[1][1] - center[1]
    for k in keypoints:
        k[0] = k[0] - xdiff
        k[1] = k[1] - ydiff
    return keypoints


# 发现openpose返回的数据是反的，为了方便可视化，将图片坐标翻转
def Flip(keypoints, size):
    keypoints = keypoints.copy()
    for k in keypoints:
        k[0] = size[0] - k[0]
        k[1] = size[1] - k[1]
    return keypoints


# 按某一比例放大
def Scale(keypoint, xratio, yratio):
    keypoints = keypoint.copy()
    for k in keypoints:
        k[0] = k[0] * (1 + xratio)
        k[1] = k[1] * (1 + yratio)
    return keypoints


# 获取归一化处理比率
# @param lw_x1: 标准动作的左腕坐标
# @param lw_x2: 待测者的左腕坐标
# @param rw_x1: 标准动作的右腕坐标
# @param rw_x2: 待测者的右腕坐标
def NormalizationRatio(lw_x1, lw_x2, rw_x1, rw_x2):
    return math.fabs((lw_x1 - lw_x2) / (rw_x1 - rw_x2))


# 将多张图片转换成gif
def ConvertToGif(image_files, _output_path):
    # 打开第一张图片，获取尺寸
    img = Image.open(image_files[0])
    img.save(
        _output_path,
        save_all=True,
        append_images=[Image.open(f) for f in image_files[:]],
        duration=10,
        loop=0,
    )


def ProcessData(_files_path, _size, _center, _output_dir, _gif_path):
    print(f"共检测到{len(_files_path)}个文件")
    for index, file in enumerate(_files_path):  # 遍历每个文件
        data = LoadPoseKeypointsData(file)  # 加载json文件，获取关节点坐标
        data = Scale(data, 1.5, 1.5)  # 对坐标进行放缩，方便可视化
        data = Flip(
            data, _size
        )  # 对坐标进行上下翻转(视频的坐标原点与matplotlib坐标轴原点不一样)
        data = Recentralize(data, _center)  # 对坐标进行平移
        plt.figure()  # 可视化坐标信息
        for d in data:
            plt.scatter(d[0], d[1], c="blue", marker="x")
        plt.xlim(0, size[0])
        plt.ylim(0, size[1])
        plt.savefig(f"{_output_dir}/{index}.png")
        plt.close()

    ConvertToGif(ScanDirectory(_output_dir), _gif_path)  # 将得到的所有图片转换成gif


def RunOpenPose(_input_video_path, _output_json_path, _output_video_path):
    os.system(
        rf"cd openpose & bin\OpenPoseDemo.exe --video {_input_video_path} --write_json {_output_json_path} --display 0 --render_pose 0"
    )
    os.system(
        rf"cd openpose & bin\OpenPoseDemo.exe --video {_input_video_path} --write_video {_output_video_path} --display 0"
    )


if __name__ == "__main__":
    size = (2560, 2560)  # 设置视频尺寸
    center = (size[0] / 2, size[1] / 1.5)  # 设置中心点位置

    # RunOpenPose("./data/引体向上(不标准).mp4", "./output/test-Pullup", "./output/test.avi")
    # RunOpenPose("./data/引体向上.mp4", "./output/standard-Pullup", "./output/standard.avi")

    all_standard_json_files = ScanDirectory(
        "openpose/output/standard-Pullup/"
    )  # 获取所有json骨骼文件
    all_test_json_files = ScanDirectory("openpose/output/test-Pullup/")

    ProcessData(all_standard_json_files, size, center, "standard", "standard.gif")
    ProcessData(all_test_json_files, size, center, "test", "test.gif")
