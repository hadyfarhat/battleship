from board import Board

class Player:
	def __init__(self):
		self.name = input("Enter your name: ")
		self.board = Board()
		self.ships = self.put_ship_locations_into_dict(self.board.ship_grid)
		self.misses = []
		self.hits = []
		self.ships_sunk_locations = []
		# self.player_all_ships_locations = get_all_ships_locations(self.board.ship_grid)

	# arrange board ship locations into a dict
	def put_ship_locations_into_dict(self, ship_grid):
		player_ships = {}
		count = 1
		for ship in ship_grid:
			player_ships[count] = []
			for ship_location in ship:
				player_ships[count].append(ship_location)
			count += 1
		return player_ships


