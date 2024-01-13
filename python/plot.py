import numpy as np
import matplotlib.pyplot as plt

# Set the size of the plot
width, height = 800, 800

# Define the region of the complex plane we're interested in
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5

# Generate a grid of complex numbers
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Initialize the Mandelbrot image
image = np.zeros(Z.shape, dtype=float)
max_iter = 100

# Compute the Mandelbrot set
for i in range(width):
    for j in range(height):
        c = Z[j, i]
        z = 0
        for k in range(max_iter):
            z = z**2 + c
            if abs(z) > 2.0:
                image[j, i] = k
                break

# Plot the Mandelbrot set
plt.imshow(image, extent=(xmin, xmax, ymin, ymax), cmap='hot')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.show()
