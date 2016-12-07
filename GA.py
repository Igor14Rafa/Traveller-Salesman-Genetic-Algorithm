from Chromossome import *

class GA():
    def __init__(self, num_generation = 100, pop_size = 50, crossover_tax = 0.5, mutation_chance = 0.1, chromossome_size = 5, tournament_size):
        self.num_generation = num_generation
        self.pop_size = pop_size
        self.crossover_tax = crossover_tax
        self.mutation_chance = mutation_chance
        self.chromossome_size = chromossome_size
        self.tournament_size = tournament_size
        self.cities = {}
        self.population = []

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
            self.population.append(chromossome)    

    def fitness(self):
        for chromossome in self.population:
            for i in range(self.chromossome_size - 1):
                chromossome.fitness+=self.cities[int(chromossome.value[i])][int(chromossome.value[i+1])]

    def tournament(self):
        fathers = []
        for _ in range(tournament_size):
            fathers.append(self.population[int(random()*self.pop_size)])

            
        
    def run_process(self):
        self.get_cities("cidades.txt")
        self.init_pop()
        self.fitness()
        for i in self.population:
        

if __name__ == "__main__":
    test = GA(10,10,0.5,0.1,4)
    test.run_process()
    
    
