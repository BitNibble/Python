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
import numpy as np                     # For numerical operations
import matplotlib.pyplot as plt         # For plotting
import sklearn.linear_model             # For linear regression model

# Prepare the data
x = np.array([[1], [2], [3], [4], [5], 
              [6], [7], [8], [9], [10], 
              [11], [12], [13], [14], [15], 
              [20], [25], [30]])  # x values
y = np.array([[1], [4], [9], [16], [25], 
              [36], [49], [64], [81], [100], 
              [121], [144], [169], [196], [225], 
              [400], [625], [900]])  # y values (x squared)

# Alternatively creating x and y using a range
# Uncomment if you prefer to generate x and y dynamically
# x = np.array([list(range(1, 15)) + list(range(15, 31, 5))]).reshape(-1, 1)
# y = x ** 2

# Create and fit the linear regression model
m = sklearn.linear_model.LinearRegression()
m.fit(x, y)

# Make predictions
pred_10 = m.predict([[10]])  # Predict for x = 10
pred_35 = m.predict([[35]])  # Predict for x = 35

# Print predictions
print(f"Prediction for x=10: {pred_10[0][0]:.2f}")  # Outputs predicted y for x = 10
print(f"Prediction for x=35: {pred_35[0][0]:.2f}")  # Outputs predicted y for x = 35

# Visualize the data and predictions
plt.figure(figsize=(10, 6))
plt.plot(x, y, "o", label='Data Points (x vs y)')
plt.xlabel("x", fontsize=16)
plt.ylabel("y", rotation=0, fontsize=16)

# Generate new x values for smooth line plotting
xs = np.linspace(0, 30, 100).reshape(-1, 1)
ys = m.predict(xs)  # Predicted y values for the smooth line

# Plot the regression line
plt.plot(xs, ys, color='r', label='Regression Line')
plt.title('Linear Regression: Predicting y from x', fontsize=18)
plt.legend()
plt.grid(True)
plt.show()  # Display the plot
