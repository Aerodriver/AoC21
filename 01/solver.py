# input.txt contains the puzzle numbers

def sonar_number_of_increase(inputpath: str) -> int:
    """
    :param inputpath: path to the file containing one reading per line
    :returns: the number of increases between readings
    """
    readings = []

    #read numbers and store them in order
    with open(inputpath, 'r') as file1:
        lines = file1.readlines()
        for line in lines:
            readings.append(int(line.strip()))

    # calculate the number of increases by comparing each reading to the previous one
    n_of_increases = 0
    previous_reading = readings[0]
    for reading in readings[1:]:
        if reading>previous_reading:
            n_of_increases +=1
        previous_reading = reading

    return n_of_increases


def sonar_number_of_increase_sliding(inputpath: str) -> int:
    """
    like sonar_number_of_increase but considers a three-measurement sliding window
    :param inputpath: path to the file containing one reading per line
    :returns: the number of increases between window sums
    """
    readings = []
    
    #read numbers and store them in order
    with open(inputpath, 'r') as file1:
        lines = file1.readlines()
        for line in lines:
            readings.append(int(line.strip()))

    # calculate sliding window sums by creating a tupel for each window and summing those tupels
    # for this just zip the elements with an offset 
    # keep in mind that the resulting list has window lenght -1 entries less than the original one
    window_sums = list(map(
        lambda x: x[0]+x[1]+x[2],
        zip(readings[0:-2],readings[1:-1],readings[2:])
        ))

    # calculate the number of increases by comparing each window sum to the previous one
    n_of_increases = 0
    previous_sum = window_sums[0]
    for window in window_sums[1:]:
        if window>previous_sum:
            n_of_increases +=1
        previous_sum = window

    return n_of_increases