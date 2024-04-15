import os
import random
import shutil

def copy_random_images(source_dir, dest_dir, num_images=6):
    # Create the destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Iterate over each subdirectory
    for subdir in os.listdir(source_dir):
        subdir_path = os.path.join(source_dir, subdir)
        if os.path.isdir(subdir_path):
            # Create a new subdirectory in the destination directory
            dest_subdir = os.path.join(dest_dir, subdir)
            os.makedirs(dest_subdir, exist_ok=True)
            
            # Get a list of all image files in the subdirectory
            image_files = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f))]
            
            # Select 6 random images (or all images if there are less than 6)
            selected_images = random.sample(image_files, min(num_images, len(image_files)))
            
            # Copy the selected images to the destination directory
            for image in selected_images:
                image_path = os.path.join(subdir_path, image)
                dest_path = os.path.join(dest_subdir, image)
                shutil.copy(image_path, dest_path)

# Path to the original directory
source_dir = 'Segmented-Casia-Iris-Lamp-New'

# Path to the new directory where the random images will be saved
dest_dir = 'Segmented-Casia-Iris-Lamp-New-Test'

# Copy 6 random images from each subdirectory to the new directory
copy_random_images(source_dir, dest_dir)
print('Completed')