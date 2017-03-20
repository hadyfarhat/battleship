import pdb

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
    while len(p1.board.ships) > 0:
        print("Its {} turn".format(p1.name))
        attack(p1)
        # print("Its {} turn".format(p2.name))
        # attack(player)

# attack boards
def attack(player):
    while True:
        attack_location = input("Where do you want to attack {}?".format(p1.name))
        if validate_attack(attack_location):
            print("Your attack is successful!")
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

################
# board related functions
################

def clear_screen():
    print("\033c", end="")


def print_board_heading():
    print("" + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))



def get_ships_locations(player_board_ship_gird):
    ships_locations = []
    for ship in player_board_ship_gird:
        for ship_location in ship:
            ships_locations.append(ship_location)
    return ships_locations


def print_board(ship_locations):
    print("", end=' ')
    print_board_heading()
    for row in range(1, 11):
        print(row, end=' ')
        for x in letter_board:
            if (x, row, 'v') in ship_locations:
                print(VERTICAL_SHIP, end=' ')
            elif (x, row, 'h') in ship_locations:
                print(HORIZONTAL_SHIP, end=' ')
            else:
                print(EMPTY, end=' ')
        print("\n")


if __name__ == "__main__":
    p1 = Player()
    play()







