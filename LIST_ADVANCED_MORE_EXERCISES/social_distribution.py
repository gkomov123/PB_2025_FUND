population = [int(person) for person in input().split(", ")]
minimum_wealth = int(input())
distributed = True

for index, person_wage in enumerate(population):
    wealthiest = max(population)
    wealthiest_index = population.index(max(population))
    if person_wage < minimum_wealth:
        wage_difference = minimum_wealth - person_wage
        if wealthiest - wage_difference >= minimum_wealth:
            population[index] += wage_difference
            population[wealthiest_index] -= wage_difference
        else:
            print("No equal distribution possible")
            distributed = False
            break

if distributed:
    print(population)
