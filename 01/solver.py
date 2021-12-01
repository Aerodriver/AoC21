## naive solutions ##

def count_number_of_increases(valuelist: [int]) -> int:
    # returns the number of times a value is higher than the previous one in the given list
    increases = 0
    for i in range(1, len(valuelist)) :
        if valuelist[i] > valuelist[i-1] :
            increases += 1
    return increases


def parse_input_list(input_path: str) -> [int]:
    values = []
    with open(input_path, 'r') as file1:
        for line in file1:
            values.append(int(line.strip()))
    return values


def sonar(input_path: str) -> int:
    readings = parse_input_list(input_path)
    increases = count_number_of_increases(readings)
    return increases


def sonar_sliding(input_path: str) -> int:
    readings = parse_input_list(input_path)
    window_sums = list( map( lambda x: sum(x), zip(readings[0:-2], readings[1:-1], readings[2:])))
    increases = count_number_of_increases(window_sums)
    return increases


## solutions using generators to be more memory friendly ##

def input_list_generator(input_path):
    for line in open(input_path, 'r'):
        yield int(line.strip())


def count_number_of_increases_from_generator(valuegen) -> int:
    # returns the number of times a value is higher than the previous one in the given generator
    # if the genrator does not stop, neither will this function
    increases = 0
    previous_value = next(valuegen)
    for value in valuegen :
        if value > previous_value :
            increases += 1
        previous_value = value
    return increases


def sonar2(input_path: str) -> int:
    gen = input_list_generator(input_path)
    increases = count_number_of_increases_from_generator(gen)
    return increases


def sonar_sliding2(input_path: str) -> int:
    def gen_window(valuegen):
        x = next(valuegen)
        y = next(valuegen)
        for z in valuegen:
            yield x + y + z
            x = y
            y = z

    gen = input_list_generator(input_path)
    # use the generator to create a new one that yields the sums of the sliding window
    window_gen = gen_window(gen)
    increases = count_number_of_increases_from_generator(window_gen)
    return increases


#print("solution 1: ", sonar2("input.txt"))
#print("solution 2: ", sonar_sliding2("input.txt"))