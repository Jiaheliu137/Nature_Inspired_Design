import config as conf
import random

city_dist_mat = None
config = conf.get_config()

# Set up various parameters
gene_len = config.city_num  # The number of genes, equal to the number of cities
individual_num = config.individual_num  # The number of individuals in the population
gen_num = config.gen_num  # Number of generations, i.e. iterations
mutate_prob = config.mutate_prob  # Probability of gene mutation


def copy_list(old_arr):
    # Function to copy a list
    new_arr = []
    for element in old_arr:
        new_arr.append(element)
    return new_arr


# Individual class
class Individual:
    def __init__(self, genes=None):
        # Initialize a new individual with a random sequence if no genes are provided
        if genes is None:
            genes = [i for i in range(gene_len)]
            random.shuffle(genes)
        self.genes = genes
        self.fitness = self.evaluate_fitness()

    def evaluate_fitness(self):
        # Calculate the fitness of an individual
        fitness = 0.0
        for i in range(gene_len - 1):
            # Travel from one city to the next
            from_idx = self.genes[i]
            to_idx = self.genes[i + 1]
            fitness += city_dist_mat[from_idx, to_idx]
        # Return to the starting point
        fitness += city_dist_mat[self.genes[-1], self.genes[0]]
        return fitness


class EP:
    def __init__(self, input):
        global city_dist_mat
        city_dist_mat = input
        self.best = None  # The best individual of each generation
        self.individual_list = []  # List of all individuals in the population of each generation
        self.result_list = []  # The solution corresponding to each generation
        self.fitness_list = []  # The fitness corresponding to each generation

    def cross(self):
        # Crossover function
        new_gen = []
        random.shuffle(self.individual_list)
        for i in range(0, individual_num - 1, 2):
            # Parental genes
            genes1 = copy_list(self.individual_list[i].genes)  # Father's genotype
            genes2 = copy_list(self.individual_list[i + 1].genes)  # Mother's genotype
            index1 = random.randint(0, gene_len - 2)  # Defines the starting point of the gene sequence to be crossed
            index2 = random.randint(index1, gene_len - 1)  # Defines the end point of the gene sequence to be crossed
            genes1_recorder = {value: idx for idx, value in enumerate(
                genes1)}  # Records the position (idx) of each gene (value) in the father's DNA
            genes2_recorder = {value: idx for idx,
                               value in enumerate(genes2)}  # Records the position of each gene in the mother's DNA

            # Cross recombination
            for j in range(index1, index2):
                value1, value2 = genes1[j], genes2[j]  # The j-th gene in parents' DNA
                pos1, pos2 = genes1_recorder[value2], genes2_recorder[value1]  # Find the position of the mother's value2 gene in the father and the position of the father's value1 gene in the mother

                # Such crossover operation can ensure that there will be no duplicate cities on the path
                genes1[j], genes1[pos1] = genes1[pos1], genes1[j]
                genes2[j], genes2[pos2] = genes2[pos2], genes2[j]

                # Update the corresponding index of the parents' genes, but the dictionary is not needed later
                genes1_recorder[value2], genes1_recorder[value1] = j, pos1
                genes2_recorder[value1], genes2_recorder[value2] = j, pos2

            new_gen.append(Individual(genes1))
            new_gen.append(Individual(genes2))
        return new_gen

    def mutate(self, new_gen):
        # Mutation function
        for individual in new_gen:
            if random.random() < mutate_prob:

                old_genes = copy_list(individual.genes)
                index1 = random.randint(0, gene_len - 2)  # Start of mutation
                index2 = random.randint(index1, gene_len - 1)  # End of mutation
                genes_mutate = old_genes[index1:index2]  # The fragment of genes to be mutated (excluding index2)
                genes_mutate.reverse()  # Use reverse operation for mutation
                individual.genes = old_genes[:index1] + genes_mutate + old_genes[index2:]
                    

        # Combine parents and offspring
        self.individual_list += new_gen

    def select(self):
        # Selection function
        winners = []  # Tournament result
        n = 5
        for _ in range(individual_num):
            # Randomly select n individuals
            players = random.sample(self.individual_list, n)
            # Choose the individual with the highest fitness
            winner = min(players, key=lambda x: x.fitness)
            winners.append(winner)
        self.individual_list = winners

    def next_gen(self):
        # Create the next generation
        new_gen = self.cross()  # Cross
        self.mutate(new_gen)  # Mutate
        self.select()  # Select
        # Get the result of this generation
        for individual in self.individual_list:
            if individual.fitness < self.best.fitness:
                self.best = individual

    def train(self):
        # Initial generation population
        self.individual_list = [Individual() for _ in range(individual_num)]
        self.best = self.individual_list[0]
        # Iterate
        for i in range(gen_num):
            self.next_gen()
            # Connect the head and tail
            result = copy_list(self.best.genes)
            result.append(result[0])
            self.result_list.append(result)
            self.fitness_list.append(self.best.fitness)
        return self.result_list, self.fitness_list
