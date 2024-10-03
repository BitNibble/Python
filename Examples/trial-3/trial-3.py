#python -V
#cd "pyhton/trial-3"
#python -u test.py
#pip3 install numpy
#pip3 show numpy
#python -m pip install --upgrade pip
#python -m pip install numpy
#pip3 install --upgrade numpy
#python -m pip install pandas
#python -m pip install scipy
#python -m pip install matplotlib
############################################################
# Import necessary libraries
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pylab as plt
from astropy.io import fits  # Use astropy instead of pyfits

# Print SciPy version
print("SciPy version:", sp.version.version)

# Create a simple sequence from 0 to 99
n = np.arange(100)

# Create a Primary HDU (Header/Data Unit) using astropy
hdu = fits.PrimaryHDU(n)

# Optionally, you can create a FITS file to save the HDU
hdulist = fits.HDUList([hdu])  # Create an HDU list with the primary HDU
hdulist.writeto('output.fits', overwrite=True)  # Write to a FITS file

print("FITS file 'output.fits' created with data.")








