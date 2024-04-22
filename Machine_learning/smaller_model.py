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
import argparse

def model_one(model, num_classes):
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(480, 640, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu', groups=1))
    model.add(layers.MaxPooling2D((2, 2)))
    # model.add(layers.Conv2D(128, (3, 3), activation='relu', groups=1))
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(num_classes, activation='softmax'))
    return model


def finish_model(model, model_num, directory, batch_size):
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    img_height = 480
    img_width = 640
    input_shape = (img_height, img_width, 3) 

    train_datagen = ImageDataGenerator(
        validation_split=0.2,
        )

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
    
    model_name = 'model' + str(model_num) + '.keras'
    model.save(model_name)


def main(model_num, dir):
    directory = dir

    num_classes = 820

    batch_size = 32
    model = models.Sequential()

    if(model_num == 1):
        model_one(model, num_classes)
    elif(model_num == 2):
        model_two(model, num_classes)
    elif(model_num == 3):
        model_three(model, num_classes)
    else:
        exit()
    
    finish_model(model, model_num, directory, batch_size)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Choose which model to run")
    parser.add_argument("model_num", type=int, help="which model number to run")
    parser.add_argument("dir", type=str, help="which directory for dataset")
    args = parser.parse_args()

    main(args.model_num, args.dir)