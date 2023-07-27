from gui_utils import *
# from gui_utils import draw_gui
from other_utils import *
import multimodal_functions
import argparse
import inspect

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
    parser.add_argument('-f', '--function', default='ackley', type=str, help='Name of the {} function to plot (e.g., {}).'.format(len(functions.keys()), ', '.join(functions.keys())))
    parser.add_argument('-x', '--x_range', default=[-10, 10], nargs=2, type=float, help="The range of x-axis, input format: lower_bound upper_bound")
    parser.add_argument('-y', '--y_range', default=[-10, 10], nargs=2, type=float, help="The range of y-axis, input format: lower_bound upper_bound")
    parser.add_argument('-c', '--cmap', default='viridis', type=str, help='Color map to use for the plot. Some options are "viridis" (default), "hot", "cool", "autumn", "winter".')
    parser.add_argument('-g', '--gui', action='store_true', help='Run the program with a graphical user interface.')
    
    args = parser.parse_args()

    cmap = ['viridis', 'hot', 'cool', 'autumn', 'winter']

    if args.gui:
        draw_gui(functions, cmap)
    else:
        function_name = args.function.lower()
        if function_name in functions:
            plot_function(functions[function_name], args.x_range, args.y_range, args.cmap)
        else:
            print(f"Invalid function name. Available functions are: {', '.join(functions.keys())}")
