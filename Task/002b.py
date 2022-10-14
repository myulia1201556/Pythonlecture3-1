# Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 
# конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у 
# своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import shuffle, randint

candies = 150
candies_limit = 28


def bot_run(candies: int) -> int:
    result = candies % 29
    if not result:
        result = randint(1, 28)
    return result


def games(player_run):
    first, second = players
    return second if player_run == first else first


players = ["human", "bot" if int(input("Play with bot 1 - yes, 0 - no? "))  else "person"]
shuffle(players)

active_player = players[0]
print(f"1 игрок - {players[0]}, 2 игрок - {players[1]}")

while candies > 0:
    print(f"\n На столе {candies} конфет, вы можете взять  [1 .. {candies_limit}]")
    print(f"Игрок {active_player}  делает ход")

    if active_player == "bot":
        get_candies = bot_run(candies)
        print(f"Bot взял {get_candies} конфет")
    else:
        get_candies = int(input(f"Сколько конфет вы хотите взять {active_player}: "))

    if get_candies not in range(1, candies_limit + 1):
        print("Error!")
    else:
        candies -= get_candies
        if candies > 0:
            active_player = games(active_player)
        else:
            print(f"Игрок {active_player} выиграл, поздравляем!")
  
