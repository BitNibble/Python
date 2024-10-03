# Check Python version
# python -V

# Change directory to where the script is located
# cd "python/trial-3"

# Run the script
# python -u test.py

# Install necessary libraries
# pip3 install numpy pandas scipy matplotlib

############################################################
# Import required libraries
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pylab as plt
import urllib.request  # Corrected import
import sys

# Print the version of SciPy
print("SciPy version:", sp.version.version)

############################################################
# Generate a simple sequence from 0 to 99
n = np.arange(100)

# URL of the dataset
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
               "databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# Read data from the URL
response = urllib.request.urlopen(target_url)  # Corrected function

# Arrange data into list for labels and list of lists for attributes
xList = []
labels = []

# Read and process each line in the dataset
for line in response:
    # Decode the bytes to string and split on comma
    row = line.decode('utf-8').strip().split(",")
    xList.append(row)

# Display number of rows and columns
sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[0])) + '\n')  # Corrected indexing to [0]
