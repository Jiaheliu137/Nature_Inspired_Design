import argparse

parser = argparse.ArgumentParser(description='Configuration file')
arg_lists = []


def add_argument_group(name):
    # Create a new group of arguments.
    arg = parser.add_argument_group(name)
    arg_lists.append(arg)
    return arg


# Data
data_arg = add_argument_group('Data')
data_arg.add_argument('-cn', '--city_num', type=int, default=20, help='Number of cities')  # Number of cities
data_arg.add_argument('-d', '--dimension', type=int, default=2, help='Coordinate dimension')  # Coordinate dimension
data_arg.add_argument('-in', '--individual_num', type=int, default=60, help='Number of individuals')  # Number of individuals
data_arg.add_argument('-gn', '--gen_num', type=int, default=400, help='Number of generations')  # Number of generations
data_arg.add_argument('-mp', '--mutate_prob', type=float, default=0.25, help='Probability of mutation')  # Mutation probability
data_arg.add_argument('-f', '--frames', type=int, default=20, help='frames of animation')  # frames of animation

def get_config():
    # Parse the arguments and return the configuration
    config, unparsed = parser.parse_known_args()
    return config


def print_config():
    config = get_config()
    print('\n')
    print('Data Config:')
    print('* Number of cities:', config.city_num)
    print('* Number of individuals:', config.individual_num)
    print('* Number of generations:', config.gen_num)
    print('* Mutation probability:', config.mutate_prob)
    print('* frames of animation', config.frames)
