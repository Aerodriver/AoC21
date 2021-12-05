
def generate_line1(input_path):
    for i in open(input_path, 'r'):
        coordinates = i.split("->")
        c1 = [int(x) for x in coordinates[0].split(",")]
        c2 = [int(x) for x in coordinates[1].split(",")]
        res = []
        if c1[0] == c2[0] :
            res = [(c1[0], y) for y in range(min(c1[1],c2[1]),max(c1[1],c2[1])+1) ]
        elif c1[1] == c2[1] :
            res = [(x, c1[1]) for x in range(min(c1[0],c2[0]),max(c1[0],c2[0])+1) ]
        yield set(res)

def generate_line2(input_path):
    for i in open(input_path, 'r'):
        coordinates = i.split("->")
        c1 = [int(x) for x in coordinates[0].split(",")]
        c2 = [int(x) for x in coordinates[1].split(",")]
        res = []
        if c1[0] == c2[0] :
            res = [(c1[0], y) for y in range(min(c1[1],c2[1]),max(c1[1],c2[1])+1) ]
        elif c1[1] == c2[1] :
            res = [(x, c1[1]) for x in range(min(c1[0],c2[0]),max(c1[0],c2[0])+1) ]
        # horizontal lines with 45 degrees
        elif abs(c1[0]-c2[0]) == abs(c1[1]-c2[1]):
            #get direction
            if c1[0] < c2[0]: # first point left of second point
                if c1[1] < c2[1]:# upright
                    for k in range(0, abs(c1[0]-c2[0])+1):
                        res.append((c1[0]+k,c1[1]+k))
                else: # downright
                    for k in range(0, abs(c1[0]-c2[0])+1):
                        res.append((c1[0]+k,c1[1]-k))
            else: # first point right of second point
                if c1[1] < c2[1]: # upleft
                    for k in range(0, abs(c1[0]-c2[0])+1):
                        res.append((c1[0]-k,c1[1]+k))
                else: # downleft
                    for k in range(0, abs(c1[0]-c2[0])+1):
                        res.append((c1[0]-k,c1[1]-k))
        yield set(res)


def overlap_count(gen):
    points_of_overlap = {}
    lines = [x for x in gen]
    for l1 in range(0,len(lines)):
        for l2 in range(l1+1, len(lines)) :
            #print(l1,l2,len(lines))
            for x in list(lines[l1] & lines[l2]): # way faster than using in list
                points_of_overlap[x] = points_of_overlap.get(x,0) + 1
    return len(points_of_overlap)


print(overlap_count(generate_line1("input.txt")))
print(overlap_count(generate_line2("input.txt")))