import numpy as np
import matplotlib.pyplot as plt

# Define the original function
def original_function(x):
    return np.sin(x)  # You can change this to any function

# Define the range and resolution
x_start = 0
x_end = 10
num_points = 1000
x_values = np.linspace(x_start, x_end, num_points)

# Calculate the area under the curve using the trapezoidal rule
areas = np.zeros(num_points)
for i in range(1, num_points):
    areas[i] = areas[i-1] + (original_function(x_values[i-1]) + original_function(x_values[i])) * (x_values[i] - x_values[i-1]) / 2

# Create a new function that represents the area
def area_function(x):
    # Ensure x is within the defined range
    if x < x_start or x > x_end:
        return None
    # Find the index corresponding to x
    index = np.searchsorted(x_values, x)
    return areas[index]

# Generate values for the area function
area_values = np.array([area_function(x) for x in x_values])

# Plot the original function and the area function
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_values, original_function(x_values), label='Original Function (sin(x))', color='blue')
plt.fill_between(x_values, original_function(x_values), color='lightblue', alpha=0.5)
plt.title('Original Function and Area Under the Curve')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_values, area_values, label='Area Under the Curve', color='orange')
plt.title('Area Function')
plt.xlabel('x')
plt.ylabel('Area')
plt.legend()

plt.tight_layout()
plt.show()
