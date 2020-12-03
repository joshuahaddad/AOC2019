# Day 1 The Tyranny of the Rocket Equation
import math

def calculate_fuel(filepath="../assets/fuel.txt"):
    with open(filepath, 'r') as f:
        masses = f.readlines()

    sum_fuel_pt1 = 0
    sum_fuel_pt2 = 0

    for mass in masses:
        fuel = math.floor(float(mass) / 3) - 2
        sum_fuel_pt1 += fuel
        sum_fuel_pt2 += fuel

        while (math.floor(float(fuel) / 3) - 2) > 0:
            fuel = math.floor(float(fuel) / 3) - 2
            sum_fuel_pt2 += fuel

    return sum_fuel_pt1, sum_fuel_pt2


pt1, pt2 = calculate_fuel()

print(f'Part1: {pt1}\nPart2: {pt2}')
