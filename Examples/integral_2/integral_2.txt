import numpy as np
import matplotlib.pyplot as plt

# Define the original function
def original_function(x):
    return np.sin(x)  # You can change this to any function

# Define the area calculation using Riemann sums
def calculate_area(func, x_start, x_end, num_intervals):
    x_values = np.linspace(x_start, x_end, num_intervals + 1)  # Include endpoint
    delta_x = (x_end - x_start) / num_intervals
    areas = np.zeros(num_intervals + 1)  # Store accumulated area

    for i in range(num_intervals):
        # Use the left endpoint for Riemann sum
        areas[i + 1] = areas[i] + func(x_values[i]) * delta_x

    return x_values, areas

# Create a new function that represents the area
def area_function(func, x_start, x_end, num_intervals):
    x_values, areas = calculate_area(func, x_start, x_end, num_intervals)
    
    # Area function that returns the accumulated area at any given x
    def inner_area_function(x):
        if x < x_start or x > x_end:
            return None
        index = np.searchsorted(x_values, x)
        return areas[index]
    
    return inner_area_function

# Define the range and precision
x_start = 0
x_end = 10
num_intervals = 100  # Adjust this for more precision

# Create the area function
area_func = area_function(original_function, x_start, x_end, num_intervals)

# Generate values for the area function
x_values = np.linspace(x_start, x_end, 1000)
area_values = np.array([area_func(x) for x in x_values])

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
