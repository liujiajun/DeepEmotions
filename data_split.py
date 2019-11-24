import os
import shutil
from random import sample

dataset_dir = '/Users/wuchu/Documents/UROP/DeepEmotions/dataset'
train_dir = '/train'
test_dir = '/test'
test_ratio = 0.2

class_names = os.listdir(dataset_dir + train_dir)

for class_name in class_names:
    if (not os.path.exists(dataset_dir + test_dir + '/' + class_name)):
        os.mkdir(dataset_dir + test_dir + '/' + class_name)

for class_name in class_names:
    all_images = os.listdir(dataset_dir + train_dir + '/' + class_name)
    samples = sample(all_images, (int)(len(all_images) * test_ratio))
    for image_name in samples:
        source = dataset_dir + train_dir + '/' + class_name + '/' + image_name
        dest = dataset_dir + test_dir + '/' + class_name + '/' + image_name
        shutil.move(source, dest)