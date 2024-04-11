import os
import random
import shutil

# Path to the main directory
main_dir = "Segmented-Casia-Iris-Lamp-New"

# Get all subdirectories
subdirs = [d for d in os.listdir(main_dir) if os.path.isdir(os.path.join(main_dir, d))]

# Shuffle subdirectories
random.shuffle(subdirs)

# Get the total number of subdirectories
num_subdirs = len(subdirs)

# Ask user for the test-train split percentage
split_percentage = float(input("Enter the test-train split percentage (e.g., 0.2 for 20%): "))

# Calculate the number of subdirectories for the test set
num_test = int(num_subdirs * split_percentage)

# Create test and train directories
test_dir = "Segmented-Casia-Iris-Lamp-New-Train"
train_dir = "Segmented-Casia-Iris-Lamp-New-Test"
os.makedirs(test_dir, exist_ok=True)
os.makedirs(train_dir, exist_ok=True)

# Move subdirectories to test and train directories
for i, subdir in enumerate(subdirs):
    if i < num_test:
        shutil.move(os.path.join(main_dir, subdir), os.path.join(test_dir, subdir))
    else:
        shutil.move(os.path.join(main_dir, subdir), os.path.join(train_dir, subdir))

print("Split completed successfully.")