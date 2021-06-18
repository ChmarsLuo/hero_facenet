import os
import pinyin
import glob
import shutil



if __name__ == '__main__':
    path = r'C:\Users\yeluo\Desktop\cdk\uploadSkin'
    save_path = r'C:\Users\yeluo\Desktop\cdk\uploadSkin_cdk'

    for he in os.listdir(path):
        hero = os.path.join(path,he)
        he_str = pinyin.get(he,format='strip')
        for sk in os.listdir(hero):
            skin = os.path.join(hero,sk)
            sk_str = pinyin.get(sk,format='strip')
            for i in os.listdir(skin):
                number = os.path.join(skin,i)
                for fra in os.listdir(number):
                    frame = os.path.join(number,fra)
                    images = []
                    for im in os.listdir(frame):
                        image = os.path.join(frame,im)
                        images.append(image)

                    # a = ['left','right','backward','forward']
                    # # image = glob.glob(frame + '/' + 'left' + '*.png')
                    # for n in a:
                    #     image = glob.glob(frame+'/'+n+'*.png')
                    #     final_path = os.path.join(save_path,he_str,sk_str+'_'+str(i)+'_'+fra.replace(' ',''))
                    #     if not os.path.exists(final_path):
                    #         os.makedirs(final_path)
                    #     # name = final_path + im
                    #     for j in image:
                    for j in images:
                        a = ['left', 'right', 'backward', 'forward']
                        if 'left' in j:
                            final_path = os.path.join(save_path,he_str,sk_str+'_'+str(i)+'_'+fra.replace(' ',''))
                            final_path = final_path + '_' + 'left'
                            if not os.path.exists(final_path):
                                os.makedirs(final_path)
                            name = os.path.join(final_path,j.split('\\')[10])
                            image = shutil.copyfile(j,name)
                        elif 'right' in j:
                            final_path = os.path.join(save_path, he_str,sk_str + '_' + str(i) + '_' + fra.replace(' ', ''))
                            final_path = final_path + '_' + 'right'
                            if not os.path.exists(final_path):
                                os.makedirs(final_path)
                            name = os.path.join(final_path,j.split('\\')[10])
                            image = shutil.copyfile(j, name)
                        elif 'backward' in j:
                            final_path = os.path.join(save_path, he_str,
                                                      sk_str + '_' + str(i) + '_' + fra.replace(' ', ''))
                            final_path = final_path + '_' + 'backward'
                            if not os.path.exists(final_path):
                                os.makedirs(final_path)
                            name = os.path.join(final_path,j.split('\\')[10])
                            image = shutil.copyfile(j, name)
                        elif 'forward' in j:
                            final_path = os.path.join(save_path, he_str,
                                                      sk_str + '_' + str(i) + '_' + fra.replace(' ', ''))
                            final_path = final_path + '_' + 'forward'
                            if not os.path.exists(final_path):
                                os.makedirs(final_path)
                            name = os.path.join(final_path ,j.split('\\')[10])
                            image = shutil.copyfile(j, name)

                            print(name)


                    # print(images)






