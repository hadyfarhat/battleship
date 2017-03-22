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
        clear_screen()
        check_sunk_ships(p1, p2)
        display_progress_board(p1, p2)
        print("Its {} turn".format(p1.name))
        player_1_attack = get_attack_location(p1)
        attack(p2, player_1_attack, p1)
        switch_players()
        clear_screen()
        check_sunk_ships(p2, p1)
        display_progress_board(p2, p1)
        print("Its {} turn".format(p2.name))
        player_2_attack = get_attack_location(p2)
        attack(p1, player_2_attack, p2)
        switch_players()

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

# attack player
def attack(player_attacked, attack_location, player_attacking):
    print("{} is attacking {}".format(player_attacking.name, player_attacked.name))
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
    print("Board Progress")
    print(20*"-")
    print("\n")
    print(" ", end=' ')
    print_board_heading()
    for row in range(1, 11):
        print(row, end=' ')
        for x in letter_board:
            # check if their any location of a sunk ship
            if player_attacked.ships_sunk_locations:
                # for ship_sunk in player_attacked.ships_sunk:
                if (x,row) in player_attacked.ships_sunk_locations:
                    print(SUNK, end=' ')
                else:
                    print(EMPTY, end=' ')
            elif (x, row) in player_attacking.hits:
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
            if ship_location[:2] not in player_attacking.hits:
                ship_sunk = False
        if ship_sunk:
            for ship_sunk_location in player_attacked.ships[ship]:
                player_attacked.ships_sunk_locations.append(ship_sunk_location[:2])

if __name__ == "__main__":
    p1 = Player()
    clear_screen()
    p2 = Player()
    clear_screen()
    play()
 






