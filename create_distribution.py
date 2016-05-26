#!/usr/bin/env python

import glob
import os
import random
import shutil

TRAIN_PERCENTAGE = 100

TRAIN_SET = []
VAL_SET = []

PLANTVILLAGE_PATH="/home/ubuntu/PlantVillage/plantvillage"
DATA_PATH=PLANTVILLAGE_PATH+"/crowdai"
LMDB_PATH=PLANTVILLAGE_PATH"/lmdb"

#Distribute the files into Training and Validation sets
for _image in glob.glob(DATA_PATH + "/*/*"):
        className = _image.split("/")[-2]

        # Some fileNames contain spaces, which creates some incompatibility with a preprocessing script shipped with caffe
        # Hence we replace all spaces in the filename with _
        newFileName = _image.split("/")[-1]
        newFileName = newFileName.replace(" ", "_")
        newFilePath = DATA_PATH + "/"+className+"/"+newFileName
        shutil.move(_image, newFilePath)


        if random.randint(0,100) <= TRAIN_PERCENTAGE:
                TRAIN_SET.append((newFilePath, className.split("_")[-1]))
        else:
                VAL_SET.append((newFilePath, className.split("_")[-1]))

#Write the distribution into a separate text files
try:
        os.mkdir(LMDB_PATH)
except:
        pass

f = open(LMDB_PATH+"/train.txt", "w")
for _entry in TRAIN_SET:
        f.write(_entry[0]+" "+_entry[1]+"\n")
f.close()

f = open(LMDB_PATH+"/val.txt", "w")
for _entry in VAL_SET:
        f.write(_entry[0]+" "+_entry[1]+"\n")
f.close()
