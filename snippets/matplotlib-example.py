# coding: utf-8
"""
Matplotlib example
Dependencies: Python, NumPy, matplotlib
"""
 
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
 
# Calculate spiral coordinates 
theta = np.linspace(-8 * np.pi, 8 * np.pi, 200) 
z = np.linspace(-3, 0, 200)
r = 5
x = r * np.sin(theta)*z
y = r * np.cos(theta)*z
 
# Use matplotib and its OOP interface to draw it 
fig = plt.figure() # Create figure
ax = fig.gca(projection='3d') # 3D
ax.view_init(15, 0) # Set view angle
ax._axis3don = False # Hide the 3d axes
 
# Plot figure
ax.plot(x, y, z,
        c='green', linewidth=2.5)
 
# Add a new plot 
ax.scatter(0, 0, 0.2,
           c='red', s=250, marker='*')
 
# Type here your best whishes
ax.set_title(u"title_text")
 
plt.show()