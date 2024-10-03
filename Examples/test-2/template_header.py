#python -V
#Python the lazy mans programming language
#cd "pyhton/template_header"
#python -m pip --version
#python -m pip install --user -U pip
#python -m pip install --user -U virtualenv
#python -m pip install -U jupyter matplotlib numpy pandas scipy scikit-learn
#python -c "import jupyter, matplotlib, numpy, pandas, scipy, sklearn"
#python -u test.py
#pip3 install numpy
#pip3 show numpy
#python -m pip install numpy
#pip3 install --upgrade numpy
#python -m pip install pandas
#python -m pip install scipy
#python -m pip install matplotlib
#python -m pip install sklearn
#pip install pyinstaller
#pip install numpy
#pip install --upgrade pygame numpy pandas matplotlib scikit-learn
#pip install astropy
############################################################
############################################################
# Ensure we are using Python version 3.5 or higher
import sys
assert sys.version_info >= (3, 5)

# Import necessary libraries
import os                          # Provides functions to interact with the operating system
import urllib.request              # Module for opening and reading URLs
from urllib.request import urlretrieve  # Function to download files from a given URL
import numpy as np                 # Library for numerical operations and handling arrays
import pandas as pd                # Library for data manipulation and analysis using DataFrames
import scipy as sp                 # Library for scientific computing, includes modules for optimization, integration, etc.
import matplotlib.pyplot as plt     # Module for creating static, animated, and interactive visualizations
import matplotlib as mpl            # Core matplotlib library to configure default settings
import sklearn                     # Scikit-learn, a library for machine learning

# Check that the installed version of scikit-learn is at least 0.20
assert sklearn.__version__ >= "0.20"

# Set default font sizes for matplotlib plots
mpl.rc('axes', labelsize=14)      # Set axes label size
mpl.rc('xtick', labelsize=12)     # Set x-tick label size
mpl.rc('ytick', labelsize=12)     # Set y-tick label size

import tarfile                     # Module for reading and writing tar archives
# import pyfits                    # Uncomment this if working with FITS files (use astropy.io.fits instead)
import pygame                      # Library for creating video games
import tkinter as tk               # Standard GUI toolkit for Python, useful for creating desktop applications
import hashlib                     # Library for hashing messages, useful for data integrity checks

##############################################################
##############################################################
# Write your code here:





























##############################################################
