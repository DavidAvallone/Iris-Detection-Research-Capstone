import os

# Base paths
base_input_path = "/Users/daavallone/cs496/Iris-Recognition-Research-Capstone/CASIA-Iris-Lamp/"
base_output_path = "/Users/daavallone/cs496/Iris-Recognition-Research-Capstone/Segmented-Casia-Iris-Lamp/"

# Iterate over 10 tasks
for i in range(1, 11):
    # Iterate over "L" and "R" directories
    for side in ["L", "R"]:
        # Generate input and output paths
        input_path = os.path.join(base_input_path, "{:03d}".format(i), side)
        output_path = os.path.join(base_output_path, "{:03d}".format(i), side)

        # Create task command
        task_command = f"python /Users/daavallone/cs496/Iris-Recognition-Research-Capstone/iris_segmentation_V3/main.py --r 100 --p {input_path} --e png --o {output_path} > task{i}_{side}"

        # Print the task
        print(f"task{i}_{side}:\n\t{task_command}")