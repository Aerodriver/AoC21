def input_gen(input_path):
    with open(input_path, "r") as file:
        for line in file:
            vals = line.split("|")
            yield (vals[0].split(),vals[1].split())


def part1(input_path):
    lengths = [2,4,3,7]
    total_nums_found = 0
    # this is where i would put my list comprehension: if I had any!
    for segment in input_gen(input_path):
        for s in segment[1]:
            if len(s) in lengths:
                total_nums_found+=1
    return total_nums_found


def part2(input_path):
    # 1111
    #2    3
    #2    3
    # 4444
    #5    6
    #5    6
    # 7777
    def build_a_num(segments, ilist):
        # idea: look for overlapping segmentnames; get initial names from easily known segments
        lengths = [2,4,3,7]
        easy_len = {2:"1",4:"4",3:"7",7:"8"}
        vals = {len(s):set(s) for s in segments if len(s) in lengths}
        n1 = vals[2]
        n4 = vals[4]
        n7 = vals[3]
        n8 = vals[7]
        seg2_4 = n4.symmetric_difference(n1)
        seg5_7 = n8.symmetric_difference(n4.union(n7))
        num=""
        for entry in ilist:
            seg_on = set(entry)
            num_of_letters = len(entry)
            if num_of_letters in lengths:
                num = num + easy_len[num_of_letters]
            elif num_of_letters == 5:
                if len(seg_on & seg2_4) == 2:
                    num = num + "5"
                elif len(seg_on & n1) != 2:
                    num = num + "2"
                else:
                    num = num + "3"
            else : # num_of_letters has to be 6
                if len(seg5_7 & seg_on) == 1 :
                    num = num + "9"
                elif len( n1 & seg_on) == 2:
                    num = num + "0"
                else:
                    num = num + "6"
        return int(num)

    sum_of_nums = 0
    for segment in input_gen(input_path):
        sum_of_nums += build_a_num(segment[0], segment[1])
    return sum_of_nums


print(part1("input.txt"))
print(part2("input.txt"))