from Chromossome import *


class GA():
    def __init__(self, num_gen=100, pop_size=50, cross_tax=0.5, mut_chance=0.1, chrom_size=5, tourn_size=3, selection=1):
        self.num_generation = num_gen
        self.pop_size = pop_size
        self.crossover_tax = cross_tax
        self.mutation_chance = mut_chance
        self.chromossome_size = chrom_size
        self.tournament_size = tourn_size
        self.cities = {}
        self.population = []
        self.selection = selection
        self.error = 0.1
        self.elitism_tax = 0.1

    def get_cities(self, filename):
        f = open(filename, "r")
        key = 1
        for line in f:
            self.cities[key] = map(int, line.split())
            key += 1
        f.close()    

    def init_pop(self):
        for i in range(self.pop_size):
            chromossome = Chromossome(self.chromossome_size, self.crossover_tax, self.mutation_chance)
            self.verify_valid_son(chromossome)
            self.population.append(chromossome)    

    def fitness(self, population):
        for chromossome in population:
            for i in range(self.chromossome_size):
                chromossome.absolute_fitness += self.cities[int(chromossome.value[i])][int(chromossome.value[i+1])-1]
            chromossome.relative_fitness = 1.0/chromossome.absolute_fitness

    def verify_valid_son(self, chromossome):
        generate_new_son = False
        for i in range(self.chromossome_size):
            if (self.cities[int(chromossome.value[i])][int(chromossome.value[i+1]) - 1] == -1):
                generate_new_son = True
        if(chromossome.value[0] != chromossome.value[-1]):
                generate_new_son = True
        for i in range(1, self.chromossome_size):
            for j in range(i + 1, self.chromossome_size):
                if chromossome.value[i] == chromossome.value[j]:
                    generate_new_son = True                    
        if generate_new_son:
            chromossome.value = sample(xrange(1, self.chromossome_size + 1),  self.chromossome_size)
            chromossome.value.append(chromossome.value[0])
            self.verify_valid_son(chromossome)
                    
    def tournament(self):
        fathers = []
        best_index = 0
        best_fitness = 0
        for i in range(self.tournament_size):
            fathers.append(self.population[int(random()*self.pop_size)])
            if fathers[i].relative_fitness > best_fitness:
                best_index = i
                best_fitness = fathers[i].relative_fitness
        return fathers[best_index]

    def sum_all_fitness():
        sum_fitness = 0
        for i in range(self.pop_size):
            sum_fitness += self.population[i].relative_fitness
        return sum_fitness
        
    def roulette(self):
        index = 0
        aux_sum = 0
        upper_boundary = random()*self.sum_all_fitness()
        for i in range(self.pop_size):
            while(aux < upper_boundary):
                aux += self.population[i].relative_fitness
            index = i - 1
        return self.population[index]

    def get_best(self, population):
        index_best = 0
        fitness_best = 0
        for i in range(len(population)):
            if population[i].relative_fitness > fitness_best:
                index_best = i
                fitness_best = self.population[i].relative_fitness
        return population[index_best]

    def elitism(self, population):
        elitist_vector = []
        elitism_size = int(self.elitism_tax*self.pop_size)
        aux_population = self.population
        for _ in range(elitism_size):
            elitist_vector.append(self.get_best(aux_population))
            aux_population.pop(self.get_best(aux_population))
        return elitist_vector

    def generation(self):
        new_population = []
        new_population.append(self.elitism(self.population))
        while(len(self.population) < self.pop_size):
            if self.selection == 0:
                father1 = self.roulette()
                father2 = self.roulette()
            else:
                father1 = self.tournament()
                father2 = self.tournament()
            sons = father1.crossover(father2)
            for son in sons:
                self.verify_valid_son(son)
                new_population.append(son)
        self.population = new_population

    def calc_media(self):
        media = 0.0
        for chromossome in self.population:
            media += chromossome.relative_fitness
        media = media/self.pop_size
        return media

    def verify_convergence(self):
        convergence = False
        best = self.get_best(self.population)
        if (best.relative_fitness - self.calc_media()) < self.error:
            convergence = True
        return convergence
    
    def run_process(self):
        self.get_cities("cidades.txt")
        self.init_pop()
        generation_index = 1
        while (self.verify_convergence()):
            print "Generation {0}".format(generation_index)
            self.fitness(self.population)
            self.generation()
        print self.get_best(self.population)
            
if __name__ == "__main__":
    test = GA(10, 100, 0.5, 0.1, 5, 3, 0)
    test.run_process()
