import numpy as np
import matplotlib.pyplot as plt

# Define the original function
def original_function(x):
    return np.sin(x)  # You can change this to any function

# Define the area calculation using the trapezoidal rule
def calculate_area_trapezoidal(func, x_start, x_end, num_intervals):
    x_values = np.linspace(x_start, x_end, num_intervals + 1)  # Include endpoint
    delta_x = (x_end - x_start) / num_intervals
    areas = np.zeros(num_intervals + 1)  # Store accumulated area

    for i in range(num_intervals):
        # Use the trapezoidal rule for area calculation
        areas[i + 1] = areas[i] + (func(x_values[i]) + func(x_values[i + 1])) / 2 * delta_x

    return x_values, areas

# Create a new function that represents the area using the trapezoidal rule
def area_function_trapezoidal(func, x_start, x_end, num_intervals):
    x_values, areas = calculate_area_trapezoidal(func, x_start, x_end, num_intervals)
    
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

# Create the area function using the trapezoidal rule
area_func_trap = area_function_trapezoidal(original_function, x_start, x_end, num_intervals)

# Generate values for the area function
x_values = np.linspace(x_start, x_end, 1000)
area_values_trap = np.array([area_func_trap(x) for x in x_values])

# Plot the original function and the area function using the trapezoidal rule
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_values, original_function(x_values), label='Original Function (sin(x))', color='blue')
plt.fill_between(x_values, original_function(x_values), color='lightblue', alpha=0.5)
plt.title('Original Function and Area Under the Curve')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_values, area_values_trap, label='Area Under the Curve (Trapezoidal)', color='orange')
plt.title('Area Function Using Trapezoidal Rule')
plt.xlabel('x')
plt.ylabel('Area')
plt.legend()

plt.tight_layout()
plt.show()
