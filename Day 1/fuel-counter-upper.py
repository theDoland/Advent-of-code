import math

module_mass_input_file = open("module-mass-input.txt", "r")

sum = 0
for module_mass in module_mass_input_file:
    sum += math.floor(int(module_mass) / 3) - 2

print(sum)