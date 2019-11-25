import os
import shutil
import random

dataset_dir = '/Users/wuchu/Documents/UROP/DeepEmotions/fer'
train_dir = '/train'
test_dir = '/test'
valid_dir = '/valid'
valid_ratio = 0.1
test_ratio = 0.1

class_names = os.listdir(dataset_dir + train_dir)

for class_name in class_names:
    if (not os.path.exists(dataset_dir + test_dir + '/' + class_name)):
        os.mkdir(dataset_dir + test_dir + '/' + class_name)
    if (not os.path.exists(dataset_dir + valid_dir + '/' + class_name)):
        os.mkdir(dataset_dir + valid_dir + '/' + class_name)


for class_name in class_names:
    all_images = os.listdir(dataset_dir + train_dir + '/' + class_name)

    random.shuffle(all_images)

    size = len(all_images)

    valid_images = all_images[:(int)(size * valid_ratio)]
    test_images = all_images[(int)(size * valid_ratio) + 1 : (int)(size * valid_ratio) + 1 + (int)(size * test_ratio)]
    
    for image_name in valid_images:
        source = dataset_dir + train_dir + '/' + class_name + '/' + image_name
        dest = dataset_dir + valid_dir + '/' + class_name + '/' + image_name
        shutil.move(source, dest)

    for image_name in test_images:
        source = dataset_dir + train_dir + '/' + class_name + '/' + image_name
        dest = dataset_dir + test_dir + '/' + class_name + '/' + image_name
        shutil.move(source, dest)