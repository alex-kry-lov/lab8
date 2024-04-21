import random

def computer_throw():
    if random.random() < 0.7:
        print("Компьютер бросает мяч: Бросок, вы поймали мяч.")
        answer = input("Вопрос: Ваше имя?\n")
        return answer
    else:
        print("Компьютер бросает мяч: Бросок, вы не поймали мяч.")
        return "Ржавое корыто"

def player_throw():
    if random.random() < 0.7:
        print("Вы бросаете мяч: Бросок, компьютер не поймал мяч.")
        answer = input("Вопрос: Где вы живете?\n")
        return answer
    else:
        print("Вы бросаете мяч: Бросок, компьютер поймал мяч.")
        return random.choice(["На Марсе", "На Луне", "В тумане"])

def play_game():
    history_player = []
    history_computer = []

    for _ in range(5):
        history_player.append(player_throw())
        history_computer.append(computer_throw())

    print("\nИстория для игрока:")
    for i, answer in enumerate(history_player):
        print(f"Ход {i+1}: {answer}")

    print("\nИстория для компьютера:")
    for i, answer in enumerate(history_computer):
        print(f"Ход {i+1}: {answer}")

play_game()