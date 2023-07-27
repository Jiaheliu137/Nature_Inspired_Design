import numpy as np
import config as conf
from utils import EP
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import os



config = conf.get_config()

frames = config.frames

# Building a matrix to store the distances between all pairs of cities.
def build_dist_mat(input_list):
    n = config.city_num
    dist_mat = np.zeros([n, n])
    for i in range(n):
        for j in range(i + 1, n):
            d = input_list[i, :] - input_list[j, :]
            dist_mat[i, j] = np.sqrt(np.dot(d, d))
            dist_mat[j, i] = dist_mat[i, j]
    return dist_mat

# Initialize the city position list randomly
city_pos_list = np.random.rand(config.city_num, config.dimension)

# Get the distance matrix between cities
city_dist_mat = build_dist_mat(city_pos_list)

# Print out the position of each city
for i, city_pos in enumerate(city_pos_list):
    print(f'City {i}: {city_pos}')

# Start the Evolutionary Programming algorithm
EP = EP(city_dist_mat)

# Get the list of shortest path and fitness value of each generation
result_list, fitness_list = EP.train() 

print(f'Optimal path: {result_list[-1]}')
print(f'Shortest distance: {fitness_list[-1]:.4f}')

fig = plt.figure(figsize=(18, 7.5))

# Create the subplot for displaying the travel route
ax1 = fig.add_subplot(121, projection='3d' if config.dimension==3 else None)
ax1.set_title('Travel Route')
line = ax1.plot([], [], 'o-r' if config.dimension==2 else 'o-r')[0]

# Depending on the dimension, create the text for generation and shortest distance
if config.dimension==3:
    gen_text = ax1.text2D(0.02, 0.95, '', transform=ax1.transAxes)
else:
    gen_text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes) 

# Create the subplot for displaying the fitness curve
ax2 = fig.add_subplot(122)
ax2.set_title('Fitness Curve')
curve = ax2.plot([], [], 'r-', label='Shortest Distance')[0]

# Initialize the subplots
def init():
    # Depending on the dimension, set the initial state for line and ax1
    if config.dimension==3:  
        line.set_data(np.array([]), np.array([]))
        line.set_3d_properties(np.array([])) # set z axis data
        ax1.set_zlim(-0.05, 1.1)
    else:
        line.set_data([], [])
    curve.set_data([], []) # fitness graph
    gen_text.set_text('')  
    ax1.set_xlim(-0.05, 1.1)  
    ax1.set_ylim(-0.05, 1.1)  
    ax2.set_xlim(0, len(fitness_list))
    ax2.set_ylim(min(fitness_list), max(fitness_list))
    ax2.set_yticks(np.arange(math.floor(min(fitness_list))-1, math.ceil(max(fitness_list)), 0.5))
    return line, curve, gen_text,

# Update the subplots in each frame
def update(frame):

    # Update the travel route
    result = result_list[frame] # shortest path of the frame-th generation, is a series of indices
    result_pos_list = city_pos_list[result, :] # rearrange the coordinates according to the sequence of the shortest path
    if config.dimension == 2:
        line.set_data(result_pos_list[:, 0], result_pos_list[:, 1])
    else:
        line.set_data(result_pos_list[:, 0], result_pos_list[:, 1])
        line.set_3d_properties(result_pos_list[:, 2])  # Z axis
    gen_text.set_text(f'Generation: {frame}, Shortest Distance: {fitness_list[frame]:.4f}')  
    
    # Update the fitness curve
    curve.set_data(range(frame+1), fitness_list[:frame+1])
    
    # Add annotation for each city position
    for i, pos in enumerate(result_pos_list):
        if config.dimension == 2:
            ax1.annotate(str(result[i]), (pos[0], pos[1]), textcoords="offset points", xytext=(0,10), ha='center')
        else:
            ax1.text(pos[0], pos[1], pos[2], str(result[i]), color='blue')
            

    return line, curve, gen_text,

# Create the animation
ani = FuncAnimation(fig, update, frames=list(range(0, len(result_list), len(result_list)//frames)) + [len(result_list)-1], init_func=init, blit=False, repeat=False)

plt.show()


# # save anime in ./imgs
# folder_path = "./imgs"
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
# else:
#     pass

# if config.dimension == 3:
#     ani.save('./imgs/animation_3d.mp4', writer='ffmpeg')
# else:
#     ani.save('./imgs/animation_2d.mp4', writer='ffmpeg')

