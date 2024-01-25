import configparser
from game_logic import calculate_winnings, generate_winning_slot

config = configparser.ConfigParser()
config.read('settings.ini')
starting_money = int(config['DEFAULT']['MY_MONEY'])





def play_game():
    money = starting_money
    while True:
        print(f"У вас есть {money}$")
        if money <= 0:
            print("У вас недостаточно средств для продолжения игры")
            break
        slot = None
        while slot not in range(1, 31):
            try:
                slot = int(input("Выберите слот от 1 до 30: "))
                if slot < 1 or slot > 30:
                    print("Выбранный слот должен быть строго от 1 до 30!!!")
            except ValueError:
                print("Выбранный слот должен быть строго от 1 до 30!!!")

        bet_amount = int(input("Сколько вы хотите поставить? "))


        winning_slot = generate_winning_slot()
        winnings = calculate_winnings(bet_amount, slot, winning_slot)

        if winnings > 0:
            print(f"Вы выиграли {winnings}$!")
        else:
            print("Вы проиграли...")

        money += winnings

        play_again = input("Хотите сыграть еще? (да/нет): ")
        if play_again.lower() != "да":
            break

    if money > starting_money:
        print(f"Поздравляем! Вы выиграли {money - starting_money}$.")
    elif money < starting_money:
        print(f"К сожалению, вы проиграли {starting_money - money}$.")
    else:
        print("Ничья!")


if __name__ == "__main__":
    play_game()
