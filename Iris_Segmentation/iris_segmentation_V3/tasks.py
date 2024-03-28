import os
import argparse


# To run this code input the 
# the path to where the unsegmented casia lamp files are 
# the path to where you want the segmented images to be saved
# the path to where you want the .mf file to be saved
def main(input, output, task_file):
    # Base paths
    # base_input_path = "/home/daavallone/Iris-Recognition-Research-Capstone/CASIA-Iris-Lamp/"
    # base_output_path = "/home/daavallone/Iris-Recognition-Research-Capstone/Segmented-Casia-Iris-Lamp/"
    count = 1

    # File to write tasks to
    # output_file_path = "iris_segmentation_V3/full.mf"

    file_path = "Iris-Recongnition-Research-Capstone/ris_Segmentation/iris_segmentation_V3/main.py"
    dirr = "Iris-Recongnition-Research-Capstone/Iris_Segmentation/iris_segmentation_V3"
    task_file = os.path.join(dirr, task_file)
    # Open the file in write mode
    with open(task_file, "w") as output_file:
        # Iterate over 10 tasks
        for i in range(1, 207):
            # Iterate over "L" and "R" directories
            for side in ["L", "R"]:
                # Generate input and output paths
                input_path = os.path.join(input, "{:03d}".format(i), side)
                output_path = os.path.join(output, "{:03d}".format(i), side)

                # Create task command
                task = f"task{count}:\n"
                task_command = f"python {file_path} --r 100 --p {input_path} --e jpg --o {output_path} > task{count}\n"

                # Write the task to the file
                output_file.write(task)
                output_file.write("\t" + task_command.replace("\\", "/"))
                count += 1

    print(f"Tasks written to {task_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate tasks for processing images.")
    parser.add_argument("input", type=str, help="Input image directory path")
    parser.add_argument("output", type=str, help="Output image directory path")
    parser.add_argument("task_file", type=str, help=".mf file path")
    args = parser.parse_args()

    main(args.input, args.output, args.task_file)