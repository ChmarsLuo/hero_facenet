import os
import shutil

def get_file_path(root):
    files = []
    for he in os.listdir(root):
        hero = os.path.join(root,he)
        for sk in os.listdir(hero):
            skin = os.path.join(hero,sk)
            if len(os.listdir(skin))==0:
                os.remove(skin)
                shutil.rmtree(skin)
            files.append(skin)

    return files



if __name__ == '__main__':
    files = get_file_path(root=r'E:\facenet-keras-main\datasets\hero_new')
    print(len(files))