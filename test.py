import cv2
import os
from PIL import Image
import glob
from facenet import Facenet





if  __name__ == "__main__":
    model = Facenet()
    test_path = r"C:\Users\yeluo\Desktop\model_result_model"
    save_path = r"C:\Users\yeluo\Desktop\result_1"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    images = os.listdir(test_path)
    for im in images:
        if len(im.split('_'))==2:
            name = im.split('_')[0]

        elif len(im.split('_'))==3:
            name = im.split('_')[0]+ im.split('_')[1]

        name1_ori = name + '_1.png'
        name2_ori = name + '_2.png'
        name1 = os.path.join(test_path, name1_ori)
        name2 = os.path.join(test_path, name2_ori)
        image1 = Image.open(name1)
        image2 = Image.open(name2)
        # print(image1, image2)
        probability = model.detect_image(image1, image2,save_path=os.path.join(save_path,name))
        print("name and probability:",name1_ori,probability)
        # if probability < 0.98:
        #     image1.save(os.path.join(save_path,name1_ori))
        #     image2.save(os.path.join(save_path,name2_ori))