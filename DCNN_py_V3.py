import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.utils import to_categorical

import os
import random
import shutil
import PIL
from PIL import Image
# https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image/ImageDataGenerator

"""
    Split the dataset into training and testing sets.

    """
def split_dataset(directory, ratio=0.8):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg'):
                file_path = os.path.join(root, file)
                all_files.append(file_path)

    random.shuffle(all_files)

    split_idx = int(len(all_files) * ratio)
    train_files = all_files[:split_idx]
    test_files = all_files[split_idx:]

    return train_files, test_files


def combine_subdirectories(main_dir):
    
    for subdir in os.listdir(main_dir):
        subdir_path = os.path.join(main_dir, subdir)
        if os.path.isdir(subdir_path):
            subdirs = [os.path.join(subdir_path, subsubdir) for subsubdir in os.listdir(subdir_path)]
            if all(os.path.isdir(path) for path in subdirs):
                for file in os.listdir(subdirs[1]):
                    src = os.path.join(subdirs[1], file)
                    dst = os.path.join(subdirs[0], file)
                    shutil.move(src, dst)
                # Remove the now empty second subdirectory
                os.rmdir(subdirs[1])

# this was a test but i think its useless
directory = "Segmented-Casia-Iris-Lamp"
combine_subdirectories(directory)
train_files, test_files = split_dataset(directory, ratio=0.7)

print("Number of training files:", len(train_files))
print("Number of testing files:", len(test_files))

num_classes = 822
model = models.Sequential()

# increasing the number of layers
# increase the kernel size
model.add(layers.Conv2D(32, (5, 5), activation='relu', input_shape=(480, 640, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (5, 5), activation='relu', groups=1))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (5, 5), activation='relu', groups=1))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(256, (5, 5), activation='relu', groups=1))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())

# adding a dropout layer to try to avoid overfitting
model.add(layers.Dropout(0.5))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))

# using the adam optimizer again
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# model.summary()

img_height = 480
img_width = 640
input_shape = (img_height, img_width, 3) 

batch_size = 32

train_datagen = ImageDataGenerator(
    validation_split=0.2,
    )

# train_datagen.fit(train_files)

train_generator = train_datagen.flow_from_directory(
    directory,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='sparse',
    subset='training')

validation_generator = train_datagen.flow_from_directory(
    directory,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='sparse',
    subset='validation')

model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    epochs=10)