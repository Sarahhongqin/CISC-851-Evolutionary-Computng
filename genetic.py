import random
class geneticMaterial:
    # gene_num_bits here reresents the number of bits representing each hyperparameter value.
    # learning_rate_dict should have 10 bits i.e. maximum value 1023/2000 i.e. 0.511
    # num_hidden_dict should have 9 bits in a 32 bit gene, i.e. maximum value should be 511
    # epochs_dict should have 4 bits in a 32 bit gene, i.e. maximum value should be 15
    # timesteps_dict which means first l number of words of a movie review the LSTM sees before making a correct prediction. - 9 bits are assigned with max length 511
    gene_num_bits = [10,9,4,9]

    chromosome_length = sum(gene_num_bits)

    num_hyper_parameters = 4
    num_population = 20
    max_generations = 15

    mutation_probability = 0.3

    #  creating first generation of population by assigning random 0s and 1s to each bit
    def __init__(self):
        self.gene = [random.randint(0,1) for i in range(self.chromosome_length)]
        self.fitness = None
        self.phenoType = []
        self.convert_to_phenotype()
        
    # convert the genes to phenotypes i.e. generate an integer number for each hyperparameter
    def convert_to_phenotype(self):
        self.phenoType = []
        boundary = 0
        for each in self.gene_num_bits:
            self.phenoType.append(int(''.join(map(str,self.gene[boundary:boundary+each])),2))
            boundary += each
            
    # convert phenotypes to generate bit values for each parameter i.e. into genotype
    def convert_to_genotype(self):

        gene = []
        for i, hyper in enumerate(self.phenoType):
            binary_ = '{0:0' + str(self.gene_num_bits[i]) + 'b}'
            gene.extend(list(binary_.format(hyper)))
        gene = [int(each) for each in gene]
        self.gene = gene

    # one-point crossover used
    def crossover(self, model_1,model_2,crossover_point):
        self.gene = model_1.gene[:crossover_point] + model_2.gene[crossover_point:]
        self.convert_to_phenotype()
        
    # One- point mutation - for each hyperparameters's bit values, we pick a random position and flip the bit of that position
    # For each mutation, total four bits are flipped, one for each hyperparamter.
    def mutate(self):
        boundary = 0
        change_points = []
        for each in self.gene_num_bits:
            change_points.append(random.randint(boundary,boundary+each-1))
            boundary += each
        for change_point in change_points:
            self.gene[change_point] = 1 - self.gene[change_point]
        self.convert_to_phenotype()

    # A fitness value is assigned
    def set_fitness(self, fitness_value):
        self.fitness = fitness_value
