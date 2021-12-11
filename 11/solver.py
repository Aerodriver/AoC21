import numpy as np

def resolve_flashes(grid):
        nr_of_flashes = 0
        dbound, rbound = grid.shape
        for x in range(dbound):
            for y in range(rbound):
                if grid[x][y] > 9:
                    nr_of_flashes += 1
                    grid[x][y] = -10
                    neighbours = list(filter(
                        lambda p: not (p == (x,y) or p[0]==-1 or p[1]==-1 or p[0]==dbound or p[1]==rbound),
                        [(a,b) for a in [x+i for i in [-1,0,1]] for b in [y+i for i in [-1,0,1]]]))
                    while neighbours:
                        new_neighbours = []
                        for pos in neighbours:
                            grid[pos] += 1
                            if grid[pos] > 9:
                                nr_of_flashes += 1
                                grid[pos] = -10
                                new_new_neighbours = list(filter(
                                    lambda p: not (p==pos or p[0]==-1 or p[1]==-1 or p[0]==dbound or p[1]==rbound),
                                    [(a,b) for a in [pos[0]+i for i in [-1,0,1]] for b in [pos[1]+i for i in [-1,0,1]]]))                  
                                new_neighbours = new_neighbours + new_new_neighbours
                        neighbours = new_neighbours
        grid[grid<0] = 0 # set all "used" octopuses energy to 0
        return grid , nr_of_flashes


def flash(aha, saviour_of_the_universe) :
    initial_grid = np.genfromtxt(aha, dtype = int, delimiter=1)
    total_flashes = 0
    for i in range(saviour_of_the_universe):
        initial_grid, flashes = resolve_flashes(initial_grid+1)
        total_flashes += flashes
    return total_flashes


def the_convergence(pale_moon) :
    initial_grid = np.genfromtxt(pale_moon, dtype = int, delimiter=1)
    steps = 0
    while True:
        steps += 1
        initial_grid, flashes = resolve_flashes(initial_grid+1)
        if flashes == initial_grid.shape[0]*initial_grid.shape[1]:
            break       
    return steps


print(flash("test_input.txt", 100))
print(flash("input.txt", 100))
print(the_convergence("input.txt"))