import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
import argparse
import inspect
import multimodal_functions



def plot_function(function, x_range, y_range, cmap):
    x = np.linspace(*x_range, 200)
    y = np.linspace(*y_range, 200)
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


def get_function_dict(module):
    function_dict = {}
    for f in dir(module):
        if not f.startswith("__"):  
            func = getattr(module, f)
            if callable(func) and len(inspect.signature(func).parameters) >= 2:
                function_dict[f] = func
    return function_dict


if __name__ == "__main__":
    
    functions = get_function_dict(multimodal_functions)

    parser = argparse.ArgumentParser(description="Plot multimodal functions.")
    parser.add_argument('-f', '--function', default='ackley', type=str, help='Name of the function to plot (e.g., {}).'.format(', '.join(functions.keys())))
    parser.add_argument('-x', '--x_range', default=[-10, 10], nargs=2, type=float, help="The range of x-axis, input format: lower_bound upper_bound")
    parser.add_argument('-y', '--y_range', default=[-10, 10], nargs=2, type=float, help="The range of y-axis, input format: lower_bound upper_bound")
    parser.add_argument('-c', '--cmap', default='viridis', type=str, help='Color map to use for the plot. Some options are "viridis" (default), "hot", "cool", "autumn", "winter".')

    
    args = parser.parse_args()
    
    function_name = args.function.lower()
    if function_name in functions:
        plot_function(functions[function_name], args.x_range, args.y_range, args.cmap)
    else:
        print(f"Invalid function name. Available functions are: {', '.join(functions.keys())}")
