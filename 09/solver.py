
def height_map(input_path):
    res = []
    with open(input_path, "r") as file:
        for line in file:
            res.append(list(map(int, line.strip())))
    return res


def part1(input_path):
    # naive solution
    hmap = height_map(input_path)
    rbound = len(hmap[0])-1
    dbound = len(hmap)-1
    sum_of_rlevels = 0
    for i in range(len(hmap)):
        for j in range(len(hmap[i])):
            val = hmap[i][j]
            #the sea of if and ifs
            if i == 0:
                if j == 0:
                    if val < hmap[i+1][j] and val < hmap[i][j+1] :
                        sum_of_rlevels = sum_of_rlevels+ val+1
                elif j == rbound:
                    if val < hmap[i+1][j] and val < hmap[i][j-1] :
                        sum_of_rlevels = sum_of_rlevels+ val+1
                else :
                    if val < hmap[i+1][j] and val < hmap[i][j+1] and val < hmap[i][j-1] :
                        sum_of_rlevels = sum_of_rlevels+ val+1
            elif i == dbound:
                if j == 0:
                    if (val < hmap[i-1][j]) and (val < hmap[i][j+1]) :
                        sum_of_rlevels = sum_of_rlevels + val+1
                elif j == rbound:
                    if (val < hmap[i-1][j]) and (val < hmap[i][j-1]) :
                        sum_of_rlevels = sum_of_rlevels + val+1
                else :
                    if (val < hmap[i-1][j]) and (val < hmap[i][j-1]) and (val < hmap[i][j+1]) :
                        sum_of_rlevels = sum_of_rlevels + val+1
            elif j == 0:
                if (val < hmap[i-1][j]) and (val < hmap[i+1][j]) and (val < hmap[i][j+1]) : 
                        sum_of_rlevels = sum_of_rlevels + val+1
            elif j == rbound:
                if (val < hmap[i-1][j]) and (val < hmap[i+1][j]) and (val < hmap[i][j-1]) :
                        sum_of_rlevels = sum_of_rlevels + val+1
            else:
                if (val < hmap[i-1][j]) and (val < hmap[i][j-1]) and (val < hmap[i+1][j]) and (val < hmap[i][j+1]) :
                    sum_of_rlevels = sum_of_rlevels + val+1
    return sum_of_rlevels


class Basin():
    def __init__(self, positions):
        self.positions = positions
        self.size = len(self.positions)


def build_a_basin(pos, field, rbound ,dbound):
    changes = True
    positions = set([])
    new_pos = [pos]
    while changes:
        tmp_pos = []
        changes = False
        for x, y in new_pos:
            for i in [1,-1] :
                if x+i < 0 or x+i > dbound:
                    continue 
                if field[x+i][y] != 9 and not (x+i,y) in positions:
                    tmp_pos.append((x+i,y))
                    positions.add((x+i,y))
            for i in [1,-1] :
                if y+i < 0 or y+i > rbound:
                    continue 
                if field[x][y+i] != 9 and not (x,y+i) in positions: 
                    tmp_pos.append((x,y+i))
                    positions.add((x,y+i))
        if len(tmp_pos) != 0 :
            changes = True
        new_pos = tmp_pos
    return Basin(positions)


def basin_finder(input_path):
    hmap = height_map(input_path)
    basins = []
    basin_posses = set([])
    rbound = len(hmap[0])-1
    dbound = len(hmap)-1
    for i in range(len(hmap)):
        for j in range(len(hmap[i])):
            if hmap[i][j] != 9 and not (i,j) in basin_posses:
                basin = build_a_basin((i,j), hmap, rbound, dbound)
                for p in basin.positions:
                    basin_posses.add(p)
                basins.append(basin)
    basins.sort(key = lambda x: x.size)
    return basins[-1].size * basins[-2].size * basins[-3].size