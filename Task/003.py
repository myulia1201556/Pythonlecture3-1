# Создайте программу для игры в 'Крестики-нолики'.

print("Игра крестики - нолики!")

board = list(range(1,10))


def create_board(board):
    print("-"*12)
    for i in range(3):
        print("|", board[0+i*3],"|", board[1+i*3], "|", board[2+i*3], "|")
        print('-'*12)


def choice(number):
    valid = False
    while not valid:
        player_step = input("Ваш ход, выберите ячейку " + number + " --> ")
        try:
            player_step = int(player_step)
        except:
            print("Error")
            continue
        if player_step >= 1 and player_step <= 9:
            if(str(board[player_step - 1]) not in "XO"):
                board[player_step-1] = number
                valid = True
            else:
                print("Эта ячейка занята")
        else:
            print("Попробуйте снова")


def win_step(board):
    win_position = [(0,1,2),(3,4,5),(6,7,8),
                    (0,3,6),(1,4,7),(2,5,8),
                    (0,4,8),(2,4,6)]
    win = ""
    for i in win_position:
        if board[i[0]] == "X" and board[i[1]] =="X"and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"
    return win

    for i in win_position:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False



def game(board):
    counter = 0
    winner = False
    while not winner:
        create_board(board)
        if counter % 2 == 0:
            choice("X")
        else:
            choice("0")
        counter +=1
        if counter > 4:
            tmp = win_step(board)
            if tmp:
                print(tmp,"Победа")
                winner = True
                break
            if counter == 9:
                print("Ничья!)")
        create_board(board)
       

game(board)






