from random import *


class Chromossome():
    def __init__(self, chromossome_size, crossover_tax, mutation_chance):
        self.chromossome_size = chromossome_size
        self.crossover_tax = crossover_tax
        self.mutation_chance = mutation_chance
        self.relative_fitness = 0
        self.absolute_fitness = 0
        self.value = sample(xrange(1, self.chromossome_size + 1),  self.chromossome_size)
        self.value.append(self.value[0])
        
    def crossover(self, chromossome_2):
        sons = []
        cutpoint = int(random() * self.chromossome_size)
        son_1 = Chromossome(self.chromossome_size, self.crossover_tax, self.mutation_chance)
        son_1.value = self.value[0 : cutpoint] + chromossome_2.value[cutpoint : (len(self.value))] 
        sons.append(son_1)
        son_2 = Chromossome(self.chromossome_size, self.crossover_tax, self.mutation_chance)
        son_2.value = chromossome_2.value[0 : cutpoint] + self.value[cutpoint : (len(self.value))] 
        sons.append(son_2)
        return sons
    
    def mutation(self):
        for i in range(self.chromossome_size):
            mutated_value = int(random() * self.chromossome_size) + 1
            if random() < self.mutation_chance:
                self.value[i] = mutated_value

    def __str__(self):
        return "Value=>{0} : Absolute Fitness=>{1}; Relative Fitness=>{2}\n".format(self.value, self.absolute_fitness, self.relative_fitness)

if __name__ == "__main__":
    test = Chromossome(5, 0.5, 0.1)
    print test
##    for _ in range(1000):
##        print int(random()*5) + 1
    test.mutation()
    print test
    
