

def command_generator(input_path):
    for line in open(input_path, 'r'):
        values = line.split()
        yield {"name":str(values[0]).lower(), "value":int(values[1])}


def submarine_mover1(input_path):
    #this is really not ideal, I just wanted to play around with dictionaries and lambda
    commands = { 
    "forward": lambda h_d, value : (h_d[0]+value, h_d[1]), 
    "up": lambda h_d, value : (h_d[0], h_d[1]-value),
    "down": lambda h_d, value : (h_d[0], h_d[1]+value)
    }
    h_d= (0,0) # horizontal, depth
    command_gen = command_generator(input_path)
    for command in command_gen:
        h_d = commands[command["name"]](h_d, command["value"])
    return(h_d[0]*h_d[1] )


def submarine_mover2(input_path):
    commands = { 
    "forward": lambda h, d, a, value : (h+value, d+(a*value), a), 
    "up": lambda h, d, a, value : (h, d, a-value),
    "down": lambda h, d, a, value : (h, d, a + value )
    }
    h_d_a= (0,0,0) # horizontal, depth, aim
    command_gen = command_generator(input_path)
    for command in command_gen:
        h_d_a = commands[command["name"]](*h_d_a , command["value"])
    return(h_d_a[0]*h_d_a[1])


# print(submarine_mover2("input.txt"))