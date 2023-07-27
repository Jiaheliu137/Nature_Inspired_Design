import multimodal_functions
import inspect

def get_function_dict(module):
    function_dict = {}
    for f in dir(module):
        if not f.startswith("__"):  
            func = getattr(module, f)
            if callable(func) and len(inspect.signature(func).parameters) >= 2:
                function_dict[f] = func
    return function_dict

functions = get_function_dict(multimodal_functions)

print(functions)