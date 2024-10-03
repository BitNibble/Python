#python -V
#Python the lazy mans programming language
#cd "pyhton/test-2"
#python -u test.py
#pip3 install numpy
#pip3 show numpy
#python -m pip install numpy
#pip3 install --upgrade numpy
#python -m pip install pandas
#python -m pip install scipy
#python -m pip install matplotlib
#python -m pip install sklearn
############################################################
import sys
assert sys.version_info >= (3, 5)
import os
#import urllib
import urllib.request
#from urllib.request import urlretrieve
import numpy as np
import pandas as pd
import scipy as sp
#import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import sklearn
assert sklearn.__version__ >= "0.20"
#import sklearn.linear_model
#import pyfits
import matplotlib as mpl
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
############################################################
############################################################
# Download the data
datapath = os.path.join("datasets", "lifesat", "")
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
os.makedirs(datapath, exist_ok=True)
for filename in ("oecd_bli_2015.csv", "gdp_per_capita.csv"):
    print("Downloading", filename)
    url = DOWNLOAD_ROOT + "datasets/lifesat/" + filename
    urllib.request.urlretrieve(url, datapath + filename)



#############################################################