import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Game of Life settings
GRID_SIZE = (100, 100)
ON = 255  # cell is alive
OFF = 0   # cell is dead
vals = [ON, OFF]

# Populate grid with random on/off - more off than on
grid = np.random.choice(vals, GRID_SIZE[0] * GRID_SIZE[1], p=[0.2, 0.8]).reshape(GRID_SIZE[0], GRID_SIZE[1])

def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation and we go line by line 
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):

            # compute 8-neghbor sum using toroidal boundary conditions - x and y wrap around 
            # so that the simulaton takes place on a toroidal surface.
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)

            # apply Conway's rules
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

# set up animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, GRID_SIZE[0]), frames=10, interval=50, save_count=50)

# To save the animation, use the following line
ani.save('game_of_life.gif', writer='imagemagick', fps=30)

plt.show()
