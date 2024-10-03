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
# Import necessary libraries
import pandas as pd                   # For data manipulation
import numpy as np                    # For numerical operations
import matplotlib.pyplot as plt        # For plotting
import sklearn.linear_model            # For linear regression model

def prepare_country_stats(oecd_bli, gdp_per_capita):
    """
    Prepares country statistics by merging OECD life satisfaction data 
    with GDP per capita data.
    
    Parameters:
    - oecd_bli: DataFrame containing OECD life satisfaction data
    - gdp_per_capita: DataFrame containing GDP per capita data
    
    Returns:
    - A DataFrame containing GDP per capita and life satisfaction for selected countries.
    """
    # Filter for total inequality
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
    
    # Pivot the DataFrame
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    
    # Rename GDP per capita column for clarity
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    
    # Set country as index for merging
    gdp_per_capita.set_index("Country", inplace=True)
    
    # Merge the two DataFrames on the index (Country)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                   left_index=True, right_index=True)
    
    # Sort by GDP per capita
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    
    # Remove specific indices (countries)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    
    # Return the filtered DataFrame with selected columns
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]

# Load the data
try:
    oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')  # Ensure this file exists
    gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")  # Ensure this file exists

    # Prepare the data
    country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
    
    # Prepare the feature (X) and target (Y) variables
    X = np.c_[country_stats["GDP per capita"]]                # Reshape GDP data for regression
    Y = np.c_[country_stats["Life satisfaction"]]             # Reshape life satisfaction data for regression

    # Visualize the data
    country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
    plt.title('GDP per Capita vs. Life Satisfaction')
    plt.xlabel('GDP per Capita')
    plt.ylabel('Life Satisfaction')
    plt.show()

    # Select a linear regression model
    model = sklearn.linear_model.LinearRegression()

    # Train the model on the data
    model.fit(X, Y)

    # Make a prediction for Cyprus
    X_new = [[22587]]  # Cyprus GDP per capita
    prediction = model.predict(X_new)  # Outputs predicted life satisfaction
    print(f"Predicted life satisfaction for Cyprus: {prediction[0][0]:.2f}")

except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

###############################





