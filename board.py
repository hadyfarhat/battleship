import pdb  

class Board:
    ships = [
        ("Aircraft Carrier", 5),
        # ("Battleship", 4),
        # ("Submarine", 3),
        # ("Cruiser", 3),
        # ("Patrol Boat", 2)
    ]

    def __init__(self):
        self.set_up()

    # clears the screen
    def clear_screen(self):
        print("\033c", end="")

    # location of all ships related to this object

    # main loop; runs board program
    def set_up(self):
        self.ship_grid = []
        for ship in range(len(self.ships)):
            while True:
                # check if ship_grid is empty
                # if it is: print the board(empty board)
                if not self.ship_grid:
                    self.print_board()
                ship_location = input("Where do you want"
                                      "to place {}".format(self.ships[ship]))
                # if user input is valid
                if self.validate_user_input(ship_location):
                    # get ship locations
                    ship_locations = self.get_ship_locations(ship_location,
                                                            int(self.ships[ship][1]))
                    # check if ship locations are already in use
                    if self.validate_ship_locations(ship_locations):
                        self.clear_screen()
                        self.print_board(self.get_ships_locations(self.ship_grid))
                        break
                    else:
                        print("can't place ship here ...")
                else:
                    print("Please enter correct input")

    # validate user input
    def validate_user_input(self, ship_location):
        if len(ship_location) <= 3:
            ship_location_x = ship_location[:1]
            try:
                ship_location_y = int(ship_location[1:])
            except ValueError:
                return False
            if (ship_location_x in 'abcdefghij' and 
                ship_location_y in [1,2,3,4,5,6,7,8,9,10]):
               return True
        return False

    # returns an array containing ship locations on board
    def get_ship_locations(self, ship_location, ship_length):
        ship_locations = []
        direction = self.get_ship_direction()
        # check if user wants to place ships h or v
        if direction == 'h':
            # convert letter to its ascii value
            # check if it can fit on board
            if (ord('j') - ord(ship_location[:1])) + 1 >= ship_length:
                print("ship length can fit on board")
                for i in range(0, ship_length):                 
                    ship_locations.append(((chr(ord(ship_location[:1]) + i)),
                                           int(ship_location[1:]),
                                           'h'))
                return ship_locations
        elif direction == 'v':
            # check if it can fit on board
            if (10 - (int(ship_location[1:]))) + 1 >= ship_length:
                print("ship length can fit on board")
                for i in range(0, ship_length):
                    ship_locations.append((ship_location[:1],
                                           int(ship_location[1:]) + i,
                                           'v'))
                return ship_locations
        return None

    # check if ship location is already in use
    def validate_ship_locations(self, ship_locations):
        if ship_locations:
            if self.ship_grid:
                for self_ship in self.ship_grid:
                    for self_ship_location in self_ship:
                        for ship_location in ship_locations:
                            if ship_location[:2] == self_ship_location[:2]:
                                return False
            self.ship_grid.append(ship_locations)
            return True
        return False

    # check if user wants the ship horizontally or vertically
    def get_ship_direction(self):
        while True:
            ship_direction = input("Do you want to place ship"
                                   "[H]orizontally or "
                                   "[V]erticlaly ?").strip().lower()
            if ship_direction == 'v':
                return 'v'
            elif ship_direction == 'h':
                return 'h'
            print("Invalid ship direction. Please Enter either V/v or H/h")

    ##################
    # Board related functions
    ##################

    # prints the board heading
    def print_board_heading(self):
        print("" + " ".join([chr(c) for c in range(ord('A'), ord('A') + 10)]))

    # prints the board
    def print_board(self, ship_locations=None):
        print("  ", end=' ')
        self.print_board_heading()
        for row in range(1, 11):
            if row != 10:
                print(row, end='  ')
            else:
                print(row, end=' ')
            for x in 'abcdefghij':
                if ship_locations:
                    if (x, row, 'v') in ship_locations:
                        print('|', end=' ')
                    elif (x, row, 'h') in ship_locations:
                        print('-', end=' ')
                    else:
                        print('0', end=' ')
                else:
                    print('0', end=' ')
            print("\n")

    # gets all the locations of the ships
    def get_ships_locations(self, player_board_ship_gird):
        ships_locations = []
        for ship in player_board_ship_gird:
            for ship_location in ship:
                ships_locations.append(ship_location)
        return ships_locations


