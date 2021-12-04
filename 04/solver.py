def board_generator(input_path):
    #yields the bingo boards
    with open(input_path, 'r') as file:
        next(file)#skip drawn numbers
        next(file)#skip empty line
        board = []
        counter = 0
        for line in file:
            if counter == 5:
                yield board
                counter = 0
                board = []
                continue
            board.append([int(i) for i in line.split()])
            counter =  counter + 1


def drawn_numbers(input_path):
    file = open(input_path, 'r')
    return [int(i) for i in next(file).split(",")]

def enter_num(board, num):
        for row in range(5):
            for index in range(5):
                if board[row][index] == num:
                    board[row][index] = -1
                    return board
        return board


def check_board(board):
    for i in range(5):
        if sum(board[i]) == -5 or sum([row[i] for row in board]) == -5:
            return True
    return False


def squid_game(input_path):
                
    best_board = []
    drawnnumbers = drawn_numbers(input_path)
    best_needed_numbers = len(drawnnumbers)# upper bound
    number_when_won = 0
    for board in board_generator(input_path):
        needed_numbers = 0
        number_when_won_temp = 0
        for num in drawnnumbers:
            needed_numbers += 1
            board = enter_num(board, num)
            if(check_board(board)):
                number_when_won_temp = num
                #print(needed_numbers)
                break

        if needed_numbers < best_needed_numbers:
            best_needed_numbers = needed_numbers
            number_when_won = number_when_won_temp
            best_board = [x[:] for x in board]

    res = 0
    for row in best_board:
        for num in row:
            if num != -1 :
                res += num

    return res*number_when_won


def squid_game_last(input_path):
   
    worst_board = []
    drawnnumbers = drawn_numbers(input_path)
    worst_needed_numbers = 0 #lower bound
    number_when_won = 0
    for board in board_generator(input_path):
        needed_numbers = 0
        number_when_won_temp = 0
        for num in drawnnumbers:
            needed_numbers += 1
            board = enter_num(board, num)
            if(check_board(board)):
                number_when_won_temp = num
                #print(needed_numbers)
                break

        if needed_numbers > worst_needed_numbers:
            worst_needed_numbers = needed_numbers
            number_when_won = number_when_won_temp
            worst_board = [x[:] for x in board]

    res = 0
    for row in worst_board:
        for num in row:
            if num != -1 :
                res += num

    return res*number_when_won

print(squid_game("input.txt"))
print(squid_game_last("input.txt"))