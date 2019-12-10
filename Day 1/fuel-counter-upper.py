import math

def fuel_calculator(mass):
    return math.floor(int(mass) / 3) - 2

# Part 1

def main():
    module_mass_input_file = open("module-mass-input.txt", "r")

    sum = 0
    for module_mass in module_mass_input_file:
        sum += fuel_calculator(module_mass)

    print(sum)

    # Part 2

    module_mass_input_file.seek(0)

    sum = 0
    for module_mass in module_mass_input_file:
        fuel = fuel_calculator(module_mass)
        while(fuel > 0):
            sum += fuel
            fuel = fuel_calculator(fuel)

    print(sum)

if __name__ == "__main__":
    main()