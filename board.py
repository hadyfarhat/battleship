import pdb	

class Board:
	# The Board class is responsible for:
	# - Taking user input
	# - Validating User input:
	#		- Slice the input to letter and number
	#		- Validate letter and number
	# - Saving the input into an object (probably an array)
	ships = [
	    ("Aircraft Carrier", 5),
	    ("Battleship", 4),
	    ("Submarine", 3),
	    ("Cruiser", 3),
	    ("Patrol Boat", 2)
	]

	ship_grid = []

	def __init__(self):
		self.set_up()

	# main loop; runs board program
	def set_up(self):
		for ship in range(len(self.ships)):
			while True:
				ship_location = input("Where do you want"
									  "to place {}".format(self.ships[ship]))
				# if user input is valid
				if self.validate_user_input(ship_location):
					# get ship locations
					ship_locations = self.get_ship_locations(ship_location,
															int(self.ships[ship][1]))
					# check if ship locations are already in use
					if self.validate_ship_locations(ship_locations):						
						print("ship is not in use")
						break
					else:
						print("can't place ship here ...")

	# validate user input
	def validate_user_input(self, ship_location):
		if len(ship_location) <= 3:
			ship_location_x = ship_location[:1]
			ship_location_y = int(ship_location[1:])
			if (ship_location_x in 'abcdefghij' and 
				ship_location_y in [1,2,3,4,5,6,7,8,9,10]):
			   return True
		return False

	# returns an array containing ship locations on board
	def get_ship_locations(self, ship_location, ship_length):
		ship_locations = []
		# check if user wants to place ships h or v
		if self.get_ship_direction() == 'h':
			if (ord('j') - ord(ship_location[:1])) + 1 >= ship_length:
				print("ship length can fit on board")
				for i in range(0, ship_length + 1):					
					ship_locations.append((int(ship_location[1:]),
										   chr(ord(ship_location[:1]) + i)))
				return ship_locations
		return None

	# check if ship location is already in use
	def validate_ship_locations(self, ship_locations):
		if ship_locations:
			if self.ship_grid:
				for ship in self.ship_grid:
					for ship_location in ship_locations:
						if ship_location in ship:
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
