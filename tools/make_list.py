# -*- coding: utf-8 -*- 

# make list for PASCAL VOC dataset
#this file put under VOCdevikit
#author:  mkl
#date:    2018.12.28

import os
import random
door = 0.6 # used to: 0.6 to train , 0.4 to test
data = 'VOC2007'
nameList = []
for folderName, subfolders, filenames in os.walk(data+'/JPEGImages'):
    # print('the current folder is ' + folderName)
    # for subfolder in subfolders:
        # print('subfolder of ' + folderName + ' : ' + subfolder)
    for filename in filenames:
        # print('file inside ' + folderName + ' : ' + filename)
        nameList.append(filename)
random.shuffle(nameList)
# for i in nameList:
#     print(i[:-4])


write_trainval = open(data + '/ImageSets/Main/trainval.txt','w')
write_train = open(data + '/ImageSets/Main/train.txt','w')
write_val = open(data + '/ImageSets/Main/val.txt','w')
write_test = open(data + '/ImageSets/Main/test.txt','w')

for one in nameList:
    if random.random()<door:
        write_trainval.write(one[:-4] + '\n')
        if random.random() < 0.5:
            write_train.write(one[:-4] + '\n')
        else:
            write_val.write(one[:-4] + '\n')
    else:
        write_test.write(one[:-4] + '\n')

write_trainval.close()
write_train.close()
write_val.close()
write_test.close()