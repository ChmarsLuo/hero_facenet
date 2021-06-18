import cv2
import numpy as np
import utils
from skimage.metrics import structural_similarity as ssim
import os
import sys
SIMI_SOCRE = 0.85
BG_COLOR_RANGE_LIST = [
    [
        (108, 124, 102),
        (109, 125, 104)
    ],
    [
        (108, 155, 40),
        (112, 190, 112)
    ]
]

def get_files_by_type(path, ftype='.png', files=[]):
    if os.path.isfile(path):
        if path.endswith(ftype):
            files.append(path)
    elif os.path.isdir(path):
        for s in os.listdir(path):
            newdir = os.path.join(path, s)
            get_files_by_type(newdir, ftype, files)
    return files


if __name__ == "__main__":
    # path = sys.argv[1]
    files = get_files_by_type(r"E:\facenet-keras-main\datasets\hero_new")
    delete_img = set()
    for i, f in enumerate(files):
        img1 = cv2.imdecode(np.fromfile(f, dtype=np.uint8), -1)
        # 删除完全是背景的图片
        img_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
        arr = None
        for color_range in BG_COLOR_RANGE_LIST:
            mask = cv2.inRange(img_hsv, color_range[0], color_range[1])
            if arr is None:
                arr = mask > 0
            else:
                arr = np.bitwise_or(arr, mask > 0)
        arr = np.where(arr == True, 255, 0)
        mask = np.array(arr, dtype=np.uint8)
        ratio = sum(sum(mask > 0)) / (img1.shape[0] * img1.shape[1])
        print(ratio)
        if ratio > 0.95:
            delete_img.add(f)
            continue
        # 删除镜头拉远的图片
        if i + 1 >= len(files):
            break
        img2 = cv2.imdecode(np.fromfile(files[i+1], dtype=np.uint8), -1)
        score, diff = ssim(img1, img2, multichannel=True, full=True)
        if score < SIMI_SOCRE:
            if i < len(files) - 2:
                img3 = cv2.imdecode(np.fromfile(files[i + 2], dtype=np.uint8), -1)
                score, diff = ssim(img2, img3, multichannel=True, full=True)
                if score < SIMI_SOCRE:
                    delete_img.add(files[i + 1])
            else:
                delete_img.add(files[i+1])
    for f in delete_img:
        os.remove(f)
