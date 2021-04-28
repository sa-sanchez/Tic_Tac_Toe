x_count = 0
o_count = 0
empty_count = 0
three_x = 0
three_o = 0
turn = 0

def check_rows(string):
    global three_x
    global three_o

    if string[0][0] + string[0][1] + string[0][2] == "XXX":
        three_x += 1
    elif string[0][0] + string[0][1] + string[0][2] == "OOO":
        three_o += 1

    if string[1][0] + string[1][1] + string[1][2] == "XXX":
        three_x += 1
    elif string[1][0] + string[1][1] + string[1][2] == "OOO":
        three_o += 1

    if string[2][0] + string[2][1] + string[2][2] == "XXX":
        three_x += 1
    elif string[2][0] + string[2][1] + string[2][2] == "OOO":
        three_o += 1 
    
def check_colums(string):
    global three_x
    global three_o

    if (string[0][0] + string[1][0] + string[2][0]) == "XXX":
        three_x += 1
    elif (string[0][0] + string[1][0] + string[2][0]) == "OOO":
        three_o += 1

    if (string[0][1] + string[1][1] + string[2][1]) == "XXX":
        three_x += 1
    elif (string[0][1] + string[1][1] + string[2][1]) == "OOO":
        three_o += 1

    if (string[0][2] + string[1][2] + string[2][2]) == "XXX":
        three_x += 1
    elif (string[0][2] + string[1][2] + string[2][2]) == "OOO":
        three_o += 1

def check_diagonal(string):
    global three_x
    global three_o

    if (string[0][0] + string[1][1] + string[2][2]) == "XXX":
        three_x += 1
    elif (string[0][0] + string[1][1] + string[2][2]) == "OOO":
        three_o += 1
    
    if (string[0][2] + string[1][1] + string[2][0]) == "XXX":
        three_x += 1
    elif (string[0][2] + string[1][1] + string[2][0]) == "OOO":
        three_o += 1


symbols = "         "
for symbol in symbols:
    if symbol == " ":
        empty_count += 1
symbols_1 = [x for x in symbols[0:3]]
symbols_2 = [x for x in symbols[3:6]]
symbols_3 = [x for x in symbols[6:9]]
field = [symbols_1, symbols_2, symbols_3]
print("---------")
print("|", field[0][0], field[0][1], field[0][2], "|")
print("|", field[1][0], field[1][1], field[1][2], "|")
print("|", field[2][0], field[2][1], field[2][2], "|")
print("---------")

while True:
    usr_input = input("Enter the coordinates: ").split()
    confirm = 0
    count = len(usr_input)
    for i in range(count):
        if usr_input[i].isnumeric() == True:
            confirm += 1
        else:
            print("You should enter numbers!")
            break
    if confirm == 2:
        usr_coordinates = [int(x) for x in usr_input]
        for i in range(count):
            if usr_coordinates[i] > 3:
                print("Coordinates should be from 1 to 3!")
                confirm -= 1
                break
    if confirm == 2:
        coordinates = [0 , 0]
        coordinates[0] = 3 - usr_coordinates[1]
        coordinates[1] = usr_coordinates[0] - 1
        if field[coordinates[0]][coordinates[1]] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            if turn == 0:
                field[coordinates[0]][coordinates[1]] = "X"
                turn += 1
                empty_count -= 1
            elif turn == 1:
                field[coordinates[0]][coordinates[1]] = "O"
                turn -= 1
                empty_count -= 1
            print("---------")
            print("|", field[0][0], field[0][1], field[0][2], "|")
            print("|", field[1][0], field[1][1], field[1][2], "|")
            print("|", field[2][0], field[2][1], field[2][2], "|")
            print("---------")

    check_rows(field)
    check_colums(field)
    check_diagonal(field)

    if three_o + three_x == 0 and empty_count == 0:
        print("Draw")
        break
    elif three_x == 1 and three_o == 0:
        print("X wins")
        break
    elif three_o == 1 and three_x == 0:
        print("O wins")
        break


            