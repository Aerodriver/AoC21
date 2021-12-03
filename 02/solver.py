

def command_generator(input_path):
    for line in open(input_path, 'r'):
        values = line.split()
        yield {"name":str(values[0])[0], "value":int(values[1])}


def submarine_mover1(input_path):
    #this is really not ideal, I just wanted to play around with dictionaries and lambda
    commands = { 
    "f": lambda h_d, value : (h_d[0]+value, h_d[1]), 
    "u": lambda h_d, value : (h_d[0], h_d[1]-value),
    "d": lambda h_d, value : (h_d[0], h_d[1]+value)
    }
    h_d = (0,0) # horizontal, depth
    command_gen = command_generator(input_path)
    for command in command_gen:
        h_d = commands[command["name"]](h_d, command["value"])
    return(h_d[0]*h_d[1] )


def submarine_mover2(input_path):
    h_d_a = [(0,0,0)]
    mult = lambda x: x[0]*x[1]
    funcs = { 
            "f": lambda value : 
                1 if (h_d_a.append((h_d_a[-1][0]+value, h_d_a[-1][1]+(h_d_a[-1][2]*value), h_d_a[-1][2])) or h_d_a.pop(0)) else 0, 
            "u": lambda value: 
                1 if (h_d_a.append((h_d_a[-1][0], h_d_a[-1][1], h_d_a[-1][2]-value)) or h_d_a.pop(0)) else 0,
            "d": lambda value : funcs["u"](value*-1),
            }
    if not 0 in (funcs[c["n"]](c["v"]) for c in ({"n":str(ls[0])[0], "v":int(ls[1])} for s in open(input_path, 'r') for ls in [s.split()])) :
        return (mult(h_d_a.pop()))


print(submarine_mover2("input.txt"))
