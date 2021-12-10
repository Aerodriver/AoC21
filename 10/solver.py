

def line_gen(input_path):
    with open(input_path, "r") as file:
        for line in file:
            yield line.strip()


def corrupted_syntax(input_path):
    points_dict = {")":3, "]":57, "}":1197 ,">":25137}
    closing_dict = {"(":")", "[":"]", "{":"}", "<":">"}
    point_sum = 0
    for line in line_gen(input_path):
        stack = []
        for c in line:
            if stack and closing_dict.get(stack[-1]) == c:
                stack.pop(-1)
            elif c in closing_dict.keys() :
                stack.append(c)
            else : # illegal char detected
                point_sum = point_sum + points_dict.get(c)
                break
    return point_sum


def incomplete_syntax(input_path):
    def calc_points_for_line(missing_chars):
        points = 0
        points_dict = {")":1, "]":2, "}":3 ,">":4}
        for c in missing_chars:
            points = points * 5 + points_dict.get(c)
        return points

    closing_dict = {"(":")", "[":"]", "{":"}", "<":">"}
    line_points = []
    for line in line_gen(input_path):
        stack = []
        for c in line:
            if stack and closing_dict.get(stack[-1]) == c:
                stack.pop(-1)
            elif c in closing_dict.keys() :
                stack.append(c)
            else : # illegal char detected
                stack = []
                break
        if stack :
            missing_chars = ""
            while stack : 
                missing_chars = missing_chars + closing_dict.get(stack.pop())
            line_points.append(calc_points_for_line(missing_chars))
    line_points.sort()
    return line_points[int(len(line_points)/2)]  # int is sufficient because we want the middle and with this we get the middle


print(corrupted_syntax("input.txt"))
print(incomplete_syntax("input.txt"))

# too low 207570617
# too high 2797840607