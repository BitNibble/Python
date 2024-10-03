# Import necessary libraries
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pylab as plt

# Check SciPy version
print("SciPy version:", sp.version.version)

# Demonstrating NumPy functionality
a = np.array([1, 2, 3])
print("Array a:", a)
print("Type of a:", type(a))

b = np.array((3, 4, 5))
print("Array b:", b)
print("Type of b:", type(b))

# Create and display various NumPy arrays
ones_array = np.ones((3, 4), dtype=np.int16)
print("Ones array:\n", ones_array)

full_array = np.full((3, 4), 0.11)
print("Full array:\n", full_array)

arange_array = np.arange(10, 30, 5)
print("Arange array:", arange_array)

linspace_array = np.linspace(0, 5/3, 6)
print("Linspace array:", linspace_array)

random_array = np.random.rand(2, 3)
print("Random array:\n", random_array)

empty_array = np.empty((2, 3))
print("Empty array:\n", empty_array)

# Modify an existing array
c = np.array([1, 2, 5, 7, 8])
c[1:3] = -1
print("Modified array c:", c)

# Demonstrating Pandas functionality
people_dict = {
    "weight": pd.Series([68, 83, 112], index=["alice", "bob", "charles"]),
    "birthyear": pd.Series([1984, 1985, 1992], index=["bob", "alice", "charles"], name="year"),
    "children": pd.Series([0, 3], index=["charles", "bob"]),
    "hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]),
}

people = pd.DataFrame(people_dict)
print("People DataFrame:\n", people)

# Demonstrating Matplotlib functionality
t = np.linspace(0, 1, 100)  # Changed from sp.linspace to np.linspace
plt.plot(t, t**2)
plt.xlabel('t')
plt.ylabel('t^2')
plt.title('Plot of t^2')
plt.show()
