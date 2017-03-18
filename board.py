import pdb

class Board():
	SHIPS = [
	    ("Aircraft Carrier", 5),
	    ("Battleship", 4),
	    ("Submarine", 3),
	    ("Cruiser", 3),
	    ("Patrol Boat", 2)
	]

	ship_board_locations = []

	def __init__(self):
		self.get_ship_location()

	# gets the x and y of ship
	def get_ship_location(self):
		for ship in range(len(self.SHIPS)):
			print("Where do you want to place {} ?".format(self.SHIPS[ship]))
			ship_location_x = int(input("X1: ")) 
			ship_location_y	= int(input("Y1: "))
			if self.validate_ship_location(ship_location_x, ship_location_y):
				print("Ship location validated")
				if self.validate_and_add_ship_board_location(ship_location_x,
											    	 		 ship_location_y,
											    	 		 self.SHIPS[ship][1]):
					print("Ship board location validated")

	# validated if ship location
	def validate_ship_location(self, x, y):
		if x in range(1,11) and y in range(1, 11):
			return True
		return False

	# check if ship location can fit in board
	def validate_and_add_ship_board_location(self, x, y, ship_length):
		# check horizontal or vertical
		if self.horizontal_or_vertical() == "v":
			if y + ship_length <= 10:
				self.append_ship_location_vertically(x, y, ship_length)
				pdb.set_trace()
		elif self.horizontal_or_vertical() == "h":
			if x + ship_length <= 10:
				self.append_ship_location_horizontally(x, y, ship_length)
				pdb.set_trace()
		return False

	# checks if user wants to place ship h or v
	def horizontal_or_vertical(self):
		while True:
			direction = input("Do you want to place the ship V or H").lower().strip()
			if direction == "v":
				return "v"
				break
			elif direction == "h":
				return "h"
				break
			print("You should enter either [v]ertical or [h]orizontal")


	# appends to self.list a list of ship's locations horizontally
	def append_ship_location_horizontally(self, x, y, ship_length):
		if x + (ship_length - 1) <= 10:
			for i in range(x, x+ship_length):
				self.ship_board_locations.append((i,y))

	# appends to self.list a list of ship's locations vertically
	def append_ship_location_vertically(self, x, y, ship_length):
		if y + (ship_length - 1) <= 10:
			for i in range(y, y+ship_length):
				self.ship_board_locations.append((x,i))












