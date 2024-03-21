import os

# Base paths
base_input_path = "/home/daavallone/Iris-Recognition-Research-Capstone/CASIA-Iris-Lamp/"
base_output_path = "/home/daavallone/Iris-Recognition-Research-Capstone/Segmented-Casia-Iris-Lamp/"
count = 1

# File to write tasks to
output_file_path = "iris_segmentation_V3/full.mf"

# Open the file in write mode
with open(output_file_path, "w") as output_file:
    # Iterate over 10 tasks
    for i in range(1, 412):
        # Iterate over "L" and "R" directories
        for side in ["L", "R"]:
            # Generate input and output paths
            input_path = os.path.join(base_input_path, "{:03d}".format(i), side)
            output_path = os.path.join(base_output_path, "{:03d}".format(i), side)

            # Create task command
            task = f"task{count}:\n"
            task_command = f"python /home/daavallone/Iris-Recognition-Research-Capstone/iris_segmentation_V3/main.py --r 100 --p {input_path} --e jpg --o {output_path} > task{count}\n"

            # Write the task to the file
            output_file.write(task)
            output_file.write(task_command.replace("\\", "/"))
            count += 1

print(f"Tasks written to {output_file_path}")