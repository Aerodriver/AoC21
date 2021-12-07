# only move horizontal
# find minimal position change:

def crab_pos(input_path):
    crab_list = []
    with open(input_path, "r") as file:
        for x in file.readline().split(","):
            crab_list.append(int(x))
    # build a lsg and minnimize?
    fuel_best = len(crab_list)*len(crab_list)
    for i in range(len(crab_list)):
        fuel_temp = 0
        for c in crab_list:
            crab_distance = abs(c-i)
            fuel_temp = (fuel_temp + crab_distance)
        if fuel_temp < fuel_best:
            fuel_best = fuel_temp

    return fuel_best


def crab_pos2(input_path):
    crab_list = []
    with open(input_path, "r") as file:
        for x in file.readline().split(","):
            crab_list.append(int(x))
    # build a lsg and minnimize?
    fuel_best = None
    for i in range(len(crab_list)):
        fuel_temp = 0
        for c in crab_list:
            crab_distance = abs(c-i)
            nedded_fuel = ((abs(c-i))**2 + abs(c-i))/2
            fuel_temp = (fuel_temp + nedded_fuel)
        if not fuel_best or fuel_temp < fuel_best:
            fuel_best = fuel_temp

    return fuel_best

print(crab_pos("input.txt"))
print(crab_pos2("input.txt"))