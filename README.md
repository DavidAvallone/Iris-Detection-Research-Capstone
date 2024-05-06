# Iris-Recognition-Research-Capstone

# Contributors
**David Avallone & Kelly Reynolds**

**Client: Dr. Bui**

# Project Description
This project utilizes iris recognition that detect and classify the iris images through the use of computer vision and machine learning. The computer vision program detects the iris and isolates it from the original image of the eye. These iris images will then be used to train and test various machine learning models. We will utilize many machine learning algorithms to determine which will be the best for the iris detection. We will also attempt speed optimizations on these models. Finally, we will conduct an analysis on the data and use the results to answer various questions about the data.

# Installation Instructions
Install Anaconda Python Environment Software
python 3.9
Add open-cv, numpy, pillow, keras, tensorflow, scikit-learn, and matplotlib to the environment

# How to Run
Using the environment as the kernel run the files alongside the dataset in a local directory.
Iris segmentation: 
Process 1 & 2: Load up jupyter notebooks and run them block by block
Process 3: run python main.py --r 100 --p /directory/containing/images --e png --o output/directory/name

Machine Learning:
First the dataset needs to be reformatted using the file fix_data.py there is no command line input so fix directory within file.
Next run the train_test_split.py file on the output of fix_data making sure to update the directory variables in the file.
Now that you have the fixed and split data you are now able to start running and training the models.
Run python DCNN_py_New.py model_num training/dataset
Run python smaller_models.py model_num training/dataset

# How to Test
Model Analysis:
Load in keras files in the model_analysis.ipynb file and add that models architecure and run the block on the test data, see examples in the file
