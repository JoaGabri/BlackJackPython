import random
import time

user_cards = []
computer_cards = []
total_user = 0
total_computer = 0


def deal_cards(card_array):
    blackjack_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_array.append(random.choice(blackjack_cards))

def computer_wins():
     print("o computador venceu :/")
     for x in range(3):
        time.sleep(0.5)
        print(".")
     exit()

def user_wins():
    print("usuario vencedor!")
    for y in range(3):
        time.sleep(0.5)
        print(".")
    exit()

def check_ace(cards):
    count_11 = cards.count(11)
    if count_11 == 1:
        index = cards.index(11)
        cards[index] = 1
        print("o seu ace foi transformado em 1 automaticamente!")

    elif count_11 > 1:
        aces = count_11
        while True:
            try:
                num_aces_to_transform = int(input(f"Você possui {aces} aces. Quantos você deseja transformar? "))
                if 0 < num_aces_to_transform <= aces:
                    break
                else:
                    print(f"Por favor, digite um número entre 1 e {aces}.")
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

        # Transformar o número de aces especificado pelo usuário
        for i in range(num_aces_to_transform):
            index = cards.index(11)
            cards[index] = 1
    print(f"cartas do usuario: {user_cards}, cartas do computador: {computer_cards}")

    computer_wins() if sum(cards) > 21 else None

def game_compare():
    if total_computer == 21:
     computer_wins()
    elif total_user == 21:
     user_wins()

def blackjack():
    global total_user, total_computer

    total_user = sum(user_cards)
    total_computer = sum(computer_cards)

    print(f"cartas do usuario: {user_cards}, cartas do computador: {computer_cards}")


    game_compare()
    
    count_11 = user_cards.count(11)
    
    if total_user > 21:
        check_ace(user_cards) if count_11 > 0 else computer_wins()

for x in range(2):
    deal_cards(user_cards)
    deal_cards(computer_cards)

blackjack()

while True:
    choice = None
    while choice not in ['0', '1']:
        choice = input("Deseja outra carta? Digite 1 para sim e 0 para não: ")

    if choice == '1':
        deal_cards(user_cards)
        blackjack()

    elif choice == '0':
        while sum(computer_cards) <= 17:
            deal_cards(computer_cards)
            print(f"computador possui: {computer_cards}")

            print("o computador passou dos 17 digitos!")
            time.sleep(2)

        if sum(computer_cards) > 21:
            print(f"computador possui: {computer_cards}")
            print(f"o usuario possui: {user_cards}")
            user_wins()
        elif sum(computer_cards) == sum(user_cards):
            print(f"computador possui: {computer_cards}")
            print(f"o usuario possui: {user_cards}")
            print(f"empate!")
        elif sum(user_cards) > sum(computer_cards):
            print(f"computador possui: {computer_cards}")
            print(f"o usuario possui: {user_cards}")
            user_wins()
        else:
            print(f"computador possui: {computer_cards}")
            print(f"o usuario possui: {user_cards}")
            computer_wins()