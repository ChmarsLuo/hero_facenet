import cv2
import numpy as np
import utils
from skimage.metrics import structural_similarity as ssim
import os
import sys

def get_files_by_type(path, ftype='.png', files=[]):
    if os.path.isfile(path):
        if path.endswith(ftype):
            files.append(path)
    elif os.path.isdir(path):
        for i in os.listdir(path):
            newdir1 = os.path.join(path, i)
            for n in os.listdir(newdir1):
                newdir2 = os.path.join(newdir1, n)
                for s in os.listdir(newdir2):
                    newdir3 = os.path.join(newdir2, s)
                    get_files_by_type(newdir3, ftype, files)


    return files


if __name__ == "__main__":
    # path = sys.argv[1]
    files = get_files_by_type(r"C:\Users\yeluo\Desktop\cdk\uploadSkin_cdk")
    print(files)
    delete_img = set()
    for i, f in enumerate(files):
        img1 = cv2.imdecode(np.fromfile(f, dtype=np.uint8), -1)
        # 删除完全是背景的图片
        img_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(img_hsv, (108, 155, 40), (112, 190, 112))
        ratio = sum(sum(mask > 0)) / (img1.shape[0] * img1.shape[1])
        if ratio > 0.95:
            delete_img.add(f)
        continue
        # 删除镜头拉远的图片
        if i + 1 >= len(files):
            break
        img2 = cv2.imdecode(np.fromfile(files[i+1], dtype=np.uint8), -1)
        score, diff = ssim(img1, img2, multichannel=True, full=True)
        if score < 0.99:
            delete_img.add(files[i+1])
    for f in delete_img:
        os.remove(f)
