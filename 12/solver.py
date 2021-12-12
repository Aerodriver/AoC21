
class CaveSystem:
    start = "start"
    end = "end"
    def __init__(self, connections = []):
        self.connections = set(connections) #tupels of connected caves

    def twobig(self):
        return len([c for c in connections if (c[0].isupper() and c[1].isupper())])

    def find_paths_1(self):
        paths = [[self.start]] # list of paths
        final_paths = []
        changes = True
        while changes :
            changes = False
            tmp_paths = []
            for path in paths :
                #print(path)
                for neighbour in [x[1] for x in self.connections if x[0] == path[-1]] :
                    if neighbour == self.end:
                        tmp_path = path.copy()
                        tmp_path.append(neighbour)
                        final_paths.append(tmp_path)
                    elif (neighbour.isupper()) or not (neighbour in path) :
                        tmp_path = path.copy()
                        tmp_path.append(neighbour)
                        tmp_paths.append(tmp_path)
                        changes = True
            paths = tmp_paths
        return final_paths

    def find_paths_2(self): #extremly naiv approach but it works
        paths = [[0, self.start]] # first element shows if a small cave has been visited more than once, 0 = no, 1 = yes
        final_paths = []
        changes = True
        while changes :
            changes = False
            tmp_paths = []
            for path in paths :
                for neighbour in [x[1] for x in self.connections if x[0] == path[-1]] :
                    if neighbour == self.end:
                        tmp_path = path.copy()
                        tmp_path.append(neighbour)
                        final_paths.append(tmp_path)
                    elif neighbour.isupper() or not neighbour in path:
                        tmp_path = path.copy()
                        tmp_path.append(neighbour)
                        tmp_paths.append(tmp_path)
                        changes = True
                    elif neighbour!= self.start and path[0] == 0:
                        tmp_path = path.copy()
                        tmp_path.append(neighbour)
                        tmp_path[0] = 1
                        tmp_paths.append(tmp_path)
                        changes = True
            paths = tmp_paths
        return final_paths


def cave_builder(input_file):
    connections = set([])
    with open(input_file, "r") as file:
        for line in file:
            a, b = line.strip().split("-")
            connections.add((a,b))
            connections.add((b,a))
    cs = CaveSystem(connections)
    return cs


def part1(input_file):
    cs = cave_builder(input_file)
    return len(cs.find_paths_1())


def part2(input_file):
    cs = cave_builder(input_file)
    return len(cs.find_paths_2())

        
print(part1("input.txt"))
print(part2("input.txt"))
