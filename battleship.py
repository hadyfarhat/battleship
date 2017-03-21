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
    while len(p2.board.ships) > 0:
        print_board(get_ships_locations(p2.ships))
        print("Its {} turn".format(p1.name))
        player_1_attack = get_attack_location(p1)
        attack(p2, player_1_attack, p1)
        print_board(get_ships_locations(p1.ships))
        print("Its {} turn".format(p2.name))
        player_2_attack = get_attack_location(p2)
        attack(p1, player_2_attack, p2)
        print_board(get_ships_locations(p2.ships))

# attack boards
def get_attack_location(player):
    while True:
        attack_location = input("Where do you want to attack {}?".format(p1.name))
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


def attack(player_attacked, attack_location, player_attacking):
    print("{} is attacking {}".format(player_attacking.name, player_attacked.name))
    hit = False
    for ship in player_attacked.ships:
        for i in range(0, len(player_attacked.ships[ship])):
            if (player_attacked.ships[ship][i][0] == attack_location[0] and 
                player_attacked.ships[ship][i][1] == int(attack_location[1])):
                player_attacked.ships[ship][i] += HIT,
                hit = True
    if not hit:
        player_attacking.misses.append(attack_location)



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
            elif (x, row, 'h', HIT) in ships_locations or (x, row, 'v', HIT) in ships_locations:
                print(HIT, end=' ')
            else:
                print(EMPTY, end=' ')
        print("\n")


if __name__ == "__main__":
    p1 = Player()
    clear_screen()
    p2 = Player()
    clear_screen()
    play()







