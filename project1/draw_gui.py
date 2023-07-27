import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
import inspect
import multimodal_functions

def plot_function(function, x_range, y_range, cmap, ax):
    ax.clear()

    x = np.linspace(*x_range, 200)
    y = np.linspace(*y_range, 200)
    x, y = np.meshgrid(x, y)

    z = function(x, y)

    ax.plot_surface(x, y, z, cmap=cmap)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'{function.__name__.capitalize()} Function')

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
    colormaps = ['viridis', 'hot', 'cool', 'autumn', 'winter']

    root = tk.Tk()
    root.geometry('800x600')

    # Set grid
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    # Set up plot area
    fig = plt.Figure()
    ax = fig.add_subplot(111, projection='3d')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, sticky='nsew')

    # Set up control panel
    control_frame = tk.Frame(root)
    control_frame.grid(row=0, column=0, sticky='nsew')

    tk.Label(control_frame, text="Function:").grid(row=0, column=0)

    function_var = tk.StringVar()
    function_dropdown = ttk.Combobox(control_frame, textvariable=function_var, width=15)
    function_dropdown['values'] = list(functions.keys())
    function_dropdown.current(0)
    function_dropdown.grid(row=0, column=1)

    tk.Label(control_frame, text="x_range:").grid(row=0, column=2)

    lower_x_entry = tk.Entry(control_frame, width=5)
    upper_x_entry = tk.Entry(control_frame, width=5)

    lower_x_entry.grid(row=0, column=3)
    tk.Label(control_frame, text="to").grid(row=0, column=4)
    upper_x_entry.grid(row=0, column=5)

    tk.Label(control_frame, text="y_range:").grid(row=0, column=6)

    lower_y_entry = tk.Entry(control_frame, width=5)
    upper_y_entry = tk.Entry(control_frame, width=5)

    lower_y_entry.grid(row=0, column=7)
    tk.Label(control_frame, text="to").grid(row=0, column=8)
    upper_y_entry.grid(row=0, column=9)

    tk.Label(control_frame, text="Color Map:").grid(row=0, column=10)

    cmap_var = tk.StringVar()
    cmap_dropdown = ttk.Combobox(control_frame, textvariable=cmap_var, width=5)
    cmap_dropdown['values'] = colormaps
    cmap_dropdown.current(0)
    cmap_dropdown.grid(row=0, column=11)

    def plot_button_callback():
        function_name = function_var.get()
        x_range = [float(lower_x_entry.get()), float(upper_x_entry.get())]
        y_range = [float(lower_y_entry.get()), float(upper_y_entry.get())]
        cmap = cmap_var.get()
        plot_function(functions[function_name], x_range, y_range, cmap, ax)
        canvas.draw()

    plot_button = tk.Button(control_frame, text="Plot", command=plot_button_callback)
    plot_button.grid(row=0, column=12)

    root.mainloop()
