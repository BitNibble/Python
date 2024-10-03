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
############################################################
# Import necessary libraries
import os                           # For file and directory operations
import urllib.request               # For downloading files from the web
import tarfile                      # For handling tar files
import pandas as pd                 # For data manipulation and analysis
import matplotlib.pyplot as plt      # For data visualization

# Define constants for the housing data URL and local path
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """
    Fetches the housing data from the specified URL and extracts it into the local path.

    Parameters:
    - housing_url: URL to download the housing dataset.
    - housing_path: Local directory to save the dataset.
    """
    # Create the housing directory if it doesn't exist
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)

    # Define the path for the downloaded tar.gz file
    tgz_path = os.path.join(housing_path, "housing.tgz")

    # Download the housing data
    urllib.request.urlretrieve(housing_url, tgz_path)

    # Extract the tar.gz file
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

# Uncomment the line below to fetch the housing data
# fetch_housing_data()

def load_housing_data(housing_path=HOUSING_PATH):
    """
    Loads the housing data from a CSV file into a Pandas DataFrame.

    Parameters:
    - housing_path: Local path where the housing data is stored.

    Returns:
    - DataFrame containing the housing data.
    """
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

# Uncomment the line below to load the housing data
# housing = load_housing_data()

# Sample code to analyze and visualize the housing data
housing = load_housing_data()  # Load the housing data
print(housing.head())           # Display the first few rows of the dataset
print(housing.info())           # Get a summary of the dataset, including data types and non-null counts
print(housing["ocean_proximity"].value_counts())  # Count occurrences of each category in 'ocean_proximity'

# Plot histograms for numerical features
housing.hist(bins=50, figsize=(20, 15))
plt.title('Histograms of Housing Features')
plt.show()                     # Display the histograms

# Display descriptive statistics for the dataset
print(housing.describe())       # Show summary statistics for numeric columns






##############################################################
