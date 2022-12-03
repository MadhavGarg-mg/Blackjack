"""I will make a blackjack game today"""
import random

cards_13 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_52 = cards_13 * 4

print('Welcome to Blackjack!\n')

total_money = int(input('How much money are you willing to play with? \n'))
if total_money < 1:
    print('Are you trying to waste my time! Get out!')
    exit()

while True:
    bet_amount = int(input('How much would you like to bet?\n'))
    if bet_amount < 1:
        print('Are you trying to waste my time! Get out!')
        break
    while bet_amount > total_money:
        print("Don't be cheeky! You are broke and can't afford that. Try again.")
        bet_amount = int(input('How much would you like to bet?\n'))

    comp_cards = []
    player_cards = []

    comp_cards.append(random.choice(cards_52))
    player_cards.append(random.choice(cards_52))
    comp_cards.append(random.choice(cards_52))
    player_cards.append(random.choice(cards_52))

    comp_total = 0
    player_total = 0

    for i in player_cards:
        player_total += i
        if 11 in player_cards and player_total > 21:
            player_cards[-1] = 1
            player_total -= 10

    print(f'Your cards are {player_cards}')
    print(f"The computer's card is {[comp_cards[0]]}")
    print(f'Your total is {player_total}')

    if player_total != 21:

        while True:
            more_cards = input('Do you want another card?: Y or N \n').lower()

            if more_cards == 'y':
                player_cards.append(random.choice(cards_52))
                player_total += player_cards[-1]
                if player_cards[-1] == 11 and player_total > 21:
                    player_cards[-1] = 1
                    player_total -= 10
                if player_total > 21:
                    break
                print(f'Your total is {player_total}')
                print(f'Your cards are {player_cards}')
            else:
                break

        if player_total > 21:
            print(f'Your cards are {player_cards}')
            print(f'Your total is {player_total}')
            print(f'Sorry you bust and lost {bet_amount}')
            total_money -= bet_amount

        else:
            for i in comp_cards:
                comp_total += i
                if 11 in comp_cards and comp_total > 21:
                    comp_cards[-1] = 1
                    comp_total -= 10
            print(f"The computer's cards are {comp_cards}")

            while comp_total < 17:
                comp_cards.append(random.choice(cards_52))
                comp_total += comp_cards[-1]
                if comp_cards[-1] == 11 and comp_total > 21:
                    comp_cards[-1] = 1
                    comp_total -= 10
                print(f"The computer's cards are {comp_cards}")

            print(f'The computer total is {comp_total}')
            print(f'Your total is {player_total}')

            if comp_total > 21:
                print(f'Congratulations! You won and doubled your bet of {bet_amount}')
                total_money += bet_amount
            else:
                if comp_total > player_total:
                    total_money -= bet_amount
                    print(f'You lost {bet_amount}')
                elif player_total > comp_total:
                    print(f'Congratulations! You won and doubled your bet of {bet_amount}')
                    total_money += bet_amount
                elif player_total == comp_total:
                    print('It is a tie. You get your bet back.')
        print(f'Your total money now is {total_money}')

    else:
        for i in comp_cards:
            comp_total += i
            if 11 in comp_cards and comp_total > 21:
                comp_total -= 10
        if comp_total == 21:
            print('It is a tie. You get your bet back.')
        else:
            print('Congratulations! You won! You got a Blackjack!')
            total_money += (1.5 * bet_amount)

    if total_money == 0:
        print('You ran out of money! The ATM is right there.')
        get_money = input('Do you want to get more money?: Y or N').lower()
        if get_money != 'y':
            print('Thank you for playing black jack. Hope to see you soon.')
            break
        else:
            total_money = int(input('Welcome back! How much money do you have now? \n'))
            if total_money < 1:
                print('Are you trying to waste my time! Get out!')
                break
            total = total_money
    else:
        play_again = input('Play again? Y or N: \n')
        if play_again.lower() != 'y':
            print(f'Thank you for playing black jack. Your total amount is {total_money}.')
            break
