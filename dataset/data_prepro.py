# -*- coding: utf-8 -*
import pickle
import numpy as np
import os
import random

filepath = 'captions.pickle'
with open(filepath, 'rb') as f:
    filename = pickle.load(f)

filenames = os.listdir('CV-text2face')
f = open('bounding_boxes.txt', 'w') #不要频繁开启文件，容易出错
f2 = open('images.txt', 'w')
f3 = open('train_test_split.txt', 'w')
i = 1
slice = random.sample(filenames, 200)
list_train = []
list_test = []
for filename in filenames:
    mesg = filename.split('.')
    f.write('%s 0.0 0.0 255.0 255.0\n' % mesg[0])
    f2.write('%s %s\n' % (str(i), filename))
    if filename in slice:
        f3.write('%s %s\n' %(str(i), str(1)))
        filename = filename.split('.')[0]
        list_test.append(filename.decode('utf-8'))
    else:
        f3.write('%s %s\n' %(str(i), str(0)))
        filename = filename.split('.')[0]
        list_train.append(filename.decode('utf-8'))
    i += 1

filenames = os.listdir('CV-text2face/')
dict_test = []
dict_train = []
for i in range(200):
    dict_test.append('1')
for i in  range(800):
    dict_train.append('1')

file = open('filenames_test.pickle', 'wb')
pickle.dump(list_test, file, -1)
file.close()

file = open('filenames_train.pickle', 'wb')
pickle.dump(list_train, file, -1)
file.close()

file = open('class_info_test.pickle', 'wb')
pickle.dump(dict_test, file, -1)
file.close()

file = open('class_info_train.pickle', 'wb')
pickle.dump(dict_train, file, -1)
file.close()

# filenames = os.listdir('result/')
# for filename in filenames:
#     f = open(os.path.join('result', filename), 'r')
#     line = f.read()
#     mesgs = line.split('.')
#     fw = open(os.path.join('text', filename), 'w')
#     for mesg in mesgs:
#         # words = mesg.split(' ')
#         # for i in range(len(words)):
#         #     words[i] = words[i].strip()
#         #     if words == '':
#         #         del words[i]
#
#         mesg = mesg.strip()
#         mesg.strip()
#         if mesg == '':
#             continue
#         fw.write('%s.\n' % mesg)
#     fw.close()


a = 1