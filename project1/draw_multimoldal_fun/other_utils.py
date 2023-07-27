import numpy as np
import matplotlib.pyplot as plt

def plot_function(function, x_range, y_range, cmap):
    x = np.linspace(*x_range, 20 * int(abs(x_range[1] - x_range[0])))
    y = np.linspace(*y_range, 20 * int(abs(y_range[1] - y_range[0])))
    x, y = np.meshgrid(x, y)
    
    z = function(x, y)

    fig = plt.figure(figsize=(16, 10))
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.plot_surface(x, y, z, cmap=cmap)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title(f'{function.__name__.capitalize()} Function')

    plt.show()


