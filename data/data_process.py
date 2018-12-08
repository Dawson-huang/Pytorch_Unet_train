import os
import sys
import numpy as np
import random
import cv2

width = 256
height = 256

def distortion():
    pass

def data_process_256(data_path):
    images = os.listdir(data_path + "image")
    ids = []
    for l in images:
        l = l.strip().split(".")
        ids.append(int(l[0]))
    ids.sort()

    if not os.path.exists("prepare"):
        os.makedirs("prepare") 
    if not os.path.exists("prepare/train"):
        os.makedirs("prepare/train") 
    if not os.path.exists("prepare/label"):
        os.makedirs("prepare/label")
    fw = open("prepare/train.txt", 'w')  

    for i in ids:
        image = cv2.imread(data_path+"image/"+str(i)+".png", 0)
        label = cv2.imread(data_path+"label/"+str(i)+".png", 0)
        h, w = image.shape
 
        num = 20
        for j in range(num):
            random.seed(random.randint(0,100000))
            x0 = random.randint(0,100000) % (w-width)
            y0 = random.randint(0,100000) % (h-height)

            new_img = image[y0:y0+height, x0:x0+width]
            new_lab = label[y0:y0+height, x0:x0+width]
            img_name = "prepare/train/%d_%d.png"%(i, j)
            lab_name = "prepare/label/%d_%d.png"%(i, j)
            cv2.imwrite(img_name, new_img)   
            cv2.imwrite(lab_name, new_lab) 
            fw.write(img_name + " " + lab_name + '\n')
def shuffle_split():
    lines = open("prepare/train.txt", 'r').read().splitlines()
    train = open("prepare/train_source.txt", 'w')
    label = open("prepare/label_source.txt", 'w')

    random.shuffle(lines)
    random.shuffle(lines)
    random.shuffle(lines)
    for l in lines:
        l = l.strip().split(" ")
        train.write(l[0] + " 0\n")
        label.write(l[1] + " 0\n")

if __name__ == '__main__':
    data_process_256("membrane/train/")
    shuffle_split()


