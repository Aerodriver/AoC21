
class CaveSystem:
    start = "start"
    end = "end"
    
    def __init__(self, connections = []):
        #self.connections = connections
        self.neighbours = {x[0]:[y[1] for y in connections if y[0]==x[0]] for x in connections} #build a dict to quickly look up neighbours


    def find_paths(self, repeat=False): # repeat allows one small cave to appear twice on a path
        paths = [[0, self.start]] # first element shows if a small cave has been visited more than once; 0 = no, 1 = yes
        final_paths_nr = 0
        while paths :
            tmp_paths = []
            for path in paths :
                for neighbour in self.neighbours[path[-1]] :
                    if neighbour == self.end:
                        final_paths_nr += 1
                    elif neighbour.isupper() or not neighbour in path:
                        tmp_paths.append(path+[neighbour])
                    elif repeat and path[0] == 0 and neighbour!= self.start:
                        tmp_paths.append([1]+path[1:]+[neighbour])
            paths = tmp_paths
        return final_paths_nr


def cave_builder(input_file):
    connections = set([])
    with open(input_file, "r") as file:
        for line in file:
            a, b = line.strip().split("-")
            connections.add((a,b)) # add both ways
            connections.add((b,a))
    cs = CaveSystem(connections)
    return cs


def part1(input_file):
    cs = cave_builder(input_file)
    return cs.find_paths()


def part2(input_file):
    cs = cave_builder(input_file)
    return cs.find_paths(True)


print(part1("input.txt"))
print(part2("input.txt"))
