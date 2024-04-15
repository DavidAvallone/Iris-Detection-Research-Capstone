import os
import shutil

# Path to the original directory
original_dir = 'Segmented-Casia-Iris-Lamp'

# Path to the new directory
new_dir = 'Segmented-Casia-Iris-Lamp-New'

# Create the new directory if it doesn't exist
os.makedirs(new_dir, exist_ok=True)

# Iterate over each subdirectory
for subdir in os.listdir(original_dir):
    subdir_path = os.path.join(original_dir, subdir)
    if os.path.isdir(subdir_path):
        # Create new subdirectories
        new_subdir_L = os.path.join(new_dir, f'{subdir}_L')
        new_subdir_R = os.path.join(new_dir, f'{subdir}_R')
        os.makedirs(new_subdir_L, exist_ok=True)
        os.makedirs(new_subdir_R, exist_ok=True)
        
        # Copy contents of 'L' and 'R' into their respective new folders
        for subsubdir in os.listdir(subdir_path):
            subsubdir_path = os.path.join(subdir_path, subsubdir)
            if os.path.isdir(subsubdir_path):
                if subsubdir == 'L':
                    for item in os.listdir(subsubdir_path):
                        item_path = os.path.join(subsubdir_path, item)
                        shutil.copy(item_path, new_subdir_L)
                elif subsubdir == 'R':
                    for item in os.listdir(subsubdir_path):
                        item_path = os.path.join(subsubdir_path, item)
                        shutil.copy(item_path, new_subdir_R)
print("Completed")