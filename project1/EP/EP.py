import numpy as np
import matplotlib.pyplot as plt
import time
from multimodal_functions import *


# Fitness function (We aim to minimize the objective function, therefore fitness is the negative value of the objective function)
def get_fitness(pred): return -pred

def select(pop, F, method='roulette'):
    if method == 'roulette':
        F -= F.min()  # Make sure all fitness values are non-negative
        F /= F.sum()  # Normalize
        idx = np.random.choice(np.arange(len(pop)), size=len(pop)//2, replace=True, p=F)  # Sample with replacement, making genes with higher fitness more abundant in the population, while also ensuring weaker genes have a survival rate
    elif method == 'tournament':
        idx = np.zeros(len(pop)//2, dtype=np.int)
        for i in range(len(pop)//2):
            contenders = np.random.choice(np.arange(len(pop)), size=3)  # Choose 3 random individuals
            idx[i] = contenders[np.argmax(F[contenders])]  # The one with the highest fitness wins
    elif method == 'rank':
        idx = np.argsort(F)[-len(pop)//2:]  # Choose the top individuals
    return pop[idx]


def evolutionary_algorithm(DNA_SIZE = 2, BOUND=[-10,10], POP_SIZE=2000, N_GENERATIONS=200, EA_METHOD="EP", MUTATION_SIGMA=0.05, MUTATION_P=0.1, func = peaks):


    # Initialize population
    pop = np.random.uniform(*BOUND, size=(POP_SIZE, DNA_SIZE))

    # Record best fitness value for each generation
    best_fitness_values = []

    # Start timer
    start_time = time.time()

    method='tournament' # Change this to 'tournament' or 'rank' or 'roulette' as needed

    # Start evolution
    best_individual = None
    for generation in range(N_GENERATIONS):
        # First perform mutation operation
        new_pop = np.copy(pop)
        for i in range(len(new_pop)):
            if np.random.rand() < MUTATION_P:  # Only mutate if the random number is less than the mutation probability
                if EA_METHOD == "EP":
                    k = np.random.normal(size=DNA_SIZE)
                elif EA_METHOD == "FEP":
                    k = np.random.standard_cauchy(size=DNA_SIZE)
                new_pop[i] += MUTATION_SIGMA * k  # Directly modify elements in new_pop
                new_pop[i] = np.clip(new_pop[i], BOUND[0], BOUND[1])  # If genotype x, y out of bounds, change them to BOUND value
        
        pop = np.vstack((pop, new_pop))
    
        # Calculate population fitness value
        F = get_fitness(func(pop[:, 0], pop[:, 1]))

        # Record current best fitness value
        best_fitness = np.max(F)
        best_fitness_values.append(best_fitness)
    
        # Find the index of the current best individual
        best_individual_index = np.argmax(F)
        if best_individual is None or best_fitness > get_fitness(func(best_individual[0], best_individual[1])):
            best_individual = pop[best_individual_index]

        # If the current generation is a multiple of 10, print the fitness and genotype of the best individual
        if generation % (N_GENERATIONS//20) == 0:
            print("Generation {}: Best fitness = {:.5f}, x = {:.5f}, y = {:.5f}, z = {:.5f}".format(
                generation, best_fitness, best_individual[0], best_individual[1], -best_fitness))

        # Perform selection
        pop = select(pop, F, method=method)  # Change this to 'tournament' or 'rank' as needed

    # End timer
    end_time = time.time()

    # Print results
    print("{} algorithm (with {} selection) took {:.2f} seconds.".format(EA_METHOD, method, end_time - start_time))
    print("Best fitness: ", np.max(best_fitness_values))
    print("Best individual: x = {:.5f}, y = {:.5f}, z = {:.5f}".format(best_individual[0], best_individual[1], -np.max(best_fitness_values)))

    # Plot convergence curve
    plt.plot(best_fitness_values)
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title(f'POP_SIZE:{POP_SIZE},{EA_METHOD} with {method} Selection for {func.__name__} function')
    plt.show()


DNA_SIZE = 2             # DNA length
BOUND = [-10, 10]      # Upper and lower bounds for x and y
POP_SIZE = 40           # Population size
N_GENERATIONS = 600    # Number of generations

MUTATION_SIGMA = 0.1     # Standard deviation for mutation
MUTATION_P = 0.1            # Probability of mutation
EA_METHOD="EP"             # Evolutionary algorithm choice: "EP" or "FEP"

func = peaks # rastrigin or peaks

"""
Name of the 23 function to plot (e.g., ackley, bukin,
cross_in_tray, drop_wave, easom, eggholder, first_penalized,
goldstein_price, holder_table, langermann, levy, levy13,
michalewicz, peaks, quartic, rastrigin, schaffer2, schaffer4,
second_penalized, shekels_foxholes, six_hump_camel,
styblinski_tang, three_hump_camel).
"""


evolutionary_algorithm(DNA_SIZE, BOUND, POP_SIZE, N_GENERATIONS, EA_METHOD, MUTATION_SIGMA, MUTATION_P, func)

