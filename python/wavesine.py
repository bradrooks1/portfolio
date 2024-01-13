import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and an axes
fig, ax = plt.subplots()

# Set up the axes limits
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Initialize a line plot
line, = ax.plot([], [], lw=2)

# Function to generate frame data
def animate(i):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x + i * 0.1)  # Shift the sine wave
    line.set_data(x, y)
    return line,

# Create an animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=2, blit=True)

# Show the animation
plt.show()
