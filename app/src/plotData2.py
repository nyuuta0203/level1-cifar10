from pathlib import Path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import glob, os

Data_Path = "../data"
train = glob.glob(Data_Path + "/train/*")
test = glob.glob(Data_Path + "/test/*")

count_train_list = []
count_test_list = []
label_train_list = []
label_test_list = []

for f in train:
    label = os.path.basename(f)
    #print(label)
    count = len(glob.glob(f + "/*.png"))
    #print(count)
    count_train_list.append(count)
    #print(count_list)
    label_train_list.append(label)
    #print(label_list)

for f in test:
    label = os.path.basename(f)
    #print(label)
    count = len(glob.glob(f + "/*.png"))
    #print(count)
    count_test_list.append(count)
    #print(count_list)
    label_test_list.append(label)
    #print(label_list)

left = np.arange(len(count_train_list))
w = 0.3
plt.title("AmountOfNumber", fontsize=15)
plt.ylabel('Sum')
plt.xlabel('Label')
plt.tick_params(labelsize=7)
plt.xticks(left + w/2,labels = label_train_list)
plt.bar(left,height=count_train_list,
        color='green',
        width=0.3,
        align='center',
        edgecolor='royalblue',
        linewidth=1.5,
        label="TRAIN")
plt.bar(left + w,height=count_test_list,
        color='orange',
        width=0.3,
        align='center',
        edgecolor='royalblue',
        linewidth=1.5,
        label="TEST")
plt.savefig('../../plot.png')
    
