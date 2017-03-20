import pdb

# imports
from player import Player
from board import Board

def play():
    p = Player()



SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

letter_board = 'abcdefghij'

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










