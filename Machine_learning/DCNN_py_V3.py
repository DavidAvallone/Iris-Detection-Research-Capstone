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

directory = "Segmented-Casia-Iris-Lamp"

checkpoint_path = "training_3/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

num_classes = 822

batch_size = 32

cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath = checkpoint_path,
    verbose = 1,
    save_weights_only = True,
    save_freq = 5
)
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

model.save_weights(checkpoint_path.format(epoch=0))

model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    epochs=10)
model.save('model3.keras')