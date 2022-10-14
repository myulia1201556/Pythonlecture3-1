# Создайте программу для игры в 'Крестики-нолики'.

print("Игра крестики - нолики!")

board = list(range(1,10))


def create_board():
    print("-"*20)
    for i in range(3):
        print("   ", board[0+i*3],"   ", board[1+i*3], "   ", board[2+i*3], "    ")
        print('-'*20)


def choice(number):
    global board
    while True:
        player_step = input("Ваш ход, выберите ячейку " + number + " --> ")
        if player_step.isdigit() and int(player_step) in range(1, 10):
            player_step = int(player_step)
            pos = board[player_step - 1]
            if pos not in (chr(10060), chr(11093)):
                board[player_step - 1] = chr(10060) if number == "X" else chr(11093)
                break
            else:
                print("Эта ячейка занята")
        else:
            print(f"Попробуйте снова{chr(9940)}")



def win_step():
    win_position = ((0,1,2),(3,4,5),(6,7,8),
                    (0,3,6),(1,4,7),(2,5,8),
                    (0,4,8),(2,4,6))
    n = [board[x[0]] for x in win_position if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n

    
def game():
    counter = 0
    create_board()
    while True:
        choice("O") if counter % 2 else choice("X")
        create_board()

        if counter > 3:
            if win_step():
                print(f"{win_step()} - Выиграл{chr(127942)}{chr(127881)}!")
                break
        if counter == 8:
            print(f"Ничья {chr(129318)}{chr(129309)}!")
            break
        counter += 1


game()
