# only move horizontal
# find minimal position change:

def crab_pos(input_path):
    # one can also use the median
    crab_list = []
    with open(input_path, "r") as file:
        for x in file.readline().split(","):
            crab_list.append(int(x))
    fuel_best = None
    #best_pos = 0
    for i in range(max(crab_list)):
        fuel_temp = 0
        for c in crab_list:
            crab_distance = abs(c-i)
            fuel_temp = (fuel_temp + crab_distance)
            if i > 1 and fuel_temp > fuel_best:
                continue
        if  not fuel_best or fuel_temp <  fuel_best:
            fuel_best = fuel_temp
            #best_pos = i
    #print(best_pos,fuel_best)
    return fuel_best


def crab_pos2(input_path):
     # one can also use the average/mean
    crab_list = []
    with open(input_path, "r") as file:
        for x in file.readline().split(","):
            crab_list.append(int(x))
    #best_pos = 0
    fuel_best = None
    for i in range(max(crab_list)):
        fuel_temp = 0
        for c in crab_list:
            crab_distance = abs(c-i)
            nedded_fuel = (crab_distance**2 + crab_distance)/2
            fuel_temp = (fuel_temp + nedded_fuel)
            if i > 1 and fuel_temp > fuel_best:
                continue
        if not fuel_best or fuel_temp < fuel_best:
            fuel_best = fuel_temp
            #best_pos = i
    #print(best_pos, fuel_best)
    return fuel_best


print(crab_pos("input.txt"))
print(crab_pos2("input.txt"))