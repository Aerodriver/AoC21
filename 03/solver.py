def command_generator(input_path):
    for line in open(input_path, 'r'):
        yield line.strip()


def find_most_common(input_path):
    counters = [0,0,0,0,0,0,0,0,0,0,0,0]
    number_of_lines = 0

    for line in command_generator(input_path):# count how often a 1 ocures in each position
        i = 0
        number_of_lines += 1
        for s in line:
            counters[i] += int(s)
            i += 1
            
    gamma = 0b0
    for c in counters:
        gamma = gamma << 1
        if c >= number_of_lines/2: # if number of 1s on the position is more than half the amount input numbers we add a 1 at that position
            gamma = gamma+1
    epsilon = gamma  ^ 0b111111111111 # flip all bits/ apaprently ~ is not the way to go
    return int(epsilon)*int(gamma)


def life_reading(input_path):
    def most_common_at_i(ilist, pos):
        counter = 0
        totlen = len(ilist)
        for line in ilist:# count how often a 1 ocures at pos
            counter += int(line[pos])
        if counter >= totlen/2:
            return "1"
        else :
            return "0"

    def least_common_at_i(ilist, pos):
        counter = 0
        totlen = len(ilist)
        for line in ilist:# count how often a 1 ocures at pos
            counter += int(line[pos])
        if counter >= totlen/2:
            return "0"
        else :
            return "1"

    def decimate(ilist, prefix):
        return [line for line in ilist if line[:len(prefix)]==prefix]

    input_list = [line for line in command_generator(input_path)]
    prefix = ""
    prefix_pos = 0
    while len(input_list)!=1:
        prefix = prefix + most_common_at_i(input_list, prefix_pos) # build up prefix
        input_list = decimate(input_list, prefix) # delete all non compliant words from the list
        prefix_pos += 1 # advance to next position for the prefix

    oxygen = int(input_list[0],2)

    input_list = [line for line in command_generator(input_path)]
    prefix = ""
    prefix_pos = 0
    while len(input_list)!=1:
        prefix = prefix + least_common_at_i(input_list, prefix_pos)
        input_list = decimate(input_list, prefix)
        prefix_pos += 1

    co2 = int(input_list[0],2)
    
    return oxygen*co2


# print(find_most_common("input.txt"))
# print(life_reading("input.txt"))
