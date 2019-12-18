import pickle
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def unpickle(path):
        with open(path, 'rb') as f:
            dict = pickle.load(f, encoding='bytes')
        return dict

Data_Path = "../data/cifar-10-batches-py"
train_list = []
test_list = []

for i in range(1,6):
    train_dic = unpickle("../data/cifar-10-batches-py/data_batch_{}".format(i))
    for i in range(len(train_dic[b'data'])):
        labels_image = [train_dic[b'labels']]
        train_list.append(labels_image)


test_dic = unpickle("../data/cifar-10-batches-py/test_batch")
for i in range(len(test_dic[b'data'])):
        labels_image = [test_dic[b'labels']]
        test_list.append(labels_image)

#train_list = np.array(train_list)
#test_list = np.array(test_list)
#print(train_amount)
#print(test_amount)

label_data = unpickle(os.path.join(Data_Path,"batches.meta"))
label_list = label_data[b'label_names']

plt.subplot(1,2,1)
plt.title("train", fontsize=15)
plt.xlabel("class")
plt.ylabel("images")
plt.tick_params(labelsize=7)
plt.bar(label_list,train_list)

