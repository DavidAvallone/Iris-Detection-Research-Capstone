import os
import argparse

def main(arr, portnumber, dir, env):
    arr = [int(x) for x in arr.split(",")]
    for i in range(len(arr)):
        qsub_file_name = os.path.join(dir, f"node{arr[i]}.qsub")
        with open(qsub_file_name, "w") as file:
            file.write("#!/bin/bash\n")
            file.write(f"#PBS -l nodes={arr[i]}:ppn=1\n")
            file.write("#PBS -l walltime=2:00:00\n")
            file.write("#PBS -V\n\n")
            file.write("source ~/.bashrc\n")
            file.write("#cd $PBS_O_WORKDIR\n")
            file.write(f"conda activate {env}\n")
            file.write(f"cd {dir}\n")
            file.write(f"work_queue_worker master {portnumber}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate qsub files for each node count")
    parser.add_argument("arr", type=str, help="comma separated list of number of nodes")
    parser.add_argument("portnumber", type=int, help="port number")
    parser.add_argument("dir", type=str, help="the directory path to iris_segmentation_V3 this is where the qsubs will be written")
    parser.add_argument("env", type=str, help="env name")
    args = parser.parse_args()

    main(args.arr, args.portnumber, args.dir, args.env)