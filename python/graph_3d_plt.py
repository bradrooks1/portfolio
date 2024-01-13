import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generating random data for demonstration
np.random.seed(0)

df = pd.DataFrame({
    'x': np.random.randint(1, 100, 100),
    'y': np.random.randint(1, 100, 100),
    'z': np.random.randint(1, 100, 100)
})

# Creating a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['x'], df['y'], df['z'])

# Setting labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Display the plot
plt.show()
