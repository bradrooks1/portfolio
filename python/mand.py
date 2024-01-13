import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to check if a point is in the Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Function to create a grid of values
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    C = np.array([x + 1j*yi for yi in y])
    N = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            N[i, j] = mandelbrot(C[i, j], max_iter)
    return N

# Animation function
def animate(i):
    zoom_factor = 1.5 ** i
    width, height = 800, 800
    max_iter = 100
    extent = (-2, 1, -1.5, 1.5)

    xmin, xmax, ymin, ymax = [e / zoom_factor for e in extent]
    mandel = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    im.set_data(mandel)
    im.set_extent((xmin, xmax, ymin, ymax))
    return im,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.axis('off')

# Initialize the image
width, height = 800, 800
max_iter = 100
mandel = mandelbrot_set(-2, 1, -1.5, 1.5, width, height, max_iter)
im = ax.imshow(mandel, extent=(-2, 1, -1.5, 1.5), cmap='hot')

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=60, interval=100, blit=True)

# Show the animation
plt.show()
