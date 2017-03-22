import pdb
import sys

# imports
from player import Player

# constants
BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

letter_board = 'abcdefghij'


def play():
    while True:
        # player 1
        # pdb.set_trace()
        next_turn(p1, p2)
        if check_winner(p1, p2):
            clear_screen()
            display_progress_board(p1, p2)
            print("{} won".format(p1.name))
            break
        switch_players()
        # player 2
        next_turn(p2, p1)
        if check_winner(p2, p1):
            clear_screen()
            display_progress_board(p2, p1)
            print("{} won".format(p2.name))
            break
        switch_players()

def next_turn(player_attacking, player_attacked):
    clear_screen()
    check_sunk_ships(player_attacking, player_attacked)
    display_progress_board(player_attacking, player_attacked)
    print("Its {}'s turn".format(player_attacking.name))
    print("{} is attacking {}".format(player_attacking.name, player_attacked.name))
    player_attack = get_attack_location(player_attacking)
    attack(player_attacked, player_attack, player_attacking)
    check_sunk_ships(player_attacking, player_attacked)
    

def check_winner(player_attacking, player_attacked):
    if player_attacked.ships_sunk == 2:
        return True
    return False

# attack boards
def get_attack_location(player):
    while True:
        attack_location = input("Where do you want to attack {}?".format(player.name))
        if validate_attack(attack_location):
            return attack_location
            break
        print("please enter correct attack location (ex: d6")
    print("{} is attacking".format(player.name))

# validate attack
def validate_attack(attack_location):
    if len(attack_location) <= 3:
        attack_location_x = attack_location[:1]
        try:
            attack_location_y = int(attack_location[1:])
        except ValueError:
            return False
        if (attack_location_x in 'abcdefghij' and 
            attack_location_y in [1,2,3,4,5,6,7,8,9,10]):
           return True
    return False

# attack player
def attack(player_attacked, attack_location, player_attacking):
    hit = False
    # convert attack location into a tuple of proper values
    attack_location_2 = (attack_location[0], int(attack_location[1]))
    for ship in player_attacked.ships:
        for i in range(0, len(player_attacked.ships[ship])):
            # check if attack location and ship_location match
            if player_attacked.ships[ship][i][:2] == attack_location_2:
                player_attacking.hits.append(attack_location_2)
                hit = True
    if not hit:
        player_attacking.misses.append(attack_location_2)



################
# board related functions
################

def clear_screen():
    print("\033c", end="")


def print_board_heading():
    print("" + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))



def get_ships_locations(player_ships):
    ships_locations = []
    for ship in player_ships:
        for ship_location in player_ships[ship]:
            ships_locations.append(ship_location)
    return ships_locations


# display each player's board
def print_board(ships_locations):
    print("", end=' ')
    print_board_heading()
    for row in range(1, 11):
        print(row, end=' ')
        for x in letter_board:
            if (x, row, 'v') in ships_locations:
                print(VERTICAL_SHIP, end=' ')
            elif (x, row, 'h') in ships_locations:
                print(HORIZONTAL_SHIP, end=' ')
            else:
                print(EMPTY, end=' ')
        print("\n")

# display board with hits, misse, empty and sunk
def display_progress_board(player_attacking, player_attacked):
    print("{}'s Board Progress".format(player_attacking.name))
    print(20*"-")
    print("\n")
    print(" ", end=' ')
    print_board_heading()
    for row in range(1, 11):
        print(row, end=' ')
        for x in letter_board:
            # check if their any location of a sunk ship
            # if player_attacked.ships_sunk_locations:
                # for ship_sunk in player_attacked.ships_sunk:
            if (x,row) in player_attacked.ships_sunk_locations:
                print(SUNK, end=' ')
            else:
                if (x, row) in player_attacking.hits:
                    print(HIT, end=' ')
                elif (x, row) in player_attacking.misses:
                    print(MISS, end=' ')
                else:
                    print(EMPTY, end=' ')
        print("\n")

def switch_players():
    input("Switch laptops and press Enter/Return......")

# check if player being attacked has any sunk ships
def check_sunk_ships(player_attacking, player_attacked):
    for ship in player_attacked.ships:
        ship_sunk = True
        for ship_location in player_attacked.ships[ship]:
            # hits(c,5) ship_location(c,5) 
            if (ship_location[:2] not in player_attacking.hits or
                ship_location[:2] in player_attacked.ships_sunk_locations):
                ship_sunk = False
        if ship_sunk:
            player_attacked.ships_sunk += 1
            for ship_sunk_location in player_attacked.ships[ship]:
                player_attacked.ships_sunk_locations.append(ship_sunk_location[:2])

if __name__ == "__main__":
    p1 = Player()
    switch_players()
    clear_screen()
    p2 = Player()
    switch_players()
    clear_screen()
    play()
 






