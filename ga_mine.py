import numpy
import random

def fitness_values(equation_inputs):
  fitness = {}
  for i in equation_inputs:
    number_1 = 0
    for x in i:
      if(x == '1'):
        number_1 = number_1 + 1
    fitness[i] = number_1   
  return fitness   


def crossover(remaining_childs):
  print(f'remaining childs are -> ',remaining_childs)
  first_parts = []
  second_parts = []
  first_list = [i for i in remaining_childs[0]]
  second_list = [i for i in remaining_childs[1]]

  first_1 = ''.join(first_list[0:5])
  first_2 = ''.join(first_list[5:])
  second_1 = ''.join(second_list[0:5])
  second_2 = ''.join(second_list[5:])

  final1 = first_1 + second_2
  final2 = second_1 + first_2

  return [final1,final2]


def mutation(after_crossover):
   #select the first offspring
   first_offspring = after_crossover[0]
   in_list = [i for i in first_offspring]
   random_index = random.randint(0,9)

   if(in_list[random_index] == '0'):
     in_list[random_index] = '1'
   else:
     in_list[random_index] = '0'
   mutated_offspring = ''.join(in_list)  

   after_crossover[0] = mutated_offspring
   return after_crossover    



"""population is of 6 => select best 4 one point cross over of last two followed by 
one point mutation of first off spring"""

# Inputs of the equation.
equation_inputs = ['1111010101','0111000101','1110110101', '0100010011', '1110111101','0100110000']


num_generations = 80
for generation in range(num_generations):
    print(f'Generation Number = ', generation)

    print(f'The current best is', equation_inputs)


    fitness_dict = fitness_values(equation_inputs)
    values_sorted =  sorted(fitness_dict.items(), key=lambda x: x[1], reverse=True)
    #select best 4 from values sorted

    best_childs = []
    remaining_childs = []
    count = 4
    for key in values_sorted:
        if(count == 0):
            remaining_childs.append(key[0])
            
        else:
            best_childs.append(key[0])
            count -= 1
    #got best 4 childs and remaining childs for crossover and mutation

    after_crossover = crossover(remaining_childs)
    after_mutation = mutation(after_crossover)
    #now we got other two childs combine them to get the next iteration

    for i in after_mutation:
        best_childs.append(i)


    equation_inputs = best_childs















