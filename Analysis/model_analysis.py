import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import preprocess_input
from keras.models import load_model


import os
import random
import shutil
import PIL
from PIL import Image

import numpy as np
import sklearn.metrics
from sklearn.metrics import classification_report, confusion_matrix

'''
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(480, 640, 3)))
model.add(layers.Conv2D(64, (3, 3), activation='relu', groups=1))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu', groups=1))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(822, activation='softmax'))

# Restore the weights
model.load_weights("model1.keras")
model.compile()
'''

model = load_model("model1.keras")


directory = "../Segmented-Casia-Iris-Lamp-New-Test"

batch_size = 32
img_height = 480
img_width = 640
input_shape = (img_height, img_width, 3) 

test_datagen = ImageDataGenerator()

test_generator = test_datagen.flow_from_directory(
    directory,
    target_size=(img_height, img_width),
    batch_size = batch_size,
    class_mode='sparse')


#predictions = model.predict(test_generator)
#predicted_classes = np.argmax(predictions, axis=1)
#true_classes = test_generator.classes
#class_labels = list(test_generator.class_indices.keys())

# Evaluate the model
results = model.evaluate(test_generator, verbose=2)
print("Restored model results, ", results)
'''
cm = confusion_matrix(true_classes, predicted_classes)

cr = classification_report(true_classes, predicted_classes, target_names=class_labels)

print("Confusion Matrix:")
print(cm)

print("\nClassification Report:")
print(cr)'''