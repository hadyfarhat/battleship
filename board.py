class Board():
	SHIPS = [
	    ("Aircraft Carrier", 5),
	    ("Battleship", 4),
	    ("Submarine", 3),
	    ("Cruiser", 3),
	    ("Patrol Boat", 2)
	]

	board_ship_locations = []

	def __init__(self):
		self.get_ships_location()

	# prompts the user to place each ship in the board 
	def get_ships_location(self):
		for ship in range(len(self.SHIPS)):
			while True:
				ship_location = input("Where do you want"
									   "to place {}: ".format(self.SHIPS[ship]))
				if self.validate_input(ship_location):
					print("Location validated")
					if self.check_if_ship_location_exists(ship_location):
						print("Location already in use")
						continue
					else:
						ship_horizontal_or_vertical = input("Do you want to"
															"place the ship"
															"Horizentolly or"
															"VerticallY ?")
						if ship_horizontal_or_vertical == 'v':
							print("VerticallY")
							if self.validate_vertical_location_on_board(
												self.SHIPS[ship][1], ship_location[1]):
								print("ship location vertical validated")
								self.get_vertical_ship_location(self.SHIPS[ship][1],
																int(ship_location[1]))
							else:
								print("Ship is out of board")
				else:
					print("Ship input is not valid")

	# validate user input ship
	def validate_input(self, ship_location):
		if len(ship_location) == 2:
			if ship_location[0] in 'abcdefghij':
				if ship_location[1] in '0123456789':
					return True
		return False

	# check if ship location exists in the array
	def check_if_ship_location_exists(self, ship_location):
		if ship_location in self.board_ship_locations:
			return True
		return False

	# validate the location if its vertical
	def validate_vertical_location_on_board(self, ship_length, ship_location):
		if (int(ship_location) + (ship_length) - 1 <= 10):
			return True
		return False
	
	# returns the ships's location coordinates
	def get_vertical_ship_location(self, ship_length, ship_location):
		ship_location_coordinates = []
		for y in range(ship_location, ship_location+ship_length+1):
			ship_location_coordinates.append(y)
		self.board_ship_locations.append(ship_location_coordinates)
