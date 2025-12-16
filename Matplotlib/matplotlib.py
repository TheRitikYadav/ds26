import numpy as np

import matplotlib.pyplot as plt

# Basic Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
plt.title('Basic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

# Basic Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title('Basic Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

# Basic Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.figure()
plt.bar(categories, values)
plt.title('Basic Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid()
plt.show()

# Basic Histogram
data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.title('Basic Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid()
plt.show()