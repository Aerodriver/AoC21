

def initial_fish_parser(input_path):
    res={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    with open(input_path, "r") as file:
        for x in file.readline().split(","):
            res[int(x)] = res.get(int(x),0) + 1
    return res


def anglerfishes(input_path, days):
    ftp = initial_fish_parser(input_path)
    for i in range(days):
        temp1 = ftp.get(0, 0)
        ftp[0] = ftp.get(1, 0)
        ftp[1] = ftp.get(2, 0)
        ftp[2] = ftp.get(3, 0)
        ftp[3] = ftp.get(4, 0)
        ftp[4] = ftp.get(5, 0)
        ftp[5] = ftp.get(6, 0)
        ftp[6] = ftp.get(7, 0) + temp1
        ftp[7] = ftp.get(8, 0)
        ftp[8] = temp1

    return sum(ftp.values())


print(anglerfishes("input.txt", 80))
print(anglerfishes("input.txt", 256))