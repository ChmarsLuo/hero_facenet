import cv2
import os
from PIL import Image
import glob
from facenet import Facenet





if  __name__ == "__main__":
    model = Facenet()
    test_path_1 = r"C:\Users\yeluo\Desktop\pi_0"
    test_path_2 = r"C:\Users\yeluo\Desktop\pi_1"
    save_path = r"C:\Users\yeluo\Desktop\result_3"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for i in os.listdir(test_path_1):
        image1 = os.path.join(test_path_1,i)
        image1 = Image.open(image1)
        image2 = os.path.join(test_path_2,i)
        image2 = Image.open(image2)

        probability = model.detect_image(image1, image2,save_path=os.path.join(save_path,i))
        print("name and probability:",i,probability)
        # if probability < 0.98:
        #     image1.save(os.path.join(save_path,name1_ori))
        #     image2.save(os.path.join(save_path,name2_ori))