class Player:
	ships = [
        ("Aircraft Carrier", 5),
        ("Battleship", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)
    ]

	def __init__(self, **kwargs):
		self.name = input("Enter your name: ")
		self.get_ship_locations()

	def get_ship_locations(self):
		for i in range(len(self.ships)):
			self.ships[0] += Ship()
			

