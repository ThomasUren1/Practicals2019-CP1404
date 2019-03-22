########################################################################################################################
#                           Extension part 3 - Gopher Simulation
########################################################################################################################

from random import uniform

GOPHER_POPULATION = 1000
STARTING_YEAR = 1
MAX_YEARS = 10
MIN_BORN = 0.1
MAX_BORN = 0.2
MIN_DEAD = 0.08
MAX_DEAD = 0.25


def gopher_born(population):
    positive_gophers = int(population * uniform(MIN_BORN, MAX_BORN))
    return positive_gophers


def gopher_dead(population):
    negative_gophers = int(population * uniform(MIN_DEAD, MAX_DEAD))
    return negative_gophers


def main():
    print("Welcome to the Gophers Simulator 2019!")
    print("Starting Population: {}".format(GOPHER_POPULATION))
    print("Year {}".format(STARTING_YEAR))
    print()

    population = GOPHER_POPULATION

    for year in range(MAX_YEARS-1):
        new_gophers = gopher_born(population)
        dead_gophers = gopher_dead(population)
        population += new_gophers
        population -= dead_gophers
        print("{} gophers were born. {} died.".format(new_gophers, dead_gophers))
        print("Current Population is: {}".format(population))
        print("Year: {}".format(year+2))
        print()


main()
