import time
from colorama import Fore, Style, init

init(autoreset=True)

def colored_print(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

def battle():
    colored_print("Вы вступаете в сражение с врагом!", Fore.RED)
    time.sleep(1)
    colored_print("1. Атаковать", Fore.YELLOW)
    colored_print("2. Увернуться", Fore.YELLOW)
    choice = input("Выберите действие: ")
    if choice == "1":
        colored_print("Вы атакуете врага и одолеваете его.", Fore.GREEN)
    elif choice == "2":
        colored_print("Вы увернулись от атаки врага и контратаковали.", Fore.GREEN)
        time.sleep(1)
        colored_print("Вы побеждаете врага.", Fore.GREEN)
    else:
        colored_print("Неверный выбор. Вы проигрываете.", Fore.RED)
        game_over()

def game_over():
    colored_print("Игра окончена. Хотите сыграть еще раз? (да/нет)", Fore.RED)
    choice = input().lower()
    if choice == "да":
        start_game()
    else:
        colored_print("Спасибо за игру! До свидания!", Fore.YELLOW)

def continue_game():
    print("Вы продолжаете свой путь и натыкаетесь на деревню.")
    time.sleep(1)
    print("Деревня находится в опасности из-за враждебного дракона.")
    time.sleep(1)
    print("Местные жители просят вас помочь.")
    time.sleep(1)
    print("1. Согласиться помочь")
    print("2. Отказаться и уйти")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы решаете помочь деревне в борьбе с драконом.")
        time.sleep(1)
        battle()
    elif choice == "2":
        print("Вы решаете не вмешиваться и уходите.")
        time.sleep(1)
        print("По пути вы находите сокровища.")
        game_over()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()

def mystical_cave():
    print("Вы приходите к загадочной пещере.")
    time.sleep(1)
    print("1. Войти в пещеру")
    print("2. Пройти мимо")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы входите в пещеру и находите древние артефакты.")
        time.sleep(1)
        print("Артефакты придают вам магические способности.")
        time.sleep(1)
        print("Теперь вы можете использовать магию в битве.")
        time.sleep(1)
        continue_game()
    elif choice == "2":
        print("Вы решаете не рисковать и идете дальше.")
        time.sleep(1)
        continue_game()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()

def forest():
    print("Вы идете глубже в лес и натыкаетесь на странного волшебника.")
    time.sleep(1)
    print("Волшебник предлагает вам помощь в обмен на выполнение задания.")
    time.sleep(1)
    print("1. Согласиться на задание")
    print("2. Отказаться и продолжить свой путь")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы соглашаетесь выполнить задание волшебника.")
        time.sleep(1)
        print("Волшебник дарует вам магический посох.")
        time.sleep(1)
        print("Теперь у вас есть магическая сила.")
        time.sleep(1)
        mystical_cave()
    elif choice == "2":
        print("Вы решаете не связываться с волшебником и идете дальше.")
        time.sleep(1)
        mystical_cave()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()

def ancient_temple():
    print("Вы обнаруживаете древний храм в лесу.")
    time.sleep(1)
    print("Храм полон загадок и опасностей.")
    time.sleep(1)
    print("1. Исследовать храм")
    print("2. Пойти в другую сторону")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы входите в храм и сталкиваетесь с первой загадкой.")
        time.sleep(1)
        print("Решив ее, вы продвигаетесь дальше, но опасности только увеличиваются.")
        time.sleep(1)
        print("В конце храма вас ждет великое испытание.")
        time.sleep(1)
        battle()
    elif choice == "2":
        print("Вы решаете не рисковать и идете дальше в поисках других приключений.")
        time.sleep(1)
        forest()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()

def underwater_cave():
    print("Вы обнаруживаете вход в подводную пещеру.")
    time.sleep(1)
    print("1. Войти в пещеру")
    print("2. Пройти мимо")
    choice = input("Выберите действие: ")
    if choice == "1":
        print("Вы входите в пещеру и обнаруживаете потопленный корабль.")
        time.sleep(1)
        print("Исследуя корабль, вы находите сокровища и сундук с картой сокровищ.")
        time.sleep(1)
        print("1. Открыть сундук")
        print("2. Следовать по карте")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы открываете сундук и находите драгоценности.")
            time.sleep(1)
            print("С сокровищами в кармане вы возвращаетесь на берег.")
            time.sleep(1)
            continue_game()
        elif choice == "2":
            print("Вы следуете по карте и приходите к другой части пещеры.")
            time.sleep(1)
            print("Там вас ждет новая загадка.")
            time.sleep(1)
            print("1. Решить загадку")
            print("2. Вернуться обратно")
            choice = input("Выберите действие: ")
            if choice == "1":
                print("Вы решаете загадку и продвигаетесь дальше.")
                time.sleep(1)
                print("Вас ждет еще одно испытание.")
                time.sleep(1)
                battle()
            elif choice == "2":
                print("Вы решаете вернуться обратно.")
                time.sleep(1)
                continue_game()
            else:
                print("Неверный выбор. Вы проигрываете.")
                game_over()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()
    elif choice == "2":
        print("Вы решаете не рисковать и идете дальше.")
        time.sleep(1)
        continue_game()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()

def start_game():
    print("Вы находитесь в темном лесу.")
    time.sleep(1)
    print("Вы можете пойти влево, вправо, прямо или назад.")
    choice = input().lower()
    if choice == "влево":
        print("Вы находите заброшенный замок.")
        time.sleep(1)
        print("1. Исследовать замок")
        print("2. Пройти мимо")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы находите магический артефакт внутри замка.")
            time.sleep(1)
            print("Артефакт придает вам силу.")
            time.sleep(1)
            ancient_temple()
        elif choice == "2":
            print("Вы решаете не рисковать и идете дальше.")
            time.sleep(1)
            ancient_temple()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()
    elif choice == "вправо":
        print("Вы натыкаетесь на стаю волков.")
        time.sleep(1)
        print("1. Попытаться уйти")
        print("2. Сразиться с волками")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы уходите, но вас настигает волк.")
            time.sleep(1)
            battle()
        elif choice == "2":
            print("Вы сражаетесь с волками.")
            time.sleep(1)
            battle()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()
    elif choice == "прямо":
        print("Вы видите загадочный свет впереди.")
        time.sleep(1)
        print("1. Подойти ближе")
        print("2. Обойти стороной")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("Вы подходите ближе и обнаруживаете магическую фонтанку.")
            time.sleep(1)
            print("Фонтанка возвращает вам здоровье и силы.")
            time.sleep(1)
            forest()
        elif choice == "2":
            print("Вы решаете обойти и идете дальше.")
            time.sleep(1)
            forest()
        else:
            print("Неверный выбор. Вы проигрываете.")
            game_over()
    elif choice == "назад":
        print("Вы решаете вернуться на своей пути.")
        time.sleep(1)
        underwater_cave()
    else:
        print("Неверный выбор. Вы проигрываете.")
        game_over()

if __name__ == "__main__":
    start_game()
